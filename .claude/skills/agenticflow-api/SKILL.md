---
name: agenticflow-api
description: Use when calling, integrating, or debugging the AgenticFlow API (api.agenticflow.studio / docs.agenticflow.studio) — voice assistants, calls, phone numbers, SIP trunks, tools, knowledge bases, chat sessions, messaging (WhatsApp/Telegram/SMS/email), chat widgets, or platform webhooks. Also when the user mentions AgenticFlow, Amira voice platform, X-Api-Key, or an endpoint under api.agenticflow.studio.
---

# AgenticFlow API

## Overview

Complete reference for the AgenticFlow Voice AI Platform API — build AI agents for voice, telephony, messaging, and conversational interfaces. **166 REST endpoints + 5 outbound webhook events**, snapshotted from https://docs.agenticflow.studio/api-reference (2026-07-29).

- **Base URL:** `https://api.agenticflow.studio`
- **Auth:** `X-Api-Key: <workspace key>` header on every request (create under Workspace → Settings → API Keys; keys are scoped to one workspace)
- **Idempotency:** send an `Idempotency-Key` header (UUID) on message-send POSTs

## Finding the right endpoint

1. **[endpoints.md](endpoints.md)** — all 166 endpoints as method/path/summary tables, grouped by category. Each summary links to its official doc page (`.md` URLs return clean markdown via curl/WebFetch).
2. **[openapi.yaml](openapi.yaml)** — the full OpenAPI 3.1 spec (request/response schemas, params, enums). Grep for the path, e.g. `grep -n "  /messaging/messages:" openapi.yaml`, then read that region.
3. **Live doc index:** https://docs.agenticflow.studio/llms.txt lists every doc page including guides (messaging billing/quickstart, SIP trunk setup/troubleshooting, widget identity/installation, changelog).

## API categories (endpoint counts)

| Category | Count | Covers |
|---|---|---|
| Assistant | 8 | CRUD + version history/snapshots |
| Tool | 8 | CRUD + versions; function tools call their own `server.url` |
| Call | 6 | Create/list/get/update/delete calls + sanitized log archive |
| Monitor | 5 | Live-call listen/takeover tokens, control messages |
| Phone Number | 5 | Provision (Twilio or BYO SIP), routing, lifecycle |
| SIP Trunk | 6 | Gateways, digest auth, REGISTER mode, credential clearing |
| Chat | 9 | Sessions, buffered/streaming messages, operator injection |
| File | 4 | Upload/list/get/delete knowledge-base documents |
| Knowledge Base | 8 | CRUD + sources + re-sync |
| Folders | 5 | Organize resources by `resourceType` |
| Messaging | 67 | Channels, WhatsApp templates, sends (polymorphic), batches, conversations, contacts, quick replies, opt-outs/consent (TCPA), webhook-delivery debug, media |
| Widget – Admin | 35 | Chat widgets, help-center articles, news, CSAT surveys, audit webhooks, GDPR requests |

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

## Outbound webhooks (platform → your server)

Subscribe via `assistant.webhookEvents`. Five events: `assistant-request` (pre-call, must answer within 7s), `status-update` (call lifecycle), `transcript` (partial/final chunks), `end-of-call-report` (the key post-call event — transcript, recording, analysis), `tool-function-call` (per LLM tool invocation, sync or async). Details: see the Webhooks section in [endpoints.md](endpoints.md) and https://docs.agenticflow.studio/api-reference/webhooks/overview.md

## Common mistakes

- Guessing field names from memory instead of grepping `openapi.yaml` — schemas here are the source of truth.
- Forgetting the `X-Api-Key` header or using a key from the wrong workspace.
- Sending free-form WhatsApp messages outside the 24h window — pre-flight with the window-check endpoint or use a template.
- Deletes are mostly **soft**-deletes (assistants, tools, KBs, chat sessions, widgets); template deletion on Meta is **irreversible**.
- Treating `GET /call/{callId}/logs` as live-streaming — it is archive-only. Während des Calls kommt `source: pending` zurück; für Live-Monitoring stattdessen die Monitor-Endpunkte nutzen.
