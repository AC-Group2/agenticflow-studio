---
name: testautomation-api
description: Use when calling, integrating, or debugging the internal Amira Testautomation API — starting or reading automated test runs for voice/chat agents, conversation analyses with prompt-improvement suggestions, applying/deploying prompt changes, rule data, reported anomalies, or evidence/phrase-frequency search across conversations.
---

# Testautomation API (Amira)

## Overview

Externe Steuerung von Testläufen und Gesprächsanalysen für Amira-Agenten. **14 Endpunkte**, snapshotted von https://<testautomation-host>/api/v1/openapi (2026-07-28).

- **Base URL:** `https://<testautomation-host>/api/v1` — der echte Hostname steht bewusst nicht in diesem Repo. Er kommt aus der Umgebungsvariable `TESTAUTOMATION_BASE_URL` bzw. intern beim Team.
- **Auth:** `Authorization: Bearer <API-Key>` **oder** `X-Api-Key: <API-Key>` — ein Schlüssel gehört zu genau einem Kunden und sieht nur dessen Agenten/Läufe/Analysen.
- **Scopes:** `read` für GET, `write` für POST/PATCH.
- **Langläufer-Pattern:** Testläufe und Analysen sind asynchron. Der POST liefert sofort eine `id` zurück; Fortschritt/Ergebnis per GET auf die ID abfragen. Analyse-Status durchläuft `collecting → classifying → synthesizing → verifying → done`.

Volles Schema (Request/Response-Bodies, Felder): [openapi.json](openapi.json) — grep nach dem Pfad, z.B. `grep -n '"/test-runs"' openapi.json`.

## Endpoints

| Method | Path | Zweck |
|---|---|---|
| GET | `/me` | Zu welchem Kunden gehört dieser API-Key |
| GET | `/agents` | Agenten inkl. Szenarien |
| GET | `/test-runs` | Testläufe auflisten (Filter: `agentId`, `limit`) |
| POST | `/test-runs` | Testlauf starten — komplette aktive Szenario-Suite. **Voice: nur ein Lauf pro Agent gleichzeitig, sonst 409.** |
| GET | `/test-runs/{id}` | Status + Einzelergebnisse eines Testlaufs |
| GET | `/analyses` | Analysen auflisten (Filter: `agentId`) |
| POST | `/analyses` | Gesprächsanalyse starten — wertet echte Produktivgespräche aus, schlägt belegte Prompt-/Tool-Verbesserungen vor; eigene Testanrufe werden ausgeschlossen |
| GET | `/analyses/{id}` | Report einer Analyse — `report` erst gefüllt bei `status=done` |
| POST | `/analyses/{id}/apply` | Prompt-Änderungen freigeben & deployen — siehe Drift-Handling unten |
| GET | `/rules` | Regeldaten (kumulatives Wissen je Agent, Filter: `agentId`) |
| PATCH | `/rules` | Regelstatus setzen |
| GET | `/reports` | Gemeldete Auffälligkeiten (Filter: `agentId`) |
| POST | `/reports` | Auffälligkeit melden — konkrete Call-IDs + Beobachtung; wird sofort geprüft und Regeldaten zugeordnet |
| POST | `/evidence` | Beleg-Suche — zählt per Volltextsuche, in wie vielen Gesprächen eine Formulierung vorkommt (keine KI, keine Zusatzkosten) |

## Wichtig: Drift-Handling bei `/analyses/{id}/apply`

Wurde der Prompt seit der Analyse extern geändert, antwortet die Route mit **409 (drift)**. Dann entweder:
- die Analyse neu laufen lassen, oder
- mit `force=true` erzwingen.

Nach dem Deploy wird der Prompt zurückgelesen und verifiziert; jede Änderung wird versioniert (Rollback möglich).

## Common Mistakes

- Auf synchrone Antwort von `POST /test-runs` oder `POST /analyses` warten — beide sind Langläufer, nur Polling auf `GET .../{id}` liefert das Endergebnis.
- Zweiten Voice-Testlauf für denselben Agenten starten, während einer läuft → 409.
- `report`-Feld einer Analyse lesen, bevor `status=done` erreicht ist — ist bis dahin leer/unvollständig.
- Nach externer Prompt-Änderung `apply` ohne `force=true` erneut aufrufen und den 409 (drift) ignorieren, statt neu zu analysieren.
