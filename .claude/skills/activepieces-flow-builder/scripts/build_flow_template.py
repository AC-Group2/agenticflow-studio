#!/usr/bin/env python3
"""
Activepieces flow-JSON builder (schemaVersion 22, Amira self-hosted server).

Copy this file into your project, adapt the example at the bottom, run it,
then validate the output with validate_flow.py.

Proven rules encoded here (do not remove):
- SHARED wrapper with flows[] (NOT the {"template": ...} format)
- Manual trigger first (webhook/cron triggers break the import; swap in UI later)
- Every step: skip/valid/displayName/lastUpdatedDate + settings.sampleData
  + settings.propertySettings (one MANUAL entry per input key)
- Code steps: pure JS only (isolated-vm: no fetch/npm/Node APIs)
"""
import hashlib
import json

STAMP = "2026-01-01T00:00:00.000Z"
ERR = {"retryOnFailure": {"value": True}, "continueOnFailure": {"value": False}}
ERR_CONT = {"retryOnFailure": {"value": True}, "continueOnFailure": {"value": True}}
PS = lambda keys: {k: {"type": "MANUAL"} for k in keys}

HTTP_KEYS = ["url", "body", "method", "headers", "timeout", "authType", "body_type",
             "use_proxy", "authFields", "failureMode", "queryParams", "proxy_settings",
             "followRedirects", "response_is_binary"]


# --------------------------------------------------------------- triggers

def manual_trigger(next_action):
    """ALWAYS use this as the first piece. Swap to webhook/schedule in the UI after import."""
    return {
        "name": "trigger", "valid": True, "displayName": "Manual Trigger",
        "type": "PIECE_TRIGGER", "lastUpdatedDate": STAMP,
        "settings": {
            "sampleData": {},
            "propertySettings": {"markdown": {"type": "MANUAL"}},
            "pieceName": "@activepieces/piece-manual-trigger",
            "pieceVersion": "0.0.5",
            "triggerName": "manual_trigger",
            "input": {},
        },
        "nextAction": next_action,
    }


# --------------------------------------------------------------- steps

def http_step(name, display, method, url, *, body=None, headers=None, query=None,
              next_action=None, err=None):
    """@activepieces/piece-http send_request. body=None -> no body; dict -> JSON body."""
    step = {
        "name": name, "skip": False, "type": "PIECE", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {
            "input": {
                "url": url,
                "body": {"data": body} if body is not None else {},
                "method": method,
                "headers": headers or {},
                "authType": "NONE",
                "body_type": "json" if body is not None else "none",
                "use_proxy": False, "authFields": {}, "failureMode": "continue_none",
                "queryParams": query or {}, "proxy_settings": {},
                "followRedirects": False, "response_is_binary": False,
            },
            "pieceName": "@activepieces/piece-http", "actionName": "send_request",
            "sampleData": {}, "pieceVersion": "0.11.10",
            "propertySettings": PS(HTTP_KEYS),
            "errorHandlingOptions": err or ERR,
        },
    }
    if next_action:
        step["nextAction"] = next_action
    return step


def zoho_crm_step(name, display, method, url, *, connection="YOUR_ZOHO_CONNECTION",
                  body=None, query=None, next_action=None, err=None):
    """@activepieces/piece-zoho-crm custom_api_call. Note the url-as-object + schema quirk."""
    keys = ["url", "body", "method", "headers", "timeout", "failsafe", "body_type",
            "queryParams", "followRedirects", "response_is_binary"]
    ps = PS(keys)
    ps["url"] = {"type": "MANUAL", "schema": {"url": {
        "type": "SHORT_TEXT", "required": True,
        "description": "You can either use the full URL or the relative path to the base URL\n"
                       "i.e https://www.zohoapis.com/crm/v3/resource or /resource",
        "displayName": "URL", "defaultValue": "https://www.zohoapis.com/crm/v3"}}}
    step = {
        "name": name, "skip": False, "type": "PIECE", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {
            "input": {
                "url": {"url": url},
                "auth": f"{{{{connections['{connection}']}}}}",
                "body": {"data": body} if body is not None else {},
                "method": method,
                "headers": {"Content-Type": "application/json"},
                "failsafe": False,
                "body_type": "json" if body is not None else "none",
                "queryParams": query or {},
                "followRedirects": False, "response_is_binary": False,
            },
            "pieceName": "@activepieces/piece-zoho-crm", "actionName": "custom_api_call",
            "sampleData": {}, "pieceVersion": "0.2.8",
            "propertySettings": ps,
            "errorHandlingOptions": err or ERR,
        },
    }
    if next_action:
        step["nextAction"] = next_action
    return step


def seatable_step(name, display, action, extra_input, *, connection="YOUR_SEATABLE_CONNECTION",
                  next_action=None, err=None):
    """@activepieces/piece-seatable v0.1.3. Actions:
       sql_query  -> {"sql": "...", "parameters": [], "convertKeys": True}
       append_rows-> {"tableName": "...", "rows": [{...}]}
       update_rows-> {"tableName": "...", "updates": [{"row_id": "...", "row": {...}}]}"""
    step = {
        "name": name, "skip": False, "type": "PIECE", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {
            "input": {"auth": f"{{{{connections['{connection}']}}}}", **extra_input},
            "pieceName": "@activepieces/piece-seatable", "actionName": action,
            "sampleData": {}, "pieceVersion": "0.1.3",
            "propertySettings": PS(["auth"] + list(extra_input.keys())),
            "errorHandlingOptions": err or ERR,
        },
    }
    if next_action:
        step["nextAction"] = next_action
    return step


def smtp_step(name, display, *, to, subject, body_tpl, sender="reports@example.com",
              sender_name="Automation", connection="YOUR_SMTP_CONNECTION",
              next_action=None, err=None):
    """@activepieces/piece-smtp send-email v0.4.2, HTML body."""
    keys = ["cc", "to", "bcc", "body", "from", "replyTo", "subject", "body_type",
            "senderName", "attachments", "customHeaders"]
    step = {
        "name": name, "skip": False, "type": "PIECE", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {
            "input": {
                "cc": [], "bcc": [], "to": to if isinstance(to, list) else [to],
                "auth": f"{{{{connections['{connection}']}}}}",
                "body": body_tpl, "from": sender, "replyTo": sender,
                "subject": subject, "body_type": "html", "senderName": sender_name,
                "attachments": [], "customHeaders": {},
            },
            "pieceName": "@activepieces/piece-smtp", "actionName": "send-email",
            "sampleData": {}, "pieceVersion": "0.4.2",
            "propertySettings": PS(keys),
            "errorHandlingOptions": err or ERR,
        },
    }
    if next_action:
        step["nextAction"] = next_action
    return step


def code_step(name, display, code, inputs, *, next_action=None, err=None):
    """CODE step. isolated-vm: PURE JS ONLY - no fetch, no npm, no Node APIs.
       code must be:  export const code = async (inputs) => { ...; return x; }"""
    step = {
        "name": name, "skip": False, "type": "CODE", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {
            "input": inputs,
            "sourceCode": {"code": code, "packageJson": "{}"},
            "sampleData": {},
            "propertySettings": PS(list(inputs.keys())) or {},
            "errorHandlingOptions": err or ERR,
        },
    }
    if next_action:
        step["nextAction"] = next_action
    return step


def loop_step(name, display, items, first_loop_action, *, next_action=None):
    """LOOP_ON_ITEMS. items e.g. \"{{step_2['output']['body']['data']}}\"."""
    step = {
        "name": name, "skip": False, "type": "LOOP_ON_ITEMS", "valid": True,
        "displayName": display, "lastUpdatedDate": STAMP,
        "settings": {"items": items, "sampleData": {},
                     "propertySettings": {"items": {"type": "MANUAL"}}},
        "firstLoopAction": first_loop_action,
    }
    if next_action:
        step["nextAction"] = next_action
    return step


# --------------------------------------------------------------- wrapper

def flow_template(name, pieces, trigger, author="Amira AI"):
    """The SHARED wrapper the server accepts. `pieces` lists every pieceName used."""
    return {
        "name": name, "type": "SHARED", "summary": "", "description": "",
        "tags": [], "blogUrl": "",
        "metadata": {"externalId": hashlib.md5(name.encode()).hexdigest()[:21]},
        "author": author, "categories": [], "pieces": pieces,
        "flows": [{"displayName": name, "trigger": trigger, "valid": True,
                   "schemaVersion": "22", "notes": []}],
        "status": "PUBLISHED",
    }


def save(filename, template):
    with open(filename, "w") as f:
        json.dump(template, f, indent=2)
    json.load(open(filename))  # round-trip check
    print("OK", filename)


# --------------------------------------------------------------- example
if __name__ == "__main__":
    flow = flow_template(
        "Example - Fetch and Notify",
        ["@activepieces/piece-manual-trigger", "@activepieces/piece-http"],
        manual_trigger(
            http_step("step_1", "Call my API", "GET", "https://api.example.com/items",
                      headers={"X-API-Key": "YOUR_API_KEY"},
                      next_action=loop_step(
                          "step_2", "For each item", "{{step_1['output']['body']['items']}}",
                          http_step("step_3", "Notify", "POST", "https://api.example.com/notify",
                                    body={"id": "{{step_2['item']['id']}}"}, err=ERR_CONT),
                      ))),
    )
    save("Example_Flow.json", flow)
