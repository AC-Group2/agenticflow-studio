---
name: agenticflow-api
description: Use when calling, integrating, or debugging the AgenticFlow API (api.agenticflow.studio / docs.agenticflow.studio) — voice assistants, calls, phone numbers, SIP trunks, tools, knowledge bases, chat sessions, messaging (WhatsApp/Telegram/SMS/email), chat widgets, or platform webhooks. Also when the user mentions AgenticFlow, Amira voice platform, X-Api-Key, or an endpoint under api.agenticflow.studio.
---

# AgenticFlow API

## Overview

Complete reference for the AgenticFlow Voice AI Platform API — build AI agents for voice, telephony, messaging, and conversational interfaces. **172 REST endpoints + 17 outbound webhook events**, snapshotted from https://docs.agenticflow.studio/api-reference (2026-08-07).

- **Base URL:** `https://api.agenticflow.studio`
- **Auth:** `X-Api-Key: <workspace key>` header on every request (create under Workspace → Settings → API Keys; keys are scoped to one workspace)
- **Idempotency:** send an `Idempotency-Key` header (UUID) on message-send POSTs

## Finding the right endpoint

1. **[endpoints.md](endpoints.md)** — all 172 endpoints as method/path/summary tables, grouped by category. Each summary links to its official doc page (`.md` URLs return clean markdown via curl/WebFetch).
2. **[openapi.yaml](openapi.yaml)** — the full OpenAPI 3.1 spec (request/response schemas, params, enums). Grep for the path, e.g. `grep -n "  /messaging/messages:" openapi.yaml`, then read that region.
3. **Live doc index:** https://docs.agenticflow.studio/llms.txt lists every doc page including guides (messaging billing/quickstart, SIP trunk setup/troubleshooting, widget identity/installation, changelog).

## API categories (endpoint counts)

| Category | Count | Covers |
|---|---|---|
| Assistant | 8 | CRUD + version history/snapshots |
| Tool | 8 | CRUD + versions; function tools call their own `server.url` |
| Call | 7 | Create/list/get/update/delete calls + live mid-call agent update + sanitized log archive |
| Monitor | 5 | Live-call listen/takeover tokens, control messages |
| Phone Number | 5 | Provision (Twilio or BYO SIP), routing, lifecycle |
| SIP Trunk | 6 | Gateways, digest auth, REGISTER mode, credential clearing |
| Chat | 9 | Sessions, buffered/streaming messages, operator injection |
| File | 4 | Upload/list/get/delete knowledge-base documents |
| Knowledge Base | 8 | CRUD + sources + re-sync |
| Folders | 5 | Organize resources by `resourceType` |
| Billing - Invoices | 4 | List/get invoices, download frozen JSON package, admin-only manual mark-paid |
| Messaging | 68 | Channels, WhatsApp templates, sends (polymorphic), batches, conversations, contacts, quick replies, opt-outs/consent (TCPA), webhook-delivery debug, media |
| Widget – Admin | 35 | Chat widgets, help-center articles, news, CSAT surveys, audit webhooks, GDPR requests |

## Live mid-call agent update — `PATCH /call/{callId}/agent`

Changes a *running* assistant's instructions and/or tools while the caller is still on the line — same connection, same conversation, **not** a transfer/handoff. Typical use: switch language or mode mid-call instead of carrying every variant in one long base prompt.

- At least one of `instructions` / `tools` is required.
- `instructions` + `mode`: `replace` (default) swaps the assistant's instructions for the rest of the call; `append` layers the text on top of the configured prompt, which stays in force.
- `tools` **replaces the whole active set** — resend any tool you want to keep, send `[]` to run with none. Knowledge-base search tools are always retained regardless of what's sent, since they follow the assistant's linked KBs, not this list.
- Returns `200` once the running agent confirms the change; `202` if it was dispatched but not confirmed within the ack window (may still land — check the call timeline via `activeToolNames`/`requestId` on the response, or the call's event log).
- Returns `409` if the call isn't in progress, or if the assistant's model doesn't support live updates.
- Applying a change may require reconnecting to the upstream model (~1s, `reconnected: true` in the response) — the caller's audio leg itself is unaffected.

## Call log archive — `GET /call/{callId}/logs`

Same feed as the dashboard's Logs tab, as JSON. **Archive-only**: records exist only after the call ended *and* the post-call worker flushed the archive. The response carries a `source` field with one of four states:

| `source` | Bedeutung |
|---|---|
| `pending` | Call noch nicht beendet oder Archiv wird noch aufgebaut — Client pollt, bis es umspringt |
| `archive` | Records geladen und sanitized — der Normalfall |
| `expired` | Archiv gemäß Data-Retention-Policy des Assistants gelöscht |
| `unavailable` | Archiv fehlt oder ist unlesbar |

Filter (alle optional, können die Query nur **einschränken**, nie erweitern): `category` (`API`, `Agent`, `Tools`, `Knowledge Base`, `Lifecycle`, `Post-Processing`, `Media Server`, `Telephony`, `System`), `level` (`debug`…`critical`), `event_type` (z.B. `agent_state_changed`), `search` (Substring, max. 200 Zeichen), `limit` (1–10000, default 5000).

Logs werden roh gespeichert (forensische Integrität), die Sanitization läuft beim Lesen: Provider-SDK-Spam und HTTP-Client-Internals werden verworfen; interne Scope-IDs, private IPs, Storage-URLs, Bearer-Tokens und Vendor-Namen redigiert. Rate-Limit pro API-Key/User — siehe `X-RateLimit-*` Response-Header (429 bei Überschreitung).

## Edit template — `PATCH /messaging/channels/{channel_id}/templates/{template_id}`

Edits a WhatsApp template's content and resubmits it to Meta for review.

- `name` and `language` are **immutable** — Meta treats them as the template's identity. To change either, create a new template instead.
- Only templates in `approved`, `rejected` or `paused` are editable. One already `pending` (mid-review) rejects the edit with `422`, naming the current state.
- A successful edit resets the template's status to `pending` — the async status worker flips it once Meta decides, same as a fresh `Create template` call.

## Outbound webhooks (platform → your server)

Call webhooks subscribe via `assistant.webhookEvents`. Five events: `assistant-request` (pre-call, must answer within 7s), `status-update` (call lifecycle), `transcript` (partial/final chunks), `end-of-call-report` (the key post-call event — transcript, recording, analysis), `tool-function-call` (per LLM tool invocation, sync or async).

12 more events cover chat sessions, messaging channels, and widgets (`chat-message`, `chat-session-status-update`, `chat-session-end-report`, `messaging-message-received`/`-status-changed`/`-failed`, `messaging-reaction-added`/`-removed`, `messaging-contact-opted-in`/`-out`, `widget-message-incoming`, `widget-audit-event`) — these are configured per-channel or per-widget (e.g. `PATCH /messaging/channels/{channel_id}`, the `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` CRUD), not via `assistant.webhookEvents`.

Full list: see the Webhooks section in [endpoints.md](endpoints.md) and https://docs.agenticflow.studio/api-reference/webhooks/overview.md

## Mark invoice paid — `POST /billing/invoices/{invoice_id}/mark-paid`

For **manual-contract (off-Stripe) invoices only** — records a payment that landed outside Stripe and triggers the same ledger credit a Stripe `invoice.paid` webhook would. **Idempotent**: calling it again on an already-paid invoice just returns the unchanged record, no duplicate credit.

- Body is optional: `paidAt` (defaults to now) and a free-text `note` (max 500 chars).
- **Auth is tiered, not just "admin"**: platform admins can mark any invoice; tenant admins can mark invoices owned by their own tenant *or* by any org under that tenant (they're the merchant of record for org manual-contract billing); **org admins are blocked outright** — a 403 here usually means an org-level caller tried this.
- Logs an `ActivityLog` row for audit.
- Related: `GET /billing/invoices/{invoice_id}/json` returns a **frozen** snapshot (issuer/bill-to as they were when issued, not current data) as a raw, unwrapped JSON document (no `{success, data}` envelope) — meant to be saved to a file, not parsed like other responses.

## Common mistakes

- Guessing field names from memory instead of grepping `openapi.yaml` — schemas here are the source of truth.
- Forgetting the `X-Api-Key` header or using a key from the wrong workspace.
- Sending free-form WhatsApp messages outside the 24h window — pre-flight with the window-check endpoint or use a template.
- Deletes are mostly **soft**-deletes (assistants, tools, KBs, chat sessions, widgets); template deletion on Meta is **irreversible**.
- Treating `GET /call/{callId}/logs` as live-streaming — it is archive-only. Während des Calls kommt `source: pending` zurück; für Live-Monitoring stattdessen die Monitor-Endpunkte nutzen.
- `PATCH /call/{callId}/agent`: `tools` additiv senden statt des kompletten gewünschten Sets — das Feld **ersetzt** die aktive Toolliste vollständig (Ausnahme: KB-Search-Tools bleiben immer erhalten).
- `POST /billing/invoices/{invoice_id}/mark-paid` als Org-Admin aufrufen — schlägt mit 403 fehl; nur Platform- und Tenant-Admins dürfen manuelle Zahlungen bestätigen.
- `PATCH .../templates/{template_id}` mit geändertem `name`/`language` senden, um ein Template umzubenennen — beide Felder sind unveränderlich; stattdessen ein neues Template anlegen. Ein Edit-Versuch während `pending` (in Review) scheitert mit 422.
