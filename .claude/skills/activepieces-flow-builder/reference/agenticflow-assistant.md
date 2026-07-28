# AgenticFlow assistant payloads that pair with Activepieces tool flows

Verified against a live platform export (July 2026, FM Fujairah POC). When flows serve as
function tools for an AgenticFlow voice assistant, deliver the assistant JSON in **this exact
export shape** — not a minimal hand-written subset. Update existing assistants with
`PATCH /assistant/{id}` using the full body.

## The export shape (all keys, verified)

```json
{
  "type": "realtime",
  "name": "…",
  "firstMessage": "…",
  "firstMessageMode": "assistant-speaks-first",
  "knowledgeBaseIds": [],
  "kbRetrievalMode": "tool",
  "silenceTimeoutSeconds": 30,
  "maxDurationSeconds": 3600,
  "allowInterruptions": true,
  "preemptiveGeneration": true,
  "maxToolSteps": 6,
  "webhookEvents": ["end-of-call-report"],
  "server": { "url": "<end-of-call flow webhook URL>", "secret": "…", "timeoutSeconds": 20 },
  "analysis": { … see below … },
  "dataRetention": { "recordingsDays": 90, "conversationDays": 90, "analysisDays": 90, "callLogArchiveDays": 90 },
  "chatDataRetention": { "conversationDays": 90, "analysisDays": 90, "chatLogArchiveDays": 90 },
  "interruption": { "numWords": 5, "voiceSeconds": 0.5, "backoffSeconds": 1 },
  "idle": { "enabled": false, "timeoutSeconds": 10, "maxPromptCount": 3, "messages": [] },
  "recording": { "stereoEnabled": true, "agentEnabled": false, "customerEnabled": false },
  "monitoring": { "listenEnabled": true, "controlEnabled": true },
  "textProcessing": { "filterMarkdown": true, "filterEmoji": true, "useTtsAlignedTranscript": false },
  "performance": { "minConsecutiveSpeechDelay": 0, "discardAudioIfUninterruptible": true },
  "telephony": { "ivrDetection": false },
  "tier": "premium",
  "voiceCardId": "holly",
  "tierLanguage": null,
  "tierSttOverrides": null, "tierVoiceOverrides": null, "tierRealtimeOverrides": null,
  "modelFallback": null, "voiceFallback": null, "transcriberFallback": null,
  "tools": [ … ],
  "systemPrompt": "…"
}
```

For a hand-off target assistant (reached via transferCall) use
`"firstMessage": ""` + `"firstMessageMode": "assistant-speaks-first-with-model-generated-message"`
so it continues the conversation instead of re-greeting.

## The analysis block — ALWAYS include it

Missing `analysis.structuredData` is the most common gap in hand-written payloads. Without it
there is no per-call structured record for the CRM/log flow. Shape (config key is
`evaluation`; the end-of-call event carries the result as `analysis.successEvaluation`):

```json
"analysis": {
  "summary":       { "enabled": true, "prompt": "<what to summarize, 4-5 sentences, language>", "timeoutSeconds": 10 },
  "structuredData": {
    "enabled": true,
    "prompt": "Extract the structured call record. Use only facts from the conversation and tool results; use 'unknown' or false when not determinable.",
    "timeoutSeconds": 10,
    "jsonSchema": {
      "type": "object",
      "properties": {
        "intent":   { "type": "string", "enum": ["…"], "description": "…" },
        "outcome":  { "type": "string", "enum": ["resolved", "escalated_human", "unresolved"] },
        "some_flag": { "type": "boolean", "description": "True if tool X was called successfully" }
      },
      "required": ["intent", "outcome"]
    }
  },
  "evaluation":    { "enabled": true, "prompt": "<success + sentiment rubric>", "rubric": "DescriptiveScale", "timeoutSeconds": 10 },
  "anonymization": { "enabled": false, "prompt": "", "timeoutSeconds": 30, "maxRetries": 3, "rules": [] }
}
```

Schema design rules that worked:

- **One schema per assistant/use case** (router: intent/transferred_to/resolved_by_ai;
  specialist: domain fields like app_no/status/reference_number). Don't share one generic schema.
- **Enums everywhere possible**, and the enum values must MATCH the categories used in the
  systemPrompt and in the tool `parameters` enums (e.g. emergency categories appear identically
  in all three places). Add `"unknown"` to enums the extractor might not resolve.
- Booleans for "did tool X run" (payment_link_sent, case_created, sms_sent) — that is how the
  demo KPIs (AI resolution rate, transfer distribution) come out of the log for free.
- The extraction `prompt` must say "use only facts from conversation and tool results" and
  define the fallback ('unknown' / false), otherwise the extractor hallucinates.

The consuming Activepieces flow (end-of-call-report → table) should log
`{{trigger['body']['analysis']['summary']}}`, `…['analysis']['successEvaluation']`,
`…['analysis']['structuredData']` (store as one JSON/text column — schemas differ per
assistant) and `{{trigger['body']['call']['assistantId']}}` to tell the assistants apart.

## Tools array — what pairs with the flows

```json
{ "type": "function",
  "function": { "name": "…", "description": "<when to call + preconditions>",
                "parameters": { "type": "object", "properties": { … }, "required": [ … ] } },
  "server": { "url": "<AP flow SYNC webhook URL, ends in /sync>", "timeoutSeconds": 20 } }
```

- Tool flows answer via the **/sync** webhook URL; the last step's output is the tool result.
  Return `{"result": …}` (string or object) — forwarded verbatim to the LLM.
- Put GUARDS in `description` ("Only call after X returned identity_verified=true"), because
  imported AP flows have no branching — the LLM is the branch.
- `transferCall`: `destinations[]` with `{"type": "assistant", "assistantId": "…",
  "transferMode": "rolling-history", "description": "<routing hint for the LLM>"}` or
  `{"type": "number", "number": "…"}`. `rolling-history` = hand-off with full context.
- Always include `{"type": "endCall", "name": "end_call"}`.
- `assistant-request` pre-call routing flows must also use the **/sync** URL and respond
  within a hard **7 s** — keep them to 2 steps (one lookup + one CODE step that returns
  `{assistantId, overrides: {firstMessage, variables}, metadata}`).

## systemPrompt structure that worked for voice

Sections in this order, kept short (voice = 1-3 sentence replies):

1. `# Role` — who, which hotline, languages, "phone call: short, natural, never invent facts".
2. `# Language` — reference call variables injected pre-call (`{{known_caller}}`,
   `{{customer_name}}`, `{{language}}`) and what to do for unknown callers.
3. `# What you handle yourself` / `# Procedure (strict order)` — numbered steps that mirror
   the tool call order; name the exact tool for each step.
4. `# When to transfer` — one line per destination, matching the transferCall descriptions.
5. `# Rules` — hard constraints: confirm before SMS, never read URLs/IDs aloud, safety
   escalations (e.g. life-threatening → advise 999/997 first), when to call end_call.

Keep enums, business hours, and category lists literally identical between systemPrompt,
tool parameters, and structuredData jsonSchema — mismatches are the top cause of wrong
tool arguments and unusable extraction.
