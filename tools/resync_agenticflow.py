#!/usr/bin/env python3
"""Resync the agenticflow-api skill against the live AgenticFlow OpenAPI spec.

Downloads the current spec + doc index, reports which operations were added or
removed compared to the committed snapshot, then rewrites openapi.yaml and
endpoints.md in place.

Usage:
    python3 tools/resync_agenticflow.py            # resync (writes files)
    python3 tools/resync_agenticflow.py --check    # report only, write nothing

Exit codes: 0 = no operation changes, 10 = operations added/removed, 1 = error.
"""
import argparse
import collections
import json
import pathlib
import re
import subprocess
import sys
import tempfile

try:
    import yaml
except ImportError:
    sys.exit("PyYAML fehlt — bitte 'pip install pyyaml' ausführen.")

SPEC_URL = "https://docs.agenticflow.studio/api-reference/openapi.yaml"
INDEX_URL = "https://docs.agenticflow.studio/llms.txt"
SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent / ".claude/skills/agenticflow-api"
METHODS = ("get", "post", "put", "patch", "delete")


def fetch(url: str) -> str:
    """curl instead of urllib — the docs host rejects urllib's default UA with 403."""
    res = subprocess.run(
        ["curl", "-sL", "--max-time", "60", "--fail", url],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        sys.exit(f"Download fehlgeschlagen: {url} (curl exit {res.returncode})")
    return res.stdout


def operations(spec: dict) -> set:
    return {
        (method.upper(), path)
        for path, ops in spec.get("paths", {}).items()
        for method in ops
        if method in METHODS
    }


def render_endpoints(spec: dict, index_text: str) -> str:
    title2url = {
        m.group(1).strip().lower(): m.group(2)
        for m in re.finditer(
            r"- \[(.*?)\]\((https://docs\.agenticflow\.studio/api-reference/[^)]+)\)",
            index_text,
        )
    }

    by_tag = collections.OrderedDict()
    for path, ops in spec["paths"].items():
        for method, op in ops.items():
            if method not in METHODS:
                continue
            tag = (op.get("tags") or ["Other"])[0]
            by_tag.setdefault(tag, []).append(
                (method.upper(), path, (op.get("summary") or "").strip())
            )

    out = [
        "# AgenticFlow API — Complete Endpoint Reference\n",
        "Base URL: `https://api.agenticflow.studio` — Auth: `X-Api-Key: <workspace key>` header on every request.\n",
        "Full request/response schemas: grep `openapi.yaml` in this skill directory for the path "
        '(e.g. `grep -n "  /assistant:" openapi.yaml`). Linked `.md` pages return clean markdown '
        "when fetched with curl/WebFetch.\n",
    ]

    tag_order = [t["name"] for t in spec.get("tags", [])]
    for tag in tag_order + [t for t in by_tag if t not in tag_order]:
        if tag not in by_tag:
            continue
        ops = by_tag[tag]
        out.append(f"\n## {tag} ({len(ops)} endpoints)\n")
        out.append("| Method | Path | Summary |")
        out.append("|---|---|---|")
        for method, path, summary in sorted(ops, key=lambda x: (x[1], x[0])):
            url = title2url.get(summary.lower())
            label = summary.replace("|", "\\|")
            cell = f"[{label}]({url})" if url else label
            out.append(f"| {method} | `{path}` | {cell} |")

    webhooks = spec.get("webhooks", {})
    if webhooks:
        out.append(f"\n## Outbound Webhooks ({len(webhooks)} events)\n")
        out.append(
            "Platform → your server. Subscribe via `assistant.webhookEvents`; function-tool calls "
            "go to the tool's own `server.url`. Overview: "
            "https://docs.agenticflow.studio/api-reference/webhooks/overview.md\n"
        )
        out.append("| Event | Summary |")
        out.append("|---|---|")
        for name, item in webhooks.items():
            op = item.get("post") or next(iter(item.values()))
            label = (op.get("summary") or name).replace("|", "\\|")
            url = title2url.get(label.lower())
            cell = f"[{label}]({url})" if url else label
            out.append(f"| `{name}` | {cell} |")

    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nur berichten, nichts schreiben")
    args = ap.parse_args()

    spec_path = SKILL_DIR / "openapi.yaml"
    if not spec_path.exists():
        sys.exit(f"Snapshot nicht gefunden: {spec_path}")

    raw_new = fetch(SPEC_URL)
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        fh.write(raw_new)
        tmp = fh.name

    new_spec = yaml.safe_load(open(tmp))
    old_spec = yaml.safe_load(open(spec_path))

    old_ops, new_ops = operations(old_spec), operations(new_spec)
    added, removed = sorted(new_ops - old_ops), sorted(old_ops - new_ops)
    wh_added = sorted(set(new_spec.get("webhooks", {})) - set(old_spec.get("webhooks", {})))
    wh_removed = sorted(set(old_spec.get("webhooks", {})) - set(new_spec.get("webhooks", {})))

    summary = {
        "endpoints_before": len(old_ops),
        "endpoints_after": len(new_ops),
        "added": [
            {
                "method": m,
                "path": p,
                "summary": new_spec["paths"][p][m.lower()].get("summary", ""),
                "tag": (new_spec["paths"][p][m.lower()].get("tags") or ["?"])[0],
                "doc_slug": re.sub(r"[^a-z0-9]+", "-",
                                   (new_spec["paths"][p][m.lower()].get("summary") or "").lower()).strip("-"),
            }
            for m, p in added
        ],
        "removed": [{"method": m, "path": p} for m, p in removed],
        "webhooks_added": wh_added,
        "webhooks_removed": wh_removed,
        "spec_bytes_changed": raw_new != spec_path.read_text(),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    if not args.check:
        spec_path.write_text(raw_new)
        (SKILL_DIR / "endpoints.md").write_text(render_endpoints(new_spec, fetch(INDEX_URL)))
        print(f"\ngeschrieben: {spec_path.name}, endpoints.md", file=sys.stderr)

    return 10 if (added or removed or wh_added or wh_removed) else 0


if __name__ == "__main__":
    sys.exit(main())
