# AgenticFlow API — Complete Endpoint Reference

Base URL: `https://api.agenticflow.studio` — Auth: `X-Api-Key: <workspace key>` header on every request.

Full request/response schemas: grep `openapi.yaml` in this skill directory for the path (e.g. `grep -n "  /assistant:" openapi.yaml`). Linked `.md` pages return clean markdown when fetched with curl/WebFetch.


## Assistant (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/assistant` | [List Assistants](https://docs.agenticflow.studio/api-reference/assistant/list-assistants.md) |
| POST | `/assistant` | [Create Assistant](https://docs.agenticflow.studio/api-reference/assistant/create-assistant.md) |
| DELETE | `/assistant/{assistantId}` | [Delete Assistant](https://docs.agenticflow.studio/api-reference/assistant/delete-assistant.md) |
| GET | `/assistant/{assistantId}` | [Get Assistant](https://docs.agenticflow.studio/api-reference/assistant/get-assistant.md) |
| PATCH | `/assistant/{assistantId}` | [Update Assistant](https://docs.agenticflow.studio/api-reference/assistant/update-assistant.md) |
| GET | `/assistant/{assistantId}/versions` | [List versions](https://docs.agenticflow.studio/api-reference/assistant/list-versions.md) |
| GET | `/assistant/{assistantId}/versions/{versionId}` | [Get Assistant Version](https://docs.agenticflow.studio/api-reference/assistant/get-assistant-version.md) |
| PATCH | `/assistant/{assistantId}/versions/{versionId}` | [Update version](https://docs.agenticflow.studio/api-reference/tool/update-version.md) |

## Tool (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/tool` | [List Tools](https://docs.agenticflow.studio/api-reference/tool/list-tools.md) |
| POST | `/tool` | [Create Tool](https://docs.agenticflow.studio/api-reference/tool/create-tool.md) |
| DELETE | `/tool/{toolId}` | [Delete Tool](https://docs.agenticflow.studio/api-reference/tool/delete-tool.md) |
| GET | `/tool/{toolId}` | [Get Tool](https://docs.agenticflow.studio/api-reference/tool/get-tool.md) |
| PATCH | `/tool/{toolId}` | [Update Tool](https://docs.agenticflow.studio/api-reference/tool/update-tool.md) |
| GET | `/tool/{toolId}/versions` | [List Tool Versions](https://docs.agenticflow.studio/api-reference/tool/list-tool-versions.md) |
| GET | `/tool/{toolId}/versions/{versionId}` | [Get Tool Version](https://docs.agenticflow.studio/api-reference/tool/get-tool-version.md) |
| PATCH | `/tool/{toolId}/versions/{versionId}` | [Update version](https://docs.agenticflow.studio/api-reference/tool/update-version.md) |

## File (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/file` | [List Files](https://docs.agenticflow.studio/api-reference/file/list-files.md) |
| POST | `/file` | [Upload a File](https://docs.agenticflow.studio/api-reference/file/upload-a-file.md) |
| DELETE | `/file/{fileId}` | [Delete a File](https://docs.agenticflow.studio/api-reference/file/delete-a-file.md) |
| GET | `/file/{fileId}` | [Get File](https://docs.agenticflow.studio/api-reference/file/get-file.md) |

## Knowledge Base (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/knowledge-base` | [List Knowledge Bases](https://docs.agenticflow.studio/api-reference/knowledge-base/list-knowledge-bases.md) |
| POST | `/knowledge-base` | [Create knowledge base](https://docs.agenticflow.studio/api-reference/knowledge-base/create-knowledge-base.md) |
| DELETE | `/knowledge-base/{kbId}` | [Delete knowledge base](https://docs.agenticflow.studio/api-reference/knowledge-base/delete-knowledge-base.md) |
| GET | `/knowledge-base/{kbId}` | [Get Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/get-knowledge-base.md) |
| PATCH | `/knowledge-base/{kbId}` | [Update knowledge base](https://docs.agenticflow.studio/api-reference/knowledge-base/update-knowledge-base.md) |
| POST | `/knowledge-base/{kbId}/sources` | [Add source](https://docs.agenticflow.studio/api-reference/knowledge-base/add-source.md) |
| DELETE | `/knowledge-base/{kbId}/sources/{sourceId}` | [Remove source](https://docs.agenticflow.studio/api-reference/knowledge-base/remove-source.md) |
| POST | `/knowledge-base/{kbId}/sync` | [Re-Sync All Sources](https://docs.agenticflow.studio/api-reference/knowledge-base/re-sync-all-sources.md) |

## Phone Number (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/phone-number` | [List Phone Numbers](https://docs.agenticflow.studio/api-reference/phone-number/list-phone-numbers.md) |
| POST | `/phone-number` | [Create Phone Number](https://docs.agenticflow.studio/api-reference/phone-number/create-phone-number.md) |
| DELETE | `/phone-number/{phoneNumberId}` | [Delete Phone Number](https://docs.agenticflow.studio/api-reference/phone-number/delete-phone-number.md) |
| GET | `/phone-number/{phoneNumberId}` | [Get Phone Number](https://docs.agenticflow.studio/api-reference/phone-number/get-phone-number.md) |
| PATCH | `/phone-number/{phoneNumberId}` | [Update Phone Number](https://docs.agenticflow.studio/api-reference/phone-number/update-phone-number.md) |

## SIP Trunk (6 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/sip-trunk` | [List SIP Trunks](https://docs.agenticflow.studio/api-reference/sip-trunk/list-sip-trunks.md) |
| POST | `/sip-trunk` | [Create a SIP Trunk](https://docs.agenticflow.studio/api-reference/sip-trunk/create-a-sip-trunk.md) |
| DELETE | `/sip-trunk/{trunkId}` | [Delete a SIP Trunk](https://docs.agenticflow.studio/api-reference/sip-trunk/delete-a-sip-trunk.md) |
| GET | `/sip-trunk/{trunkId}` | [Get SIP Trunk](https://docs.agenticflow.studio/api-reference/sip-trunk/get-sip-trunk.md) |
| PATCH | `/sip-trunk/{trunkId}` | [Update a SIP Trunk](https://docs.agenticflow.studio/api-reference/sip-trunk/update-a-sip-trunk.md) |
| DELETE | `/sip-trunk/{trunkId}/credentials` | [Clear credentials](https://docs.agenticflow.studio/api-reference/sip-trunk/clear-credentials.md) |

## Call (7 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call` | [List Calls](https://docs.agenticflow.studio/api-reference/call/list-calls.md) |
| POST | `/call` | [Create Call](https://docs.agenticflow.studio/api-reference/call/create-call.md) |
| DELETE | `/call/{callId}` | [Delete Call](https://docs.agenticflow.studio/api-reference/call/delete-call.md) |
| GET | `/call/{callId}` | [Get Call](https://docs.agenticflow.studio/api-reference/call/get-call.md) |
| PATCH | `/call/{callId}` | [Update Call](https://docs.agenticflow.studio/api-reference/call/update-call.md) |
| PATCH | `/call/{callId}/agent` | [Update a Live Call's Instructions or Tools](https://docs.agenticflow.studio/api-reference/call/update-a-live-calls-instructions-or-tools.md) |
| GET | `/call/{callId}/logs` | [Get Call Log Archive](https://docs.agenticflow.studio/api-reference/call/get-call-log-archive.md) |

## Monitor (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call/{callId}/monitor` | [Get monitor URLs](https://docs.agenticflow.studio/api-reference/monitor/get-monitor-urls.md) |
| POST | `/call/{callId}/monitor/control` | [Send control](https://docs.agenticflow.studio/api-reference/monitor/send-control.md) |
| POST | `/call/{callId}/monitor/end-takeover` | [End Takeover Session](https://docs.agenticflow.studio/api-reference/monitor/end-takeover-session.md) |
| GET | `/call/{callId}/monitor/listen-token` | [Get Listen-Only Token](https://docs.agenticflow.studio/api-reference/monitor/get-listen-only-token.md) |
| GET | `/call/{callId}/monitor/takeover-token` | [Get Takeover Token](https://docs.agenticflow.studio/api-reference/monitor/get-takeover-token.md) |

## Widget - Admin (35 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/widget/admin/widget-audit-event-catalog` | [List event names](https://docs.agenticflow.studio/api-reference/widget--admin/list-event-names.md) |
| GET | `/widget/admin/widgets` | [List widgets](https://docs.agenticflow.studio/api-reference/widget--admin/list-widgets.md) |
| POST | `/widget/admin/widgets` | [Create widget](https://docs.agenticflow.studio/api-reference/widget--admin/create-widget.md) |
| DELETE | `/widget/admin/widgets/{widget_id}` | [Soft-delete a widget](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-a-widget.md) |
| GET | `/widget/admin/widgets/{widget_id}` | [Get one widget by id](https://docs.agenticflow.studio/api-reference/widget--admin/get-one-widget-by-id.md) |
| PATCH | `/widget/admin/widgets/{widget_id}` | [Update a widget config](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-widget-config.md) |
| GET | `/widget/admin/widgets/{widget_id}/articles` | [List articles](https://docs.agenticflow.studio/api-reference/widget--admin/list-articles.md) |
| POST | `/widget/admin/widgets/{widget_id}/articles` | [Create article](https://docs.agenticflow.studio/api-reference/widget--admin/create-article.md) |
| GET | `/widget/admin/widgets/{widget_id}/articles/categories` | [List categories](https://docs.agenticflow.studio/api-reference/widget--admin/list-categories.md) |
| POST | `/widget/admin/widgets/{widget_id}/articles/categories` | [Create category](https://docs.agenticflow.studio/api-reference/widget--admin/create-category.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Delete category](https://docs.agenticflow.studio/api-reference/widget--admin/delete-category.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Update category](https://docs.agenticflow.studio/api-reference/widget--admin/update-category.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Soft-delete an article](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-an-article.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Update an article](https://docs.agenticflow.studio/api-reference/widget--admin/update-an-article.md) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries` | [List deliveries](https://docs.agenticflow.studio/api-reference/widget--admin/list-deliveries.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries/{delivery_id}/replay` | [Replay delivery](https://docs.agenticflow.studio/api-reference/widget--admin/replay-delivery.md) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [List endpoints](https://docs.agenticflow.studio/api-reference/widget--admin/list-endpoints.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [Create endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/create-endpoint.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Delete endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/delete-endpoint.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Update endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/update-endpoint.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}/test` | [Test endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/test-endpoint.md) |
| GET | `/widget/admin/widgets/{widget_id}/gdpr-requests` | [List GDPR requests](https://docs.agenticflow.studio/api-reference/widget--admin/list-gdpr-requests.md) |
| GET | `/widget/admin/widgets/{widget_id}/news` | [List news posts](https://docs.agenticflow.studio/api-reference/widget--admin/list-news-posts.md) |
| POST | `/widget/admin/widgets/{widget_id}/news` | [Create a news post](https://docs.agenticflow.studio/api-reference/widget--admin/create-a-news-post.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Delete news post](https://docs.agenticflow.studio/api-reference/widget--admin/delete-news-post.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Update a news post](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-news-post.md) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-identity-secret` | [Rotate identity secret](https://docs.agenticflow.studio/api-reference/widget--admin/rotate-identity-secret.md) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-webhook-secret` | [Rotate webhook secret](https://docs.agenticflow.studio/api-reference/widget--admin/rotate-webhook-secret.md) |
| GET | `/widget/admin/widgets/{widget_id}/surveys` | [List surveys](https://docs.agenticflow.studio/api-reference/widget--admin/list-surveys.md) |
| POST | `/widget/admin/widgets/{widget_id}/surveys` | [Create survey](https://docs.agenticflow.studio/api-reference/widget--admin/create-survey.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Soft-delete a survey](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-a-survey.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Update a survey config](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-survey-config.md) |
| GET | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}/responses` | [Get survey stats](https://docs.agenticflow.studio/api-reference/widget--admin/get-survey-stats.md) |
| POST | `/widget/admin/widgets/{widget_id}/upload-header-bg` | [Upload header image](https://docs.agenticflow.studio/api-reference/widget--admin/upload-header-image.md) |
| POST | `/widget/admin/widgets/{widget_id}/upload-logo` | [Upload logo](https://docs.agenticflow.studio/api-reference/widget--admin/upload-logo.md) |

## Folders (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/folders` | [List Folders](https://docs.agenticflow.studio/api-reference/folders/list-folders.md) |
| POST | `/folders` | [Create Folder](https://docs.agenticflow.studio/api-reference/folders/create-folder.md) |
| DELETE | `/folders/{folderId}` | [Delete Folder](https://docs.agenticflow.studio/api-reference/folders/delete-folder.md) |
| GET | `/folders/{folderId}` | [Get Folder](https://docs.agenticflow.studio/api-reference/folders/get-folder.md) |
| PATCH | `/folders/{folderId}` | [Update Folder](https://docs.agenticflow.studio/api-reference/folders/update-folder.md) |

## Billing - Invoices (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/billing/invoices` | [List invoices visible to the caller](https://docs.agenticflow.studio/api-reference/billing--invoices/list-invoices-visible-to-the-caller.md) |
| GET | `/billing/invoices/{invoice_id}` | [Retrieve a single invoice](https://docs.agenticflow.studio/api-reference/billing--invoices/retrieve-a-single-invoice.md) |
| GET | `/billing/invoices/{invoice_id}/json` | [Download an invoice as a JSON package](https://docs.agenticflow.studio/api-reference/billing--invoices/download-an-invoice-as-a-json-package.md) |
| POST | `/billing/invoices/{invoice_id}/mark-paid` | [Confirm an offline payment landed → credits the MC ledger](https://docs.agenticflow.studio/api-reference/billing--invoices/confirm-an-offline-payment-landed-→-credits-the-mc-ledger.md) |

## Chat (9 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/chat/message` | [Send message](https://docs.agenticflow.studio/api-reference/messaging/send-message.md) |
| GET | `/chat/session` | [List chat sessions](https://docs.agenticflow.studio/api-reference/chat/list-chat-sessions.md) |
| POST | `/chat/session` | [Create a chat session](https://docs.agenticflow.studio/api-reference/chat/create-a-chat-session.md) |
| DELETE | `/chat/session/{sessionId}` | [Delete session](https://docs.agenticflow.studio/api-reference/chat/delete-session.md) |
| GET | `/chat/session/{sessionId}` | [Get a chat session](https://docs.agenticflow.studio/api-reference/chat/get-a-chat-session.md) |
| POST | `/chat/session/{sessionId}/close` | [Close a chat session](https://docs.agenticflow.studio/api-reference/chat/close-a-chat-session.md) |
| POST | `/chat/session/{sessionId}/inject` | [Inject message](https://docs.agenticflow.studio/api-reference/chat/inject-message.md) |
| GET | `/chat/session/{sessionId}/logs` | [Get Chat Session Log Archive](https://docs.agenticflow.studio/api-reference/chat/get-chat-session-log-archive.md) |
| GET | `/chat/session/{sessionId}/message` | [List messages](https://docs.agenticflow.studio/api-reference/messaging/list-messages.md) |

## Messaging (68 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/batches` | [List batches](https://docs.agenticflow.studio/api-reference/messaging/list-batches.md) |
| GET | `/messaging/batches/{batch_id}` | [Get batch](https://docs.agenticflow.studio/api-reference/messaging/get-batch.md) |
| POST | `/messaging/batches/{batch_id}/cancel` | [Cancel batch](https://docs.agenticflow.studio/api-reference/messaging/cancel-batch.md) |
| GET | `/messaging/batches/{batch_id}/items` | [List batch items](https://docs.agenticflow.studio/api-reference/messaging/list-batch-items.md) |
| GET | `/messaging/channels` | [List channels](https://docs.agenticflow.studio/api-reference/messaging/list-channels.md) |
| DELETE | `/messaging/channels/{channel_id}` | [Soft-delete a channel](https://docs.agenticflow.studio/api-reference/messaging/soft-delete-a-channel.md) |
| GET | `/messaging/channels/{channel_id}` | [Get a channel by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-channel-by-id.md) |
| PATCH | `/messaging/channels/{channel_id}` | [Update channel](https://docs.agenticflow.studio/api-reference/messaging/update-channel.md) |
| GET | `/messaging/channels/{channel_id}/capabilities` | [Get capabilities](https://docs.agenticflow.studio/api-reference/messaging/get-capabilities.md) |
| POST | `/messaging/channels/{channel_id}/disconnect` | [Disconnect channel](https://docs.agenticflow.studio/api-reference/messaging/disconnect-channel.md) |
| POST | `/messaging/channels/{channel_id}/email/refresh-status` | [Refresh email status](https://docs.agenticflow.studio/api-reference/messaging/refresh-email-status.md) |
| GET | `/messaging/channels/{channel_id}/health` | [Get health](https://docs.agenticflow.studio/api-reference/messaging/get-health.md) |
| POST | `/messaging/channels/{channel_id}/reconnect` | [Reconnect channel](https://docs.agenticflow.studio/api-reference/messaging/reconnect-channel.md) |
| GET | `/messaging/channels/{channel_id}/templates` | [List templates](https://docs.agenticflow.studio/api-reference/messaging/list-templates.md) |
| POST | `/messaging/channels/{channel_id}/templates` | [Create template](https://docs.agenticflow.studio/api-reference/messaging/create-template.md) |
| POST | `/messaging/channels/{channel_id}/templates/sync` | [Sync templates](https://docs.agenticflow.studio/api-reference/messaging/sync-templates.md) |
| DELETE | `/messaging/channels/{channel_id}/templates/{template_id}` | [Delete template](https://docs.agenticflow.studio/api-reference/messaging/delete-template.md) |
| GET | `/messaging/channels/{channel_id}/templates/{template_id}` | [Get a single template](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-template.md) |
| PATCH | `/messaging/channels/{channel_id}/templates/{template_id}` | Edit template |
| POST | `/messaging/channels/{channel_id}/templates/{template_id}/preview` | [Preview template](https://docs.agenticflow.studio/api-reference/messaging/preview-template.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/diagnose` | [Diagnose channel](https://docs.agenticflow.studio/api-reference/messaging/diagnose-channel.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/refresh-status` | [Refresh WhatsApp status](https://docs.agenticflow.studio/api-reference/messaging/refresh-whatsapp-status.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/register` | [Register number](https://docs.agenticflow.studio/api-reference/messaging/register-number.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/resubscribe` | [Resubscribe WABA](https://docs.agenticflow.studio/api-reference/messaging/resubscribe-waba.md) |
| GET | `/messaging/consent` | [List consent records](https://docs.agenticflow.studio/api-reference/messaging/list-consent-records.md) |
| POST | `/messaging/consent` | [Record opt-in](https://docs.agenticflow.studio/api-reference/messaging/record-opt-in.md) |
| GET | `/messaging/consent/{contact_id}` | [Get contact consent](https://docs.agenticflow.studio/api-reference/messaging/get-contact-consent.md) |
| GET | `/messaging/contacts` | [List contacts](https://docs.agenticflow.studio/api-reference/messaging/list-contacts.md) |
| POST | `/messaging/contacts` | [Create a contact](https://docs.agenticflow.studio/api-reference/messaging/create-a-contact.md) |
| GET | `/messaging/contacts/{contact_id}` | [Get a contact by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-contact-by-id.md) |
| PATCH | `/messaging/contacts/{contact_id}` | [Update contact fields](https://docs.agenticflow.studio/api-reference/messaging/update-contact-fields.md) |
| GET | `/messaging/conversations` | [List conversations](https://docs.agenticflow.studio/api-reference/messaging/list-conversations.md) |
| GET | `/messaging/conversations/{conversation_id}` | [Get conversation](https://docs.agenticflow.studio/api-reference/messaging/get-conversation.md) |
| PATCH | `/messaging/conversations/{conversation_id}` | [Update conversation](https://docs.agenticflow.studio/api-reference/messaging/update-conversation.md) |
| POST | `/messaging/conversations/{conversation_id}/assign` | [Assign conversation](https://docs.agenticflow.studio/api-reference/messaging/assign-conversation.md) |
| POST | `/messaging/conversations/{conversation_id}/close` | [Close a conversation](https://docs.agenticflow.studio/api-reference/messaging/close-a-conversation.md) |
| GET | `/messaging/conversations/{conversation_id}/notes` | [List notes](https://docs.agenticflow.studio/api-reference/messaging/list-notes.md) |
| POST | `/messaging/conversations/{conversation_id}/notes` | [Add note](https://docs.agenticflow.studio/api-reference/messaging/add-note.md) |
| DELETE | `/messaging/conversations/{conversation_id}/notes/{note_id}` | [Delete note](https://docs.agenticflow.studio/api-reference/messaging/delete-note.md) |
| POST | `/messaging/conversations/{conversation_id}/read-all` | [Mark all read](https://docs.agenticflow.studio/api-reference/messaging/mark-all-read.md) |
| POST | `/messaging/conversations/{conversation_id}/reopen` | [Reopen conversation](https://docs.agenticflow.studio/api-reference/messaging/reopen-conversation.md) |
| POST | `/messaging/conversations/{conversation_id}/typing` | [Send typing](https://docs.agenticflow.studio/api-reference/messaging/send-typing.md) |
| POST | `/messaging/conversations/{conversation_id}/unassign` | [Unassign conversation](https://docs.agenticflow.studio/api-reference/messaging/unassign-conversation.md) |
| POST | `/messaging/media` | [Upload media](https://docs.agenticflow.studio/api-reference/messaging/upload-media.md) |
| GET | `/messaging/messages` | [List messages](https://docs.agenticflow.studio/api-reference/messaging/list-messages.md) |
| POST | `/messaging/messages` | [Send message](https://docs.agenticflow.studio/api-reference/messaging/send-message.md) |
| POST | `/messaging/messages/bulk` | [Bulk send](https://docs.agenticflow.studio/api-reference/messaging/bulk-send.md) |
| GET | `/messaging/messages/can-send` | [Check send window](https://docs.agenticflow.studio/api-reference/messaging/check-send-window.md) |
| POST | `/messaging/messages/schedule` | [Schedule message](https://docs.agenticflow.studio/api-reference/messaging/schedule-message.md) |
| GET | `/messaging/messages/{message_id}` | [Get message](https://docs.agenticflow.studio/api-reference/messaging/get-message.md) |
| POST | `/messaging/messages/{message_id}/cancel-scheduled` | [Cancel scheduled](https://docs.agenticflow.studio/api-reference/messaging/cancel-scheduled.md) |
| DELETE | `/messaging/messages/{message_id}/reactions` | [Remove reaction](https://docs.agenticflow.studio/api-reference/messaging/remove-reaction.md) |
| POST | `/messaging/messages/{message_id}/reactions` | [Add reaction](https://docs.agenticflow.studio/api-reference/messaging/add-reaction.md) |
| POST | `/messaging/messages/{message_id}/read` | [Mark as read](https://docs.agenticflow.studio/api-reference/messaging/mark-as-read.md) |
| POST | `/messaging/messages/{message_id}/retract` | [Retract message](https://docs.agenticflow.studio/api-reference/messaging/retract-message.md) |
| GET | `/messaging/messages/{message_id}/status-history` | [Get status history](https://docs.agenticflow.studio/api-reference/messaging/get-status-history.md) |
| GET | `/messaging/opt-outs` | [List opt-outs](https://docs.agenticflow.studio/api-reference/messaging/list-opt-outs.md) |
| POST | `/messaging/opt-outs` | [Add opt-out](https://docs.agenticflow.studio/api-reference/messaging/add-opt-out.md) |
| GET | `/messaging/opt-outs/check` | [Check opt-out](https://docs.agenticflow.studio/api-reference/messaging/check-opt-out.md) |
| DELETE | `/messaging/opt-outs/{optout_id}` | [Remove opt-out](https://docs.agenticflow.studio/api-reference/messaging/remove-opt-out.md) |
| GET | `/messaging/quick-replies` | [List quick replies](https://docs.agenticflow.studio/api-reference/messaging/list-quick-replies.md) |
| POST | `/messaging/quick-replies` | [Create a quick reply](https://docs.agenticflow.studio/api-reference/messaging/create-a-quick-reply.md) |
| DELETE | `/messaging/quick-replies/{quick_reply_id}` | [Delete a quick reply](https://docs.agenticflow.studio/api-reference/messaging/delete-a-quick-reply.md) |
| PATCH | `/messaging/quick-replies/{quick_reply_id}` | [Update a quick reply](https://docs.agenticflow.studio/api-reference/messaging/update-a-quick-reply.md) |
| POST | `/messaging/quick-replies/{quick_reply_id}/use` | [Record quick-reply use](https://docs.agenticflow.studio/api-reference/messaging/record-quick-reply-use.md) |
| GET | `/messaging/webhook-deliveries` | [List deliveries](https://docs.agenticflow.studio/api-reference/widget--admin/list-deliveries.md) |
| GET | `/messaging/webhook-deliveries/{delivery_id}` | [Get delivery](https://docs.agenticflow.studio/api-reference/messaging/get-delivery.md) |
| POST | `/messaging/webhook-deliveries/{delivery_id}/retry` | [Retry delivery](https://docs.agenticflow.studio/api-reference/messaging/retry-delivery.md) |

## Outbound Webhooks (17 events)

Platform → your server. Subscribe via `assistant.webhookEvents`; function-tool calls go to the tool's own `server.url`. Overview: https://docs.agenticflow.studio/api-reference/webhooks/overview.md

| Event | Summary |
|---|---|
| `assistant-request` | [Assistant Request](https://docs.agenticflow.studio/api-reference/webhooks/assistant-request.md) |
| `status-update` | [Status Update](https://docs.agenticflow.studio/api-reference/webhooks/status-update.md) |
| `transcript` | [Transcript](https://docs.agenticflow.studio/api-reference/webhooks/transcript.md) |
| `end-of-call-report` | [End of Call Report](https://docs.agenticflow.studio/api-reference/webhooks/end-of-call-report.md) |
| `tool-function-call` | [Tool Function Call](https://docs.agenticflow.studio/api-reference/webhooks/tool-function-call.md) |
| `chat-session-status-update` | Chat Session Status Update |
| `chat-message` | Chat Message |
| `chat-session-end-report` | Chat Session End Report |
| `widget-message-incoming` | Widget Message Incoming |
| `widget-audit-event` | Widget Audit Event |
| `messaging-message-received` | Message Received |
| `messaging-message-status-changed` | Status Changed |
| `messaging-message-failed` | Message Failed |
| `messaging-reaction-added` | Reaction Added |
| `messaging-reaction-removed` | Reaction Removed |
| `messaging-contact-opted-out` | Contact Opted Out |
| `messaging-contact-opted-in` | Contact Opted In |
