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

BASE_URL = "https://docs.agenticflow.studio"
# Since the 2026-09-17 docs migration there is no standalone openapi.yaml anymore.
# Every single operation page embeds the *complete*, merged OpenAPI document (all
# tags, not just its own) inside a Next.js RSC payload, so any stable operation
# page works as an anchor to pull the full spec from.
SPEC_ANCHOR_URL = f"{BASE_URL}/docs/api-reference/voice/assistants/listAssistants"
INDEX_URL = f"{BASE_URL}/llms.txt"
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


def extract_bundled_spec(html: str) -> dict:
    """Pull the embedded `"bundled": {openapi: ...}` spec out of a doc page's RSC payload.

    The page ships it as a JSON value inside a JS string literal
    (`self.__next_f.push([1, "...escaped..."])`), so we locate the enclosing
    string, undo one layer of JSON-string escaping, then brace-match the
    `bundled` object out of the result.
    """
    marker = r'\"bundled\":{\"openapi\"'
    idx = html.find(marker)
    if idx == -1:
        sys.exit(
            "Konnte das eingebettete OpenAPI-Bundle nicht in der Doku-Seite finden "
            "— hat sich das Seitenformat erneut geändert?"
        )
    script_open = '<script>self.__next_f.push([1,"'
    start_script = html.rfind(script_open, 0, idx)
    end_script = html.find('"])</script>', idx)
    if start_script == -1 or end_script == -1:
        sys.exit("Konnte das umschließende Script-Tag des OpenAPI-Bundles nicht abgrenzen.")
    raw_js_string = html[start_script + len(script_open):end_script]
    try:
        unescaped = json.loads('"' + raw_js_string + '"')
    except json.JSONDecodeError as exc:
        sys.exit(f"Konnte den Seiteninhalt nicht als JSON-String dekodieren: {exc}")

    bidx = unescaped.find('"bundled":{"openapi"')
    start = unescaped.find("{", bidx)
    depth, in_str, esc, i = 0, False, False, start
    while i < len(unescaped):
        c = unescaped[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    i += 1
                    break
        i += 1
    return json.loads(unescaped[start:i])


def fetch_spec_yaml(url: str) -> str:
    spec = extract_bundled_spec(fetch(url))
    return yaml.dump(spec, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)


def build_title2url(index_text: str) -> dict:
    return {
        m.group(1).strip().lower(): BASE_URL + m.group(2)
        for m in re.finditer(r"- \[(.*?)\]\((/docs/api-reference/[^)]+)\)", index_text)
    }


def operations(spec: dict) -> set:
    return {
        (method.upper(), path)
        for path, ops in spec.get("paths", {}).items()
        for method in ops
        if method in METHODS
    }


def render_endpoints(spec: dict, title2url: dict) -> str:
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
        '(e.g. `grep -n "  /assistant:" openapi.yaml`). Linked pages are rendered HTML; fetch '
        "`https://docs.agenticflow.studio/llm-content/<page-path>` (same path, no `/docs` prefix) "
        "instead of the linked URL to get clean markdown via curl/WebFetch.\n",
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
            f"{BASE_URL}/docs/api-reference/webhook-events\n"
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

    raw_new = fetch_spec_yaml(SPEC_ANCHOR_URL)
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        fh.write(raw_new)
        tmp = fh.name

    new_spec = yaml.safe_load(open(tmp))
    old_spec = yaml.safe_load(open(spec_path))
    index_text = fetch(INDEX_URL)
    title2url = build_title2url(index_text)

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
                "doc_url": title2url.get((new_spec["paths"][p][m.lower()].get("summary") or "").lower()),
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
        (SKILL_DIR / "endpoints.md").write_text(render_endpoints(new_spec, title2url))
        print(f"\ngeschrieben: {spec_path.name}, endpoints.md", file=sys.stderr)

    return 10 if (added or removed or wh_added or wh_removed) else 0


if __name__ == "__main__":
    sys.exit(main())
