# AgenticFlow API — Complete Endpoint Reference

Base URL: `https://api.agenticflow.studio` — Auth: `X-Api-Key: <workspace key>` header on every request.

Full request/response schemas: grep `openapi.yaml` in this skill directory for the path (e.g. `grep -n "  /assistant:" openapi.yaml`). Linked pages are rendered HTML; fetch `https://docs.agenticflow.studio/llm-content/<page-path>` (same path, no `/docs` prefix) instead of the linked URL to get clean markdown via curl/WebFetch.


## Assistant (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/assistant` | [List Assistants](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/listAssistants) |
| POST | `/assistant` | [Create Assistant](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/createAssistant) |
| DELETE | `/assistant/{assistantId}` | [Delete Assistant](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/deleteAssistant) |
| GET | `/assistant/{assistantId}` | [Get Assistant](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/getAssistant) |
| PATCH | `/assistant/{assistantId}` | [Update Assistant](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/updateAssistant) |
| GET | `/assistant/{assistantId}/versions` | [List versions](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/listAssistantVersions) |
| GET | `/assistant/{assistantId}/versions/{versionId}` | [Get Assistant Version](https://docs.agenticflow.studio/docs/api-reference/voice/assistants/getAssistantVersion) |
| PATCH | `/assistant/{assistantId}/versions/{versionId}` | [Update version](https://docs.agenticflow.studio/docs/api-reference/voice/tools/updateToolVersion) |

## Tool (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/tool` | [List Tools](https://docs.agenticflow.studio/docs/api-reference/voice/tools/listTools) |
| POST | `/tool` | [Create Tool](https://docs.agenticflow.studio/docs/api-reference/voice/tools/createTool) |
| DELETE | `/tool/{toolId}` | [Delete Tool](https://docs.agenticflow.studio/docs/api-reference/voice/tools/deleteTool) |
| GET | `/tool/{toolId}` | [Get Tool](https://docs.agenticflow.studio/docs/api-reference/voice/tools/getTool) |
| PATCH | `/tool/{toolId}` | [Update Tool](https://docs.agenticflow.studio/docs/api-reference/voice/tools/updateTool) |
| GET | `/tool/{toolId}/versions` | [List Tool Versions](https://docs.agenticflow.studio/docs/api-reference/voice/tools/listToolVersions) |
| GET | `/tool/{toolId}/versions/{versionId}` | [Get Tool Version](https://docs.agenticflow.studio/docs/api-reference/voice/tools/getToolVersion) |
| PATCH | `/tool/{toolId}/versions/{versionId}` | [Update version](https://docs.agenticflow.studio/docs/api-reference/voice/tools/updateToolVersion) |

## File (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/file` | [List Files](https://docs.agenticflow.studio/docs/api-reference/knowledge/files/listFiles) |
| POST | `/file` | [Upload a File](https://docs.agenticflow.studio/docs/api-reference/knowledge/files/uploadFile) |
| DELETE | `/file/{fileId}` | [Delete a File](https://docs.agenticflow.studio/docs/api-reference/knowledge/files/deleteFile) |
| GET | `/file/{fileId}` | [Get File](https://docs.agenticflow.studio/docs/api-reference/knowledge/files/getFile) |

## Knowledge Base (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/knowledge-base` | [List Knowledge Bases](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/listKnowledgeBases) |
| POST | `/knowledge-base` | [Create knowledge base](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/createKnowledgeBase) |
| DELETE | `/knowledge-base/{kbId}` | [Delete knowledge base](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/deleteKnowledgeBase) |
| GET | `/knowledge-base/{kbId}` | [Get Knowledge Base](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/getKnowledgeBase) |
| PATCH | `/knowledge-base/{kbId}` | [Update knowledge base](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/updateKnowledgeBase) |
| POST | `/knowledge-base/{kbId}/sources` | [Add source](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/addKnowledgeBaseSource) |
| DELETE | `/knowledge-base/{kbId}/sources/{sourceId}` | [Remove source](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/removeKnowledgeBaseSource) |
| POST | `/knowledge-base/{kbId}/sync` | [Re-Sync All Sources](https://docs.agenticflow.studio/docs/api-reference/knowledge/knowledge-bases/syncKnowledgeBase) |

## Phone Number (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/phone-number` | [List Phone Numbers](https://docs.agenticflow.studio/docs/api-reference/voice/phone-numbers/listPhoneNumbers) |
| POST | `/phone-number` | [Create Phone Number](https://docs.agenticflow.studio/docs/api-reference/voice/phone-numbers/createPhoneNumber) |
| DELETE | `/phone-number/{phoneNumberId}` | [Delete Phone Number](https://docs.agenticflow.studio/docs/api-reference/voice/phone-numbers/deletePhoneNumber) |
| GET | `/phone-number/{phoneNumberId}` | [Get Phone Number](https://docs.agenticflow.studio/docs/api-reference/voice/phone-numbers/getPhoneNumber) |
| PATCH | `/phone-number/{phoneNumberId}` | [Update Phone Number](https://docs.agenticflow.studio/docs/api-reference/voice/phone-numbers/updatePhoneNumber) |

## SIP Trunk (6 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/sip-trunk` | [List SIP Trunks](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/listSipTrunks) |
| POST | `/sip-trunk` | [Create a SIP Trunk](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/createSipTrunk) |
| DELETE | `/sip-trunk/{trunkId}` | [Delete a SIP Trunk](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/deleteSipTrunk) |
| GET | `/sip-trunk/{trunkId}` | [Get SIP Trunk](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/getSipTrunk) |
| PATCH | `/sip-trunk/{trunkId}` | [Update a SIP Trunk](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/updateSipTrunk) |
| DELETE | `/sip-trunk/{trunkId}/credentials` | [Clear credentials](https://docs.agenticflow.studio/docs/api-reference/voice/sip-trunks/clearSipTrunkCredentials) |

## Call (7 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call` | [List Calls](https://docs.agenticflow.studio/docs/api-reference/voice/calls/listCalls) |
| POST | `/call` | [Create Call](https://docs.agenticflow.studio/docs/api-reference/voice/calls/createCall) |
| DELETE | `/call/{callId}` | [Delete Call](https://docs.agenticflow.studio/docs/api-reference/voice/calls/deleteCall) |
| GET | `/call/{callId}` | [Get Call](https://docs.agenticflow.studio/docs/api-reference/voice/calls/getCall) |
| PATCH | `/call/{callId}` | [Update Call](https://docs.agenticflow.studio/docs/api-reference/voice/calls/updateCall) |
| PATCH | `/call/{callId}/agent` | [Update a Live Call's Instructions or Tools](https://docs.agenticflow.studio/docs/api-reference/voice/calls/updateLiveCallAgent) |
| GET | `/call/{callId}/logs` | [Get Call Log Archive](https://docs.agenticflow.studio/docs/api-reference/voice/calls/getCallLogs) |

## Monitor (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/call/{callId}/monitor` | [Get monitor URLs](https://docs.agenticflow.studio/docs/api-reference/voice/monitor/getCallMonitor) |
| POST | `/call/{callId}/monitor/control` | [Send control](https://docs.agenticflow.studio/docs/api-reference/voice/monitor/sendCallControl) |
| POST | `/call/{callId}/monitor/end-takeover` | [End Takeover Session](https://docs.agenticflow.studio/docs/api-reference/voice/monitor/endCallTakeover) |
| GET | `/call/{callId}/monitor/listen-token` | [Get Listen-Only Token](https://docs.agenticflow.studio/docs/api-reference/voice/monitor/getCallListenToken) |
| GET | `/call/{callId}/monitor/takeover-token` | [Get Takeover Token](https://docs.agenticflow.studio/docs/api-reference/voice/monitor/getCallTakeoverToken) |

## Messaging - Channels (15 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/channels` | [List channels](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/listMessagingChannels) |
| DELETE | `/messaging/channels/{channel_id}` | [Soft-delete a channel](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/deleteMessagingChannel) |
| GET | `/messaging/channels/{channel_id}` | [Get a channel by id](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/getMessagingChannel) |
| PATCH | `/messaging/channels/{channel_id}` | [Update channel](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/patchMessagingChannel) |
| GET | `/messaging/channels/{channel_id}/capabilities` | [Get capabilities](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/getMessagingChannelCapabilities) |
| POST | `/messaging/channels/{channel_id}/disconnect` | [Disconnect channel](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/disconnectMessagingChannel) |
| POST | `/messaging/channels/{channel_id}/email/refresh-status` | [Refresh email status](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/refreshEmailChannelStatus) |
| GET | `/messaging/channels/{channel_id}/health` | [Get health](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/getMessagingChannelHealth) |
| POST | `/messaging/channels/{channel_id}/reconnect` | [Reconnect channel](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/reconnectMessagingChannel) |
| GET | `/messaging/channels/{channel_id}/signing-secret` | [Reveal the current outbound-webhook HMAC signing secret](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/revealMessagingSigningSecret) |
| POST | `/messaging/channels/{channel_id}/signing-secret/rotate` | [Rotate the outbound-webhook signing secret and return the new value](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/rotateMessagingSigningSecret) |
| POST | `/messaging/channels/{channel_id}/whatsapp/diagnose` | [Diagnose channel](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/diagnoseWhatsAppChannel) |
| POST | `/messaging/channels/{channel_id}/whatsapp/refresh-status` | [Refresh WhatsApp status](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/refreshWhatsAppChannelStatus) |
| POST | `/messaging/channels/{channel_id}/whatsapp/register` | [Register number](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/registerWhatsAppChannel) |
| POST | `/messaging/channels/{channel_id}/whatsapp/resubscribe` | [Resubscribe WABA](https://docs.agenticflow.studio/docs/api-reference/messaging/channels/resubscribeWhatsAppChannel) |

## Messaging - Onboarding (6 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/messaging/onboarding/email` | [Connect a Resend email channel](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/onboardEmail) |
| POST | `/messaging/onboarding/sms/twilio` | [Connect a Twilio SMS channel](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/onboardSmsTwilio) |
| POST | `/messaging/onboarding/telegram` | [Connect a Telegram bot](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/onboardTelegram) |
| POST | `/messaging/onboarding/whatsapp/connect-ticket` | [Mint a one-time ticket for the hosted WhatsApp connect popup](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/createWhatsAppConnectTicket) |
| POST | `/messaging/onboarding/whatsapp/embedded-signup` | [Complete WhatsApp onboarding via Meta's Embedded Signup popup](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/onboardWhatsAppEmbeddedSignup) |
| POST | `/messaging/onboarding/whatsapp/manual` | [Connect a WhatsApp number by pasting credentials](https://docs.agenticflow.studio/docs/api-reference/messaging/onboarding/onboardWhatsAppManual) |

## Messaging - Templates (7 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/channels/{channel_id}/templates` | [List templates](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/listMessagingTemplates) |
| POST | `/messaging/channels/{channel_id}/templates` | [Create template](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/createMessagingTemplate) |
| POST | `/messaging/channels/{channel_id}/templates/sync` | [Sync templates](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/syncMessagingTemplates) |
| DELETE | `/messaging/channels/{channel_id}/templates/{template_id}` | [Delete template](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/deleteMessagingTemplate) |
| GET | `/messaging/channels/{channel_id}/templates/{template_id}` | [Get a single template](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/getMessagingTemplate) |
| PATCH | `/messaging/channels/{channel_id}/templates/{template_id}` | [Edit template](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/updateMessagingTemplate) |
| POST | `/messaging/channels/{channel_id}/templates/{template_id}/preview` | [Preview template](https://docs.agenticflow.studio/docs/api-reference/messaging/templates/previewMessagingTemplate) |

## Messaging - Messages (12 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/messages` | [List messages](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/listMessagingMessages) |
| POST | `/messaging/messages` | [Send message](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/sendMessagingMessage) |
| POST | `/messaging/messages/bulk` | [Bulk send](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/bulkSendMessages) |
| GET | `/messaging/messages/can-send` | [Check send window](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/canSendMessagingMessage) |
| POST | `/messaging/messages/schedule` | [Schedule message](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/scheduleMessagingMessage) |
| GET | `/messaging/messages/{message_id}` | [Get message](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/getMessagingMessage) |
| POST | `/messaging/messages/{message_id}/cancel-scheduled` | [Cancel scheduled](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/cancelScheduledMessagingMessage) |
| DELETE | `/messaging/messages/{message_id}/reactions` | [Remove reaction](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/removeMessagingReaction) |
| POST | `/messaging/messages/{message_id}/reactions` | [Add reaction](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/addMessagingReaction) |
| POST | `/messaging/messages/{message_id}/read` | [Mark as read](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/markMessagingMessageRead) |
| POST | `/messaging/messages/{message_id}/retract` | [Retract message](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/retractMessagingMessage) |
| GET | `/messaging/messages/{message_id}/status-history` | [Get status history](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/getMessagingMessageStatusHistory) |

## Messaging - Batches (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/batches` | [List batches](https://docs.agenticflow.studio/docs/api-reference/messaging/batches/listMessagingBatches) |
| GET | `/messaging/batches/{batch_id}` | [Get batch](https://docs.agenticflow.studio/docs/api-reference/messaging/batches/getMessagingBatch) |
| POST | `/messaging/batches/{batch_id}/cancel` | [Cancel batch](https://docs.agenticflow.studio/docs/api-reference/messaging/batches/cancelMessagingBatch) |
| GET | `/messaging/batches/{batch_id}/items` | [List batch items](https://docs.agenticflow.studio/docs/api-reference/messaging/batches/listMessagingBatchItems) |

## Messaging - Conversations (12 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/conversations` | [List conversations](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/listMessagingConversations) |
| GET | `/messaging/conversations/{conversation_id}` | [Get conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/getMessagingConversation) |
| PATCH | `/messaging/conversations/{conversation_id}` | [Update conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/patchMessagingConversation) |
| POST | `/messaging/conversations/{conversation_id}/assign` | [Assign conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/assignMessagingConversation) |
| POST | `/messaging/conversations/{conversation_id}/close` | [Close a conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/closeMessagingConversation) |
| GET | `/messaging/conversations/{conversation_id}/notes` | [List notes](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/listMessagingConversationNotes) |
| POST | `/messaging/conversations/{conversation_id}/notes` | [Add note](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/createMessagingConversationNote) |
| DELETE | `/messaging/conversations/{conversation_id}/notes/{note_id}` | [Delete note](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/deleteMessagingConversationNote) |
| POST | `/messaging/conversations/{conversation_id}/read-all` | [Mark all read](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/readAllMessagingConversation) |
| POST | `/messaging/conversations/{conversation_id}/reopen` | [Reopen conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/reopenMessagingConversation) |
| POST | `/messaging/conversations/{conversation_id}/typing` | [Send typing](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/sendMessagingTypingIndicator) |
| POST | `/messaging/conversations/{conversation_id}/unassign` | [Unassign conversation](https://docs.agenticflow.studio/docs/api-reference/messaging/conversations/unassignMessagingConversation) |

## Messaging - Contacts (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/contacts` | [List contacts](https://docs.agenticflow.studio/docs/api-reference/messaging/contacts/listMessagingContacts) |
| POST | `/messaging/contacts` | [Create a contact](https://docs.agenticflow.studio/docs/api-reference/messaging/contacts/createMessagingContact) |
| GET | `/messaging/contacts/{contact_id}` | [Get a contact by id](https://docs.agenticflow.studio/docs/api-reference/messaging/contacts/getMessagingContact) |
| PATCH | `/messaging/contacts/{contact_id}` | [Update contact fields](https://docs.agenticflow.studio/docs/api-reference/messaging/contacts/patchMessagingContact) |

## Messaging - Quick Replies (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/quick-replies` | [List quick replies](https://docs.agenticflow.studio/docs/api-reference/messaging/quick-replies/listMessagingQuickReplies) |
| POST | `/messaging/quick-replies` | [Create a quick reply](https://docs.agenticflow.studio/docs/api-reference/messaging/quick-replies/createMessagingQuickReply) |
| DELETE | `/messaging/quick-replies/{quick_reply_id}` | [Delete a quick reply](https://docs.agenticflow.studio/docs/api-reference/messaging/quick-replies/deleteMessagingQuickReply) |
| PATCH | `/messaging/quick-replies/{quick_reply_id}` | [Update a quick reply](https://docs.agenticflow.studio/docs/api-reference/messaging/quick-replies/patchMessagingQuickReply) |
| POST | `/messaging/quick-replies/{quick_reply_id}/use` | [Record quick-reply use](https://docs.agenticflow.studio/docs/api-reference/messaging/quick-replies/useMessagingQuickReply) |

## Messaging - Opt-outs (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/opt-outs` | [List opt-outs](https://docs.agenticflow.studio/docs/api-reference/messaging/opt-outs/listMessagingOptOuts) |
| POST | `/messaging/opt-outs` | [Add opt-out](https://docs.agenticflow.studio/docs/api-reference/messaging/opt-outs/createMessagingOptOut) |
| GET | `/messaging/opt-outs/check` | [Check opt-out](https://docs.agenticflow.studio/docs/api-reference/messaging/opt-outs/checkMessagingOptOut) |
| DELETE | `/messaging/opt-outs/{optout_id}` | [Remove opt-out](https://docs.agenticflow.studio/docs/api-reference/messaging/opt-outs/deleteMessagingOptOut) |

## Messaging - Consent (3 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/consent` | [List consent records](https://docs.agenticflow.studio/docs/api-reference/messaging/consent/listMessagingConsent) |
| POST | `/messaging/consent` | [Record opt-in](https://docs.agenticflow.studio/docs/api-reference/messaging/consent/createMessagingConsent) |
| GET | `/messaging/consent/{contact_id}` | [Get contact consent](https://docs.agenticflow.studio/docs/api-reference/messaging/consent/getMessagingConsentForContact) |

## Messaging - Webhook Deliveries (3 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/messaging/webhook-deliveries` | [List deliveries](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetListAuditDeliveries) |
| GET | `/messaging/webhook-deliveries/{delivery_id}` | [Get delivery](https://docs.agenticflow.studio/docs/api-reference/messaging/webhook-deliveries/getMessagingWebhookDelivery) |
| POST | `/messaging/webhook-deliveries/{delivery_id}/retry` | [Retry delivery](https://docs.agenticflow.studio/docs/api-reference/messaging/webhook-deliveries/retryMessagingWebhookDelivery) |

## Messaging - Media (1 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/messaging/media` | [Upload media](https://docs.agenticflow.studio/docs/api-reference/messaging/media/uploadMessagingMedia) |

## Widget - Admin (35 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/widget/admin/widget-audit-event-catalog` | [List event names](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetGetAuditEventCatalog) |
| GET | `/widget/admin/widgets` | [List widgets](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/listWidgets) |
| POST | `/widget/admin/widgets` | [Create widget](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/createWidget) |
| DELETE | `/widget/admin/widgets/{widget_id}` | [Soft-delete a widget](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/deleteWidget) |
| GET | `/widget/admin/widgets/{widget_id}` | [Get one widget by id](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/getWidget) |
| PATCH | `/widget/admin/widgets/{widget_id}` | [Update a widget config](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/updateWidget) |
| GET | `/widget/admin/widgets/{widget_id}/articles` | [List articles](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetListArticlesAdmin) |
| POST | `/widget/admin/widgets/{widget_id}/articles` | [Create article](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetCreateArticle) |
| GET | `/widget/admin/widgets/{widget_id}/articles/categories` | [List categories](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetListArticleCategories) |
| POST | `/widget/admin/widgets/{widget_id}/articles/categories` | [Create category](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetCreateArticleCategory) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Delete category](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetDeleteArticleCategory) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/categories/{category_id}` | [Update category](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetUpdateArticleCategory) |
| DELETE | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Soft-delete an article](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetDeleteArticle) |
| PATCH | `/widget/admin/widgets/{widget_id}/articles/{article_id}` | [Update an article](https://docs.agenticflow.studio/docs/api-reference/widgets/articles/widgetUpdateArticle) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries` | [List deliveries](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetListAuditDeliveries) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-deliveries/{delivery_id}/replay` | [Replay delivery](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetReplayAuditDelivery) |
| GET | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [List endpoints](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetListAuditEndpoints) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints` | [Create endpoint](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetCreateAuditEndpoint) |
| DELETE | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Delete endpoint](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetDeleteAuditEndpoint) |
| PATCH | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}` | [Update endpoint](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetUpdateAuditEndpoint) |
| POST | `/widget/admin/widgets/{widget_id}/audit-webhook-endpoints/{endpoint_id}/test` | [Test endpoint](https://docs.agenticflow.studio/docs/api-reference/widgets/audit-webhooks/widgetTestAuditEndpoint) |
| GET | `/widget/admin/widgets/{widget_id}/gdpr-requests` | [List GDPR requests](https://docs.agenticflow.studio/docs/api-reference/widgets/gdpr/widgetListGdprRequests) |
| GET | `/widget/admin/widgets/{widget_id}/news` | [List news posts](https://docs.agenticflow.studio/docs/api-reference/widgets/news/widgetListNewsAdmin) |
| POST | `/widget/admin/widgets/{widget_id}/news` | [Create a news post](https://docs.agenticflow.studio/docs/api-reference/widgets/news/widgetCreateNews) |
| DELETE | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Delete news post](https://docs.agenticflow.studio/docs/api-reference/widgets/news/widgetDeleteNews) |
| PATCH | `/widget/admin/widgets/{widget_id}/news/{news_id}` | [Update a news post](https://docs.agenticflow.studio/docs/api-reference/widgets/news/widgetUpdateNews) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-identity-secret` | [Rotate identity secret](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/rotateWidgetIdentitySecret) |
| POST | `/widget/admin/widgets/{widget_id}/rotate-webhook-secret` | [Rotate webhook secret](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/rotateWidgetWebhookSecret) |
| GET | `/widget/admin/widgets/{widget_id}/surveys` | [List surveys](https://docs.agenticflow.studio/docs/api-reference/widgets/surveys/widgetListSurveys) |
| POST | `/widget/admin/widgets/{widget_id}/surveys` | [Create survey](https://docs.agenticflow.studio/docs/api-reference/widgets/surveys/widgetCreateSurvey) |
| DELETE | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Soft-delete a survey](https://docs.agenticflow.studio/docs/api-reference/widgets/surveys/widgetDeleteSurvey) |
| PATCH | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}` | [Update a survey config](https://docs.agenticflow.studio/docs/api-reference/widgets/surveys/widgetUpdateSurvey) |
| GET | `/widget/admin/widgets/{widget_id}/surveys/{survey_id}/responses` | [Get survey stats](https://docs.agenticflow.studio/docs/api-reference/widgets/surveys/widgetGetSurveyResponses) |
| POST | `/widget/admin/widgets/{widget_id}/upload-header-bg` | [Upload header image](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/widgetAdminUploadHeaderBg) |
| POST | `/widget/admin/widgets/{widget_id}/upload-logo` | [Upload logo](https://docs.agenticflow.studio/docs/api-reference/widgets/widgets/widgetAdminUploadLogo) |

## Folders (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/folders` | [List Folders](https://docs.agenticflow.studio/docs/api-reference/voice/folders/listFolders) |
| POST | `/folders` | [Create Folder](https://docs.agenticflow.studio/docs/api-reference/voice/folders/createFolder) |
| DELETE | `/folders/{folderId}` | [Delete Folder](https://docs.agenticflow.studio/docs/api-reference/voice/folders/deleteFolder) |
| GET | `/folders/{folderId}` | [Get Folder](https://docs.agenticflow.studio/docs/api-reference/voice/folders/getFolder) |
| PATCH | `/folders/{folderId}` | [Update Folder](https://docs.agenticflow.studio/docs/api-reference/voice/folders/updateFolder) |

## Audio Asset (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/audio-asset` | [List Audio Assets](https://docs.agenticflow.studio/docs/api-reference/voice/audio-assets/listAudioAssets) |
| POST | `/audio-asset` | [Upload an Audio Asset](https://docs.agenticflow.studio/docs/api-reference/voice/audio-assets/uploadAudioAsset) |
| DELETE | `/audio-asset/{assetId}` | [Delete an Audio Asset](https://docs.agenticflow.studio/docs/api-reference/voice/audio-assets/deleteAudioAsset) |
| GET | `/audio-asset/{assetId}` | [Get an Audio Asset](https://docs.agenticflow.studio/docs/api-reference/voice/audio-assets/getAudioAsset) |

## Billing - Invoices (4 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/billing/invoices` | [List invoices visible to the caller](https://docs.agenticflow.studio/docs/api-reference/billing/invoices/listBillingInvoices) |
| GET | `/billing/invoices/{invoice_id}` | [Retrieve a single invoice](https://docs.agenticflow.studio/docs/api-reference/billing/invoices/getBillingInvoice) |
| GET | `/billing/invoices/{invoice_id}/json` | [Download an invoice as a JSON package](https://docs.agenticflow.studio/docs/api-reference/billing/invoices/downloadBillingInvoiceJson) |
| POST | `/billing/invoices/{invoice_id}/mark-paid` | [Confirm an offline payment landed → credits the MC ledger](https://docs.agenticflow.studio/docs/api-reference/billing/invoices/markInvoicePaid) |

## Billing - Plan Switch (1 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/billing/orgs/{org_id}/plans/switch` | [Switch an organization's plan](https://docs.agenticflow.studio/docs/api-reference/billing/plans/switchOrgPlan) |

## Billing - Plans (5 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/billing/org-plans` | [List Org Plans visible to the caller](https://docs.agenticflow.studio/docs/api-reference/billing/plans/listOrgPlans) |
| GET | `/billing/org-plans/{plan_id}` | [Retrieve an Org Plan](https://docs.agenticflow.studio/docs/api-reference/billing/plans/getOrgPlan) |
| POST | `/billing/org-plans/{plan_id}/assign` | [Assign an Org Plan to an organization](https://docs.agenticflow.studio/docs/api-reference/billing/plans/assignOrgPlan) |
| GET | `/billing/org-plans/{plan_id}/preview-assignment` | [Preview the impact of assigning an Org Plan](https://docs.agenticflow.studio/docs/api-reference/billing/plans/previewOrgPlanAssignment) |
| GET | `/billing/organizations/{organization_id}/pricing-policy` | [Retrieve an organization's active PricingPolicy](https://docs.agenticflow.studio/docs/api-reference/billing/plans/getOrganizationPricingPolicy) |

## Billing - Reports (9 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/billing/orgs/{org_id}/balance` | [Read an organization's current ledger balance](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getOrgBalance) |
| GET | `/billing/orgs/{org_id}/transactions` | [Raw ledger feed for an organization](https://docs.agenticflow.studio/docs/api-reference/billing/usage/listOrgTransactions) |
| GET | `/billing/orgs/{org_id}/usage` | [Read an organization's pre-rolled usage aggregates](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getOrgUsage) |
| GET | `/billing/orgs/{org_id}/usage/csv` | [CSV export of an organization's usage aggregates](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getOrgUsageCsv) |
| GET | `/billing/orgs/{org_id}/usage/live` | [Live usage breakdown for an organization](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getOrgUsageLive) |
| GET | `/billing/tenants/{tenant_id}/balance` | [Read a tenant's current wholesale ledger balance](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getTenantBalance) |
| GET | `/billing/tenants/{tenant_id}/transactions` | [Raw wholesale ledger feed for a tenant](https://docs.agenticflow.studio/docs/api-reference/billing/usage/listTenantTransactions) |
| GET | `/billing/tenants/{tenant_id}/usage` | [Read a tenant's pre-rolled usage aggregates](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getTenantUsage) |
| GET | `/billing/tenants/{tenant_id}/usage/live` | [Live usage breakdown for a tenant](https://docs.agenticflow.studio/docs/api-reference/billing/usage/getTenantUsageLive) |

## Billing - Revenue v2 (2 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/billing/tenants/{tenant_id}/revenue/dashboard` | [All Revenue page sections for a tenant](https://docs.agenticflow.studio/docs/api-reference/billing/revenue/getTenantRevenueDashboard) |
| GET | `/billing/tenants/{tenant_id}/revenue/summary` | [Revenue KPI summary for a tenant](https://docs.agenticflow.studio/docs/api-reference/billing/revenue/getTenantRevenueSummary) |

## Billing - Status (2 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/billing/orgs/{org_id}/reactivate` | [Reactivate an organization](https://docs.agenticflow.studio/docs/api-reference/billing/lifecycle/reactivateOrganization) |
| POST | `/billing/orgs/{org_id}/suspend` | [Suspend an organization](https://docs.agenticflow.studio/docs/api-reference/billing/lifecycle/suspendOrganization) |

## Chat (9 endpoints)

| Method | Path | Summary |
|---|---|---|
| POST | `/chat/message` | [Send message](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/sendMessagingMessage) |
| GET | `/chat/session` | [List chat sessions](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/listChatSessions) |
| POST | `/chat/session` | [Create a chat session](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/createChatSession) |
| DELETE | `/chat/session/{sessionId}` | [Delete session](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/deleteChatSession) |
| GET | `/chat/session/{sessionId}` | [Get a chat session](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/getChatSession) |
| POST | `/chat/session/{sessionId}/close` | [Close a chat session](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/closeChatSession) |
| POST | `/chat/session/{sessionId}/inject` | [Inject message](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/injectChatMessage) |
| GET | `/chat/session/{sessionId}/logs` | [Get Chat Session Log Archive](https://docs.agenticflow.studio/docs/api-reference/chat/sessions/getChatSessionLogs) |
| GET | `/chat/session/{sessionId}/message` | [List messages](https://docs.agenticflow.studio/docs/api-reference/messaging/messages/listMessagingMessages) |

## Management - Organizations (8 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/management/tenant/organizations` | [List the organizations under the calling tenant](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/listOrganizations) |
| POST | `/management/tenant/organizations` | [Create an organization under the calling tenant](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/createOrganization) |
| DELETE | `/management/tenant/organizations/{org_id}` | [Delete an organization and cascade-remove its resources](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/deleteOrganization) |
| GET | `/management/tenant/organizations/{org_id}` | [Retrieve one organization](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/getOrganization) |
| PATCH | `/management/tenant/organizations/{org_id}` | [Update an organization](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/updateOrganization) |
| GET | `/management/tenant/organizations/{org_id}/api-keys` | [List an organization's API keys](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/listOrganizationApiKeys) |
| POST | `/management/tenant/organizations/{org_id}/api-keys` | [Issue an API key for an organization](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/createOrganizationApiKey) |
| DELETE | `/management/tenant/organizations/{org_id}/api-keys/{key_id}` | [Revoke one of an organization's API keys](https://docs.agenticflow.studio/docs/api-reference/organizations/organizations/revokeOrganizationApiKey) |

## Management - Tenant Overview (3 endpoints)

| Method | Path | Summary |
|---|---|---|
| GET | `/management/tenant/organizations/{org_id}/workflows/summary` | [Workflow counts for one organization](https://docs.agenticflow.studio/docs/api-reference/organizations/reporting/getOrganizationWorkflowSummary) |
| GET | `/management/tenant/overview` | [Every customer's status, usage and workflow count in one call](https://docs.agenticflow.studio/docs/api-reference/organizations/reporting/getTenantOverview) |
| GET | `/management/tenant/workflows/summary` | [Workflow counts across every organization under the tenant](https://docs.agenticflow.studio/docs/api-reference/organizations/reporting/getTenantWorkflowSummary) |

## Outbound Webhooks (17 events)

Platform → your server. Subscribe via `assistant.webhookEvents`; function-tool calls go to the tool's own `server.url`. Overview: https://docs.agenticflow.studio/docs/api-reference/webhook-events

| Event | Summary |
|---|---|
| `assistant-request` | [Assistant Request](https://docs.agenticflow.studio/docs/api-reference/webhook-events/voice/webhookAssistantRequest) |
| `status-update` | [Status Update](https://docs.agenticflow.studio/docs/api-reference/webhook-events/voice/webhookStatusUpdate) |
| `transcript` | [Transcript](https://docs.agenticflow.studio/docs/api-reference/webhook-events/voice/webhookTranscript) |
| `end-of-call-report` | [End of Call Report](https://docs.agenticflow.studio/docs/api-reference/webhook-events/voice/webhookEndOfCallReport) |
| `tool-function-call` | [Tool Function Call](https://docs.agenticflow.studio/docs/api-reference/webhook-events/voice/webhookToolFunctionCall) |
| `chat-session-status-update` | [Chat Session Status Update](https://docs.agenticflow.studio/docs/api-reference/webhook-events/chat/webhookChatSessionStatusUpdate) |
| `chat-message` | [Chat Message](https://docs.agenticflow.studio/docs/api-reference/webhook-events/chat/webhookChatMessage) |
| `chat-session-end-report` | [Chat Session End Report](https://docs.agenticflow.studio/docs/api-reference/webhook-events/chat/webhookChatSessionEndReport) |
| `widget-message-incoming` | [Widget Message Incoming](https://docs.agenticflow.studio/docs/api-reference/webhook-events/widget/webhookWidgetMessageIncoming) |
| `widget-audit-event` | [Widget Audit Event](https://docs.agenticflow.studio/docs/api-reference/webhook-events/widget/webhookWidgetAuditEvent) |
| `messaging-message-received` | [Message Received](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingMessageReceived) |
| `messaging-message-status-changed` | [Status Changed](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingMessageStatusChanged) |
| `messaging-message-failed` | [Message Failed](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingMessageFailed) |
| `messaging-reaction-added` | [Reaction Added](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingReactionAdded) |
| `messaging-reaction-removed` | [Reaction Removed](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingReactionRemoved) |
| `messaging-contact-opted-out` | [Contact Opted Out](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingContactOptedOut) |
| `messaging-contact-opted-in` | [Contact Opted In](https://docs.agenticflow.studio/docs/api-reference/webhook-events/messaging/webhookMessagingContactOptedIn) |
