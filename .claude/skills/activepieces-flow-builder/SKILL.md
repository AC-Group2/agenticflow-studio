---
name: activepieces-flow-builder
description: "Build importable Activepieces flow JSONs for the Amira self-hosted server (schemaVersion 22). Use whenever the task is to create, generate, fix or debug an Activepieces flow/workflow JSON for import — especially on 'Template file is invalid' errors, when a flow must be delivered as a file, or when converting a described automation into Activepieces steps. Encodes the proven import format (SHARED wrapper, per-step lastUpdatedDate/sampleData/propertySettings), the manual-trigger-first rule, the isolated-vm code-step limits, and known-good piece configs (HTTP, Zoho CRM, SeaTable, SMTP). Also covers the paired AgenticFlow voice-assistant payloads when flows act as assistant tools: the live platform export shape (realtime/tier/voiceCard), the analysis block with per-use-case structuredData jsonSchema, voice systemPrompt structure, and tool/transferCall wiring via /sync webhook URLs."
---

# Activepieces Flow Builder (self-hosted, schemaVersion 22)

Battle-tested rules for generating flow JSONs that import cleanly on the Amira
Activepieces server. Every rule here was learned from a real import failure —
do not "simplify" the format.

## Workflow

1. Design the flow (steps, pieces, references) on paper first.
2. Generate the JSON with `scripts/build_flow_template.py` — copy it into the
   project and adapt; its helpers emit the exact schema below.
3. Validate with `scripts/validate_flow.py <file.json>` before delivering.
4. Tell the user the post-import steps (trigger swap, connections, placeholders).
5. If the flows are tools for an AgenticFlow voice assistant, ALSO deliver the
   assistant JSON per `reference/agenticflow-assistant.md` — full platform export
   shape including the `analysis` block with a per-use-case `structuredData`
   jsonSchema. A tool flow without its assistant payload (or an assistant payload
   without structuredData) is an incomplete delivery.

## The 6 iron rules

1. **Wrapper format** — top level must be the SHARED template wrapper, NOT the
   `{"template": {...}}` format:
   ```json
   {"name", "type": "SHARED", "summary": "", "description": "", "tags": [],
    "blogUrl": "", "metadata": {"externalId": "<any-unique-21-chars>"},
    "author": "…", "categories": [], "pieces": ["@activepieces/piece-…"],
    "flows": [{"displayName", "trigger", "valid": true,
               "schemaVersion": "22", "notes": []}],
    "status": "PUBLISHED"}
   ```

2. **First piece is ALWAYS a Manual Trigger** (`@activepieces/piece-manual-trigger`
   v0.0.5, triggerName `manual_trigger`). Flows whose first piece is a webhook or
   schedule/cron trigger fail to import. The user swaps the trigger in the UI
   AFTER import (→ Catch Webhook v0.1.34 or Schedule), republishes, and only then
   copies the webhook URL.

3. **Every step needs ALL of these keys** (missing any one → "Template file is
   invalid"): `name`, `skip: false`, `type`, `valid: true`, `displayName`,
   `lastUpdatedDate` (ISO string), and inside `settings`: the step inputs,
   `sampleData: {}`, `propertySettings` (one `{"type": "MANUAL"}` entry per input
   key), `errorHandlingOptions: {"retryOnFailure": {"value": bool},
   "continueOnFailure": {"value": bool}}`. This applies to CODE and
   LOOP_ON_ITEMS steps too, not just PIECE steps.

4. **Code steps run in isolated-vm: NO network, NO npm, NO Node APIs.**
   `fetch` throws `ReferenceError: fetch is not defined`. Code steps may only do
   pure JS transformation of their inputs. Anything that needs the network goes
   through an HTTP piece — or an external service the HTTP piece calls
   (the Hetzner pipeline-service pattern).

5. **Reference syntax includes `['output']`**: previous step
   `{{step_1['output']['body']['x']}}`, loop item `{{step_3['item']}}`, trigger
   payload `{{trigger['body']['x']}}`. Loop `items` example:
   `{{step_2['output']['body']['data']}}`.

6. **Connections are instance-specific.** Emit
   `{{connections['PLACEHOLDER_NAME']}}` and instruct the user to reselect the
   connection in each piece step after import. Same for API keys/URLs: use
   `YOUR_*` placeholders, never real secrets, and list them in the handover note.

## Step type skeletons

See `reference/pieces.md` for full, known-good JSON of every piece used so far
(HTTP send_request 0.11.10, Zoho CRM custom_api_call 0.2.8, SeaTable 0.1.3
sql_query/append_rows/update_rows, SMTP send-email 0.4.2, webhook trigger
0.1.34, LOOP_ON_ITEMS, CODE). Key specials:

- **HTTP piece JSON body**: `"body": {"data": <payload>}` with
  `"body_type": "json"`; empty body: `"body": {}` + `"body_type": "none"`.
- **Zoho CRM custom_api_call**: the URL is an object `"url": {"url": "https://…"}`
  and its propertySettings entry carries a `schema` block (copy from reference).
- **LOOP_ON_ITEMS**: `settings: {items, sampleData: {}, propertySettings:
  {"items": {"type": "MANUAL"}}}`, children under `firstLoopAction`, follow-up
  step under `nextAction` of the loop.
- **CODE**: `settings.sourceCode = {"code": "export const code = async (inputs)
  => {…}", "packageJson": "{}"}` plus rule 3's keys. Remember rule 4.

## Post-import checklist (always give to the user)

1. Import via Flows → Import Flow.
2. Replace every `YOUR_*` placeholder (API keys, URLs) in the steps.
3. Reselect connections in every piece step that has one.
4. If the flow should be webhook/cron-triggered: swap the Manual Trigger in the
   UI now, publish, then copy the webhook URL where it is needed.
5. Publish and test-run with a small scope (e.g. limit 1) before scheduling.

## Debugging imports

- "Template file is invalid" → run `scripts/validate_flow.py`; usually a missing
  rule-3 key or the wrong wrapper.
- Piece-version doubts → export ANY existing flow from the target instance and
  copy the exact `pieceVersion` + settings shape from it. The instance's own
  exports are the ground truth (they carry a UTF-8 BOM; read with `utf-8-sig`).
- Flow imports but a code step fails at runtime with `fetch is not defined` →
  rule 4; move the network call to an HTTP piece or external service.
