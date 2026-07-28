# AgenticFlow Studio — Claude Code Skills

Gemeinsame [Claude Code](https://claude.com/claude-code) Skills fürs Team. Skills sind Referenz-Dokumente, die Claude automatisch lädt, wenn eine Aufgabe dazu passt.

## Enthaltene Skills

- **[agenticflow-api](.claude/skills/agenticflow-api/SKILL.md)** — vollständige Referenz für die AgenticFlow Voice-AI-Platform-API (api.agenticflow.studio): 165 REST-Endpunkte + 5 Webhook-Events, inkl. voller OpenAPI-Spec.
- **[testautomation-api](.claude/skills/testautomation-api/SKILL.md)** — Referenz für die interne Amira Testautomation-API: Testläufe, Gesprächsanalysen, Prompt-Deploy mit Drift-Handling, Regeldaten, Beleg-Suche.
- **[activepieces-flow-builder](.claude/skills/activepieces-flow-builder/SKILL.md)** — Aufbau importierbarer Activepieces-Flow-JSONs für den Amira-Server.

## Installation

**Team-weit (empfohlen):** Dieses Repo als Submodule oder direkt in ein Projekt klonen, in dem ihr mit Claude Code arbeitet — Claude Code liest automatisch jeden Ordner unter `.claude/skills/` mit einer `SKILL.md`. Kein Import-Schritt nötig.

```bash
git clone https://github.com/AC-Group2/agenticflow-studio.git
```

Wenn ihr die Skills in einem *anderen* bestehenden Projekt nutzen wollt, kopiert einfach den `.claude/skills/`-Ordner (oder einzelne Unterordner davon) in euer Projektverzeichnis.

**Persönlich (für alle Projekte verfügbar):** Skill-Ordner nach `~/.claude/skills/` kopieren:

```bash
cp -R .claude/skills/agenticflow-api ~/.claude/skills/
cp -R .claude/skills/testautomation-api ~/.claude/skills/
cp -R .claude/skills/activepieces-flow-builder ~/.claude/skills/
```

Danach im nächsten `claude`-Start automatisch verfügbar.

## Skill hinzufügen

Neuen Ordner unter `.claude/skills/<name>/` mit einer `SKILL.md` (Frontmatter: `name`, `description`) anlegen, committen, pushen.
