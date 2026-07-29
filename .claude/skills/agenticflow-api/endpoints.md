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
| GET | `/assistant/{assistantId}/versions` | [List Assistant Versions](https://docs.agenticflow.studio/api-reference/assistant/list-assistant-versions.md) |
| GET | `/assistant/{assistantId}/versions/{versionId}` | [Get Assistant Version](https://docs.agenticflow.studio/api-reference/assistant/get-assistant-version.md) |
| PATCH | `/assistant/{assistantId}/versions/{versionId}` | [Update Assistant Version Metadata](https://docs.agenticflow.studio/api-reference/assistant/update-assistant-version-metadata.md) |

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
| PATCH | `/tool/{toolId}/versions/{versionId}` | [Update Tool Version Metadata](https://docs.agenticflow.studio/api-reference/tool/update-tool-version-metadata.md) |

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
| POST | `/knowledge-base` | [Create a Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/create-a-knowledge-base.md) |
| DELETE | `/knowledge-base/{kbId}` | [Delete a Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/delete-a-knowledge-base.md) |
| GET | `/knowledge-base/{kbId}` | [Get Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/get-knowledge-base.md) |
| PATCH | `/knowledge-base/{kbId}` | [Update a Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/update-a-knowledge-base.md) |
| POST | `/knowledge-base/{kbId}/sources` | [Add a Source to a Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/add-a-source-to-a-knowledge-base.md) |
| DELETE | `/knowledge-base/{kbId}/sources/{sourceId}` | [Remove a Source from a Knowledge Base](https://docs.agenticflow.studio/api-reference/knowledge-base/remove-a-source-from-a-knowledge-base.md) |
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
| DELETE | `/sip-trunk/{trunkId}/credentials` | [Clear SIP Trunk Credentials](https://docs.agenticflow.studio/api-reference/sip-trunk/clear-sip-trunk-credentials.md) |

## Call (6 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call` | [List Calls](https://docs.agenticflow.studio/api-reference/call/list-calls.md) |
| POST | `/call` | [Create Call](https://docs.agenticflow.studio/api-reference/call/create-call.md) |
| DELETE | `/call/{callId}` | [Delete Call](https://docs.agenticflow.studio/api-reference/call/delete-call.md) |
| GET | `/call/{callId}` | [Get Call](https://docs.agenticflow.studio/api-reference/call/get-call.md) |
| PATCH | `/call/{callId}` | [Update Call](https://docs.agenticflow.studio/api-reference/call/update-call.md) |
| GET | `/call/{callId}/logs` | [Get Call Log Archive](https://docs.agenticflow.studio/api-reference/call/get-call-log-archive.md) |

## Monitor (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call/{callId}/monitor` | [Get Live-Call Monitor URLs](https://docs.agenticflow.studio/api-reference/monitor/get-live-call-monitor-urls.md) |
| POST | `/call/{callId}/monitor/control` | [Send Control Message to Live Call](https://docs.agenticflow.studio/api-reference/monitor/send-control-message-to-live-call.md) |
| POST | `/call/{callId}/monitor/end-takeover` | [End Takeover Session](https://docs.agenticflow.studio/api-reference/monitor/end-takeover-session.md) |
| GET | `/call/{callId}/monitor/listen-token` | [Get Listen-Only Token](https://docs.agenticflow.studio/api-reference/monitor/get-listen-only-token.md) |
| GET | `/call/{callId}/monitor/takeover-token` | [Get Takeover Token](https://docs.agenticflow.studio/api-reference/monitor/get-takeover-token.md) |

## Widget - Admin (35 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/widget/admin/widget-audit-event-catalog` | [List supported audit event names (for the admin UI checkbox grid)](https://docs.agenticflow.studio/api-reference/widget--admin/list-supported-audit-event-names-for-the-admin-ui-checkbox-grid.md) |
| GET | `/widget/admin/widgets` | [List widgets for the current organization](https://docs.agenticflow.studio/api-reference/widget--admin/list-widgets-for-the-current-organization.md) |
| POST | `/widget/admin/widgets` | [Create a new chat widget](https://docs.agenticflow.studio/api-reference/widget--admin/create-a-new-chat-widget.md) |
| DELETE | `/widget/admin/widgets/{widget_id}` | [Soft-delete a widget](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-a-widget.md) |
| GET | `/widget/admin/widgets/{widget_id}` | [Get one widget by id](https://docs.agenticflow.studio/api-reference/widget--admin/get-one-widget-by-id.md) |
| PATCH | `/widget/admin/widgets/{widget_id}` | [Update a widget config](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-widget-config.md) |
| GET | `/widget/admin/widgets/{widget_id}/articles` | [List articles (drafts + published) for the widget](https://docs.agenticflow.studio/api-reference/widget--admin/list-articles-drafts-+-published-for-the-widget.md) |
| POST | `/widget/admin/widgets/{widget_id}/articles` | [Create a help-center article](https://docs.agenticflow.studio/api-reference/widget--admin/create-a-help-center-article.md) |
| GET | `/widget/admin/widgets/{widget_id}/articles/categories` | [List article categories](https://docs.agenticflow.studio/api-reference/widget--admin/list-article-categories.md) |
| POST | `/widget/admin/widgets/{widget_id}/articles/categories` | [Create an article category](https://docs.agenticflow.studio/api-reference/widget--admin/create-an-article-category.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Soft-delete an article category](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-an-article-category.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Update an article category](https://docs.agenticflow.studio/api-reference/widget--admin/update-an-article-category.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Soft-delete an article](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-an-article.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Update an article](https://docs.agenticflow.studio/api-reference/widget--admin/update-an-article.md) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries` | [List recent audit webhook deliveries (filter by status / event)](https://docs.agenticflow.studio/api-reference/widget--admin/list-recent-audit-webhook-deliveries-filter-by-status-event.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries/{delivery_id}/replay` | [Replay a failed (or already-delivered) audit webhook delivery](https://docs.agenticflow.studio/api-reference/widget--admin/replay-a-failed-or-already-delivered-audit-webhook-delivery.md) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [List audit webhook endpoints (signing secrets masked)](https://docs.agenticflow.studio/api-reference/widget--admin/list-audit-webhook-endpoints-signing-secrets-masked.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [Create an audit webhook endpoint (returns signing secret ONCE)](https://docs.agenticflow.studio/api-reference/widget--admin/create-an-audit-webhook-endpoint-returns-signing-secret-once.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Delete an audit webhook endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/delete-an-audit-webhook-endpoint.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Update an audit webhook endpoint](https://docs.agenticflow.studio/api-reference/widget--admin/update-an-audit-webhook-endpoint.md) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}/test` | [Fire a test delivery to verify the endpoint is wired up](https://docs.agenticflow.studio/api-reference/widget--admin/fire-a-test-delivery-to-verify-the-endpoint-is-wired-up.md) |
| GET | `/widget/admin/widgets/{widget_id}/gdpr-requests` | [List GDPR data-subject requests for a widget](https://docs.agenticflow.studio/api-reference/widget--admin/list-gdpr-data-subject-requests-for-a-widget.md) |
| GET | `/widget/admin/widgets/{widget_id}/news` | [List news posts (includes drafts) for the widget](https://docs.agenticflow.studio/api-reference/widget--admin/list-news-posts-includes-drafts-for-the-widget.md) |
| POST | `/widget/admin/widgets/{widget_id}/news` | [Create a news post](https://docs.agenticflow.studio/api-reference/widget--admin/create-a-news-post.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Soft-delete a news post](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-a-news-post.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Update a news post](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-news-post.md) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-identity-secret` | [Regenerate the identity HMAC secret (7-day grace)](https://docs.agenticflow.studio/api-reference/widget--admin/regenerate-the-identity-hmac-secret-7-day-grace.md) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-webhook-secret` | [Regenerate the inbound-webhook signing secret (7-day grace)](https://docs.agenticflow.studio/api-reference/widget--admin/regenerate-the-inbound-webhook-signing-secret-7-day-grace.md) |
| GET | `/widget/admin/widgets/{widget_id}/surveys` | [List surveys for the widget](https://docs.agenticflow.studio/api-reference/widget--admin/list-surveys-for-the-widget.md) |
| POST | `/widget/admin/widgets/{widget_id}/surveys` | [Create a survey for the widget](https://docs.agenticflow.studio/api-reference/widget--admin/create-a-survey-for-the-widget.md) |
| DELETE | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Soft-delete a survey](https://docs.agenticflow.studio/api-reference/widget--admin/soft-delete-a-survey.md) |
| PATCH | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Update a survey config](https://docs.agenticflow.studio/api-reference/widget--admin/update-a-survey-config.md) |
| GET | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}/responses` | [Aggregated CSAT response stats for one survey](https://docs.agenticflow.studio/api-reference/widget--admin/aggregated-csat-response-stats-for-one-survey.md) |
| POST | `/widget/admin/widgets/{widget_id}/upload-header-bg` | [Mint a presigned R2 PUT URL for the header background image](https://docs.agenticflow.studio/api-reference/widget--admin/mint-a-presigned-r2-put-url-for-the-header-background-image.md) |
| POST | `/widget/admin/widgets/{widget_id}/upload-logo` | [Mint a presigned R2 PUT URL for the workspace logo image](https://docs.agenticflow.studio/api-reference/widget--admin/mint-a-presigned-r2-put-url-for-the-workspace-logo-image.md) |

## Folders (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/folders` | [List Folders](https://docs.agenticflow.studio/api-reference/folders/list-folders.md) |
| POST | `/folders` | [Create Folder](https://docs.agenticflow.studio/api-reference/folders/create-folder.md) |
| DELETE | `/folders/{folderId}` | [Delete Folder](https://docs.agenticflow.studio/api-reference/folders/delete-folder.md) |
| GET | `/folders/{folderId}` | [Get Folder](https://docs.agenticflow.studio/api-reference/folders/get-folder.md) |
| PATCH | `/folders/{folderId}` | [Update Folder](https://docs.agenticflow.studio/api-reference/folders/update-folder.md) |

## Chat (9 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/chat/message` | [Send a chat message (buffered or streaming)](https://docs.agenticflow.studio/api-reference/chat/send-a-chat-message-buffered-or-streaming.md) |
| GET | `/chat/session` | [List chat sessions](https://docs.agenticflow.studio/api-reference/chat/list-chat-sessions.md) |
| POST | `/chat/session` | [Create a chat session](https://docs.agenticflow.studio/api-reference/chat/create-a-chat-session.md) |
| DELETE | `/chat/session/{sessionId}` | [Soft-delete a chat session](https://docs.agenticflow.studio/api-reference/chat/soft-delete-a-chat-session.md) |
| GET | `/chat/session/{sessionId}` | [Get a chat session](https://docs.agenticflow.studio/api-reference/chat/get-a-chat-session.md) |
| POST | `/chat/session/{sessionId}/close` | [Close a chat session](https://docs.agenticflow.studio/api-reference/chat/close-a-chat-session.md) |
| POST | `/chat/session/{sessionId}/inject` | [Operator-inject a hidden message into a chat session](https://docs.agenticflow.studio/api-reference/chat/operator-inject-a-hidden-message-into-a-chat-session.md) |
| GET | `/chat/session/{sessionId}/logs` | [Get Chat Session Log Archive](https://docs.agenticflow.studio/api-reference/chat/get-chat-session-log-archive.md) |
| GET | `/chat/session/{sessionId}/message` | [List messages in a chat session](https://docs.agenticflow.studio/api-reference/chat/list-messages-in-a-chat-session.md) |

## Messaging (67 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/batches` | [List bulk-send batches for the current org](https://docs.agenticflow.studio/api-reference/messaging/list-bulk-send-batches-for-the-current-org.md) |
| GET | `/messaging/batches/{batch_id}` | [Get a single batch by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-batch-by-id.md) |
| POST | `/messaging/batches/{batch_id}/cancel` | [Cancel a batch — retracts every still-scheduled message under it](https://docs.agenticflow.studio/api-reference/messaging/cancel-a-batch-—-retracts-every-still-scheduled-message-under-it.md) |
| GET | `/messaging/batches/{batch_id}/items` | [List the messages dispatched (or queued) under this batch](https://docs.agenticflow.studio/api-reference/messaging/list-the-messages-dispatched-or-queued-under-this-batch.md) |
| GET | `/messaging/channels` | [List channels for the active organisation](https://docs.agenticflow.studio/api-reference/messaging/list-channels-for-the-active-organisation.md) |
| DELETE | `/messaging/channels/{channel_id}` | [Soft-delete a channel](https://docs.agenticflow.studio/api-reference/messaging/soft-delete-a-channel.md) |
| GET | `/messaging/channels/{channel_id}` | [Get a channel by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-channel-by-id.md) |
| PATCH | `/messaging/channels/{channel_id}` | [Update channel display / webhook / AI binding](https://docs.agenticflow.studio/api-reference/messaging/update-channel-display-webhook-ai-binding.md) |
| GET | `/messaging/channels/{channel_id}/capabilities` | [Return the channel's current capability set (for FE feature flags)](https://docs.agenticflow.studio/api-reference/messaging/return-the-channels-current-capability-set-for-fe-feature-flags.md) |
| POST | `/messaging/channels/{channel_id}/disconnect` | [Disconnect a channel (history preserved, sends blocked)](https://docs.agenticflow.studio/api-reference/messaging/disconnect-a-channel-history-preserved-sends-blocked.md) |
| POST | `/messaging/channels/{channel_id}/email/refresh-status` | [Re-sync an email channel's status from the Resend domain](https://docs.agenticflow.studio/api-reference/messaging/re-sync-an-email-channels-status-from-the-resend-domain.md) |
| GET | `/messaging/channels/{channel_id}/health` | [Get channel health snapshot (quality rating, quota, etc.)](https://docs.agenticflow.studio/api-reference/messaging/get-channel-health-snapshot-quality-rating-quota-etc.md) |
| POST | `/messaging/channels/{channel_id}/reconnect` | [Reconnect a previously-disconnected channel](https://docs.agenticflow.studio/api-reference/messaging/reconnect-a-previously-disconnected-channel.md) |
| GET | `/messaging/channels/{channel_id}/templates` | [List templates synced for a channel](https://docs.agenticflow.studio/api-reference/messaging/list-templates-synced-for-a-channel.md) |
| POST | `/messaging/channels/{channel_id}/templates` | [Submit a new template to the provider for review](https://docs.agenticflow.studio/api-reference/messaging/submit-a-new-template-to-the-provider-for-review.md) |
| POST | `/messaging/channels/{channel_id}/templates/sync` | [Pull latest templates from the provider into our local cache](https://docs.agenticflow.studio/api-reference/messaging/pull-latest-templates-from-the-provider-into-our-local-cache.md) |
| DELETE | `/messaging/channels/{channel_id}/templates/{template_id}` | [Delete a template (irreversible on the provider side)](https://docs.agenticflow.studio/api-reference/messaging/delete-a-template-irreversible-on-the-provider-side.md) |
| GET | `/messaging/channels/{channel_id}/templates/{template_id}` | [Get a single template](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-template.md) |
| POST | `/messaging/channels/{channel_id}/templates/{template_id}/preview` | [Render a template with sample variables — no send](https://docs.agenticflow.studio/api-reference/messaging/render-a-template-with-sample-variables-—-no-send.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/diagnose` | [Ask Meta directly about a WhatsApp channel's state (root-cause inbound issues)](https://docs.agenticflow.studio/api-reference/messaging/ask-meta-directly-about-a-whatsapp-channels-state-root-cause-inbound-issues.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/refresh-status` | [Re-sync a WhatsApp channel's status from Meta](https://docs.agenticflow.studio/api-reference/messaging/re-sync-a-whatsapp-channels-status-from-meta.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/register` | [Register a WhatsApp number on the Cloud API (Pending → Connected)](https://docs.agenticflow.studio/api-reference/messaging/register-a-whatsapp-number-on-the-cloud-api-pending-→-connected.md) |
| POST | `/messaging/channels/{channel_id}/whatsapp/resubscribe` | [Re-push subscribed_fields=messages,... onto the WABA subscription](https://docs.agenticflow.studio/api-reference/messaging/re-push-subscribed_fields=messages-onto-the-waba-subscription.md) |
| GET | `/messaging/consent` | [List consent records (filter by contact or channelType)](https://docs.agenticflow.studio/api-reference/messaging/list-consent-records-filter-by-contact-or-channeltype.md) |
| POST | `/messaging/consent` | [Record an opt-in event (TCPA / Meta compliance)](https://docs.agenticflow.studio/api-reference/messaging/record-an-opt-in-event-tcpa-meta-compliance.md) |
| GET | `/messaging/consent/{contact_id}` | [Get consent records for a specific contact](https://docs.agenticflow.studio/api-reference/messaging/get-consent-records-for-a-specific-contact.md) |
| GET | `/messaging/contacts` | [List contacts in the active organisation](https://docs.agenticflow.studio/api-reference/messaging/list-contacts-in-the-active-organisation.md) |
| POST | `/messaging/contacts` | [Create a contact](https://docs.agenticflow.studio/api-reference/messaging/create-a-contact.md) |
| GET | `/messaging/contacts/{contact_id}` | [Get a contact by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-contact-by-id.md) |
| PATCH | `/messaging/contacts/{contact_id}` | [Update contact fields](https://docs.agenticflow.studio/api-reference/messaging/update-contact-fields.md) |
| GET | `/messaging/conversations` | [List conversations — newest activity first](https://docs.agenticflow.studio/api-reference/messaging/list-conversations-—-newest-activity-first.md) |
| GET | `/messaging/conversations/{conversation_id}` | [Get a single conversation](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-conversation.md) |
| PATCH | `/messaging/conversations/{conversation_id}` | [Update conversation status / snooze / assignee / tags](https://docs.agenticflow.studio/api-reference/messaging/update-conversation-status-snooze-assignee-tags.md) |
| POST | `/messaging/conversations/{conversation_id}/assign` | [Assign a conversation to a user](https://docs.agenticflow.studio/api-reference/messaging/assign-a-conversation-to-a-user.md) |
| POST | `/messaging/conversations/{conversation_id}/close` | [Close a conversation](https://docs.agenticflow.studio/api-reference/messaging/close-a-conversation.md) |
| GET | `/messaging/conversations/{conversation_id}/notes` | [List internal notes on a conversation](https://docs.agenticflow.studio/api-reference/messaging/list-internal-notes-on-a-conversation.md) |
| POST | `/messaging/conversations/{conversation_id}/notes` | [Add an internal note (not sent to contact)](https://docs.agenticflow.studio/api-reference/messaging/add-an-internal-note-not-sent-to-contact.md) |
| DELETE | `/messaging/conversations/{conversation_id}/notes/{note_id}` | [Delete an internal note](https://docs.agenticflow.studio/api-reference/messaging/delete-an-internal-note.md) |
| POST | `/messaging/conversations/{conversation_id}/read-all` | [Mark all messages in a conversation as read (clears unreadCount)](https://docs.agenticflow.studio/api-reference/messaging/mark-all-messages-in-a-conversation-as-read-clears-unreadcount.md) |
| POST | `/messaging/conversations/{conversation_id}/reopen` | [Reopen a closed conversation](https://docs.agenticflow.studio/api-reference/messaging/reopen-a-closed-conversation.md) |
| POST | `/messaging/conversations/{conversation_id}/typing` | [Send a typing indicator to the conversation's contact](https://docs.agenticflow.studio/api-reference/messaging/send-a-typing-indicator-to-the-conversations-contact.md) |
| POST | `/messaging/conversations/{conversation_id}/unassign` | [Clear the assignee on a conversation](https://docs.agenticflow.studio/api-reference/messaging/clear-the-assignee-on-a-conversation.md) |
| POST | `/messaging/media` | [Upload a binary attachment; returns a presigned URL (1h TTL)](https://docs.agenticflow.studio/api-reference/messaging/upload-a-binary-attachment;-returns-a-presigned-url-1h-ttl.md) |
| GET | `/messaging/messages` | [List messages — filter by channel / conversation / contact](https://docs.agenticflow.studio/api-reference/messaging/list-messages-—-filter-by-channel-conversation-contact.md) |
| POST | `/messaging/messages` | [Send a message via any channel (polymorphic body)](https://docs.agenticflow.studio/api-reference/messaging/send-a-message-via-any-channel-polymorphic-body.md) |
| POST | `/messaging/messages/bulk` | [Send a message to many recipients (creates a Batch)](https://docs.agenticflow.studio/api-reference/messaging/send-a-message-to-many-recipients-creates-a-batch.md) |
| GET | `/messaging/messages/can-send` | [Check if a freeform message can be sent given the 24h WhatsApp window](https://docs.agenticflow.studio/api-reference/messaging/check-if-a-freeform-message-can-be-sent-given-the-24h-whatsapp-window.md) |
| POST | `/messaging/messages/schedule` | [Schedule a single message for future dispatch](https://docs.agenticflow.studio/api-reference/messaging/schedule-a-single-message-for-future-dispatch.md) |
| GET | `/messaging/messages/{message_id}` | [Get a single message by id](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-message-by-id.md) |
| POST | `/messaging/messages/{message_id}/cancel-scheduled` | [Cancel a scheduled message before its dispatch tick](https://docs.agenticflow.studio/api-reference/messaging/cancel-a-scheduled-message-before-its-dispatch-tick.md) |
| DELETE | `/messaging/messages/{message_id}/reactions` | [Remove our reaction from a message](https://docs.agenticflow.studio/api-reference/messaging/remove-our-reaction-from-a-message.md) |
| POST | `/messaging/messages/{message_id}/reactions` | [React to a message with an emoji](https://docs.agenticflow.studio/api-reference/messaging/react-to-a-message-with-an-emoji.md) |
| POST | `/messaging/messages/{message_id}/read` | [Mark an inbound message as read (provider-dependent)](https://docs.agenticflow.studio/api-reference/messaging/mark-an-inbound-message-as-read-provider-dependent.md) |
| POST | `/messaging/messages/{message_id}/retract` | [Delete-for-everyone (provider-dependent)](https://docs.agenticflow.studio/api-reference/messaging/delete-for-everyone-provider-dependent.md) |
| GET | `/messaging/messages/{message_id}/status-history` | [Get the full sent → delivered → read timeline](https://docs.agenticflow.studio/api-reference/messaging/get-the-full-sent-→-delivered-→-read-timeline.md) |
| GET | `/messaging/opt-outs` | [List opt-outs for the active organisation](https://docs.agenticflow.studio/api-reference/messaging/list-opt-outs-for-the-active-organisation.md) |
| POST | `/messaging/opt-outs` | [Add a recipient to the opt-out registry (manual)](https://docs.agenticflow.studio/api-reference/messaging/add-a-recipient-to-the-opt-out-registry-manual.md) |
| GET | `/messaging/opt-outs/check` | [Check whether a recipient is opted out on a channel](https://docs.agenticflow.studio/api-reference/messaging/check-whether-a-recipient-is-opted-out-on-a-channel.md) |
| DELETE | `/messaging/opt-outs/{optout_id}` | [Remove a recipient from the opt-out registry (opt-back-in)](https://docs.agenticflow.studio/api-reference/messaging/remove-a-recipient-from-the-opt-out-registry-opt-back-in.md) |
| GET | `/messaging/quick-replies` | [List saved canned responses for the org](https://docs.agenticflow.studio/api-reference/messaging/list-saved-canned-responses-for-the-org.md) |
| POST | `/messaging/quick-replies` | [Create a quick reply](https://docs.agenticflow.studio/api-reference/messaging/create-a-quick-reply.md) |
| DELETE | `/messaging/quick-replies/{quick_reply_id}` | [Delete a quick reply](https://docs.agenticflow.studio/api-reference/messaging/delete-a-quick-reply.md) |
| PATCH | `/messaging/quick-replies/{quick_reply_id}` | [Update a quick reply](https://docs.agenticflow.studio/api-reference/messaging/update-a-quick-reply.md) |
| POST | `/messaging/quick-replies/{quick_reply_id}/use` | [Record a use of a quick reply (bumps usage count)](https://docs.agenticflow.studio/api-reference/messaging/record-a-use-of-a-quick-reply-bumps-usage-count.md) |
| GET | `/messaging/webhook-deliveries` | [List outbound webhook deliveries (debug log)](https://docs.agenticflow.studio/api-reference/messaging/list-outbound-webhook-deliveries-debug-log.md) |
| GET | `/messaging/webhook-deliveries/{delivery_id}` | [Get a single webhook delivery with full attempt history](https://docs.agenticflow.studio/api-reference/messaging/get-a-single-webhook-delivery-with-full-attempt-history.md) |
| POST | `/messaging/webhook-deliveries/{delivery_id}/retry` | [Re-queue a permanently-failed delivery](https://docs.agenticflow.studio/api-reference/messaging/re-queue-a-permanently-failed-delivery.md) |

## Outbound Webhooks (5 events)

Platform → your server. Subscribe via `assistant.webhookEvents`; function-tool calls go to the tool's own `server.url`. Overview: https://docs.agenticflow.studio/api-reference/webhooks/overview.md

| Event | Summary |
|---|---|
| `assistant-request` | [Assistant Request](https://docs.agenticflow.studio/api-reference/webhooks/assistant-request.md) |
| `status-update` | [Status Update](https://docs.agenticflow.studio/api-reference/webhooks/status-update.md) |
| `transcript` | [Transcript](https://docs.agenticflow.studio/api-reference/webhooks/transcript.md) |
| `end-of-call-report` | [End of Call Report](https://docs.agenticflow.studio/api-reference/webhooks/end-of-call-report.md) |
| `tool-function-call` | [Tool Function Call](https://docs.agenticflow.studio/api-reference/webhooks/tool-function-call.md) |
