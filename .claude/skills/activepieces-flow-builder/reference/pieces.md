# Known-good piece configurations (verified on the Amira server, July 2026)

Ground truth: when in doubt, export an existing flow from the target instance and
copy the exact shapes. Instance exports carry a UTF-8 BOM — read with `utf-8-sig`.

## Versions that import cleanly

| Piece | pieceName | Version | Action/Trigger |
|---|---|---|---|
| Manual Trigger | @activepieces/piece-manual-trigger | 0.0.5 | manual_trigger |
| Webhook (UI swap only) | @activepieces/piece-webhook | 0.1.34 | catch_webhook |
| HTTP | @activepieces/piece-http | 0.11.10 | send_request |
| Zoho CRM | @activepieces/piece-zoho-crm | 0.2.8 | custom_api_call |
| SeaTable | @activepieces/piece-seatable | 0.1.3 | sql_query, append_rows, update_rows |
| SMTP | @activepieces/piece-smtp | 0.4.2 | send-email |

## HTTP send_request — input keys (all must exist)

```json
{"url": "…", "body": {}, "method": "GET", "headers": {}, "authType": "NONE",
 "body_type": "none", "use_proxy": false, "authFields": {},
 "failureMode": "continue_none", "queryParams": {}, "proxy_settings": {},
 "followRedirects": false, "response_is_binary": false}
```
JSON body: `"body": {"data": {…payload…}}` + `"body_type": "json"`.
propertySettings: one `{"type": "MANUAL"}` per key above.

## Zoho CRM custom_api_call — the two quirks

1. URL is an **object**: `"url": {"url": "https://www.zohoapis.com/crm/v8/Accounts"}`
2. Its propertySettings entry carries a schema block:
```json
"url": {"type": "MANUAL", "schema": {"url": {"type": "SHORT_TEXT", "required": true,
  "description": "You can either use the full URL or the relative path to the base URL\ni.e https://www.zohoapis.com/crm/v3/resource or /resource",
  "displayName": "URL", "defaultValue": "https://www.zohoapis.com/crm/v3"}}}
```
Auth: `"auth": "{{connections['XXXX']}}"` — user reselects after import.
GET records needs queryParams `fields` (mandatory in v3+) and `per_page`.
Write-back: PUT /crm/v8/Accounts with body `{"data": [{"id": "…", "Field": "…"}]}`.

## SeaTable v0.1.3 — action inputs

```json
sql_query:   {"auth": "…", "sql": "SELECT * FROM T WHERE x = ?", "parameters": ["v"], "convertKeys": true}
append_rows: {"auth": "…", "rows": [{"col": "val"}]}           // + "tableName" where used
update_rows: {"auth": "…", "tableName": "T", "updates": [{"row_id": "{{step_X['item']['_id']}}", "row": {"col": "val"}}]}
```
SQL results come back in `['output']['results']`. SeaTable SQL defaults to
LIMIT 100 — always append an explicit `LIMIT 10000` for full-table reads.

## SMTP send-email v0.4.2 — input keys

```json
{"cc": [], "to": ["a@b.com"], "bcc": [], "auth": "{{connections['…']}}",
 "body": "<html…>", "from": "…", "replyTo": "…", "subject": "…",
 "body_type": "html", "senderName": "…", "attachments": [], "customHeaders": {}}
```

## Webhook trigger (for the UI swap — never as the imported first piece)

```json
{"sampleData": {}, "propertySettings": {"authType": {"type": "MANUAL"},
  "authFields": {"type": "MANUAL", "schema": {}}},
 "pieceName": "@activepieces/piece-webhook", "pieceVersion": "0.1.34",
 "triggerName": "catch_webhook", "input": {"authType": "none", "authFields": {}}}
```
Webhook payload is referenced as `{{trigger['body']['field']}}`.

## Server runtime facts

- Code steps run in **isolated-vm**: no `fetch`, no npm, no Node APIs
  (`Buffer`, `process`, …). Pure JS transformation only. `AP_EXECUTION_MODE`
  cannot be changed on this server.
- Pattern for anything network-heavy: HTTP piece → external service
  (e.g. FastAPI wrapper on Hetzner with `X-API-Key` auth), service does the work,
  flow polls a `/status` endpoint.
- Flows triggered externally: give the flow a Catch Webhook trigger (UI swap
  after import), then POST to `https://<ap-server>/api/v1/webhooks/<flow-id>`.
