# Jarvis — HOD AI Agent System

Internal tool. Adapts OpenJarvis (https://github.com/open-jarvis/OpenJarvis) for House of David operations.

**Goal:** Replace manual Claude Code session workflow with a proper local-first agent runtime — improved skill system, scheduled agents, continuous agents, desktop GUI.

**Role (primary):** Python developer / AI systems architect. You own the architecture and implementation.

**Phase:** 0 — Exploration + planning. No code yet.

---

## Session Start

Read `WORKLOG.md` — pending `[ ]` tasks are the todo, completed `[x]` entries are the history.

---

## Stack

- Python (primary — 3.10+)
- OpenJarvis patterns (local-first agent framework, skills system, Ollama)
- Tauri (desktop GUI — Phase 4, not now)

## Key Sources

- Reference repo: https://github.com/open-jarvis/OpenJarvis
- Existing HOD skills: `C:\Users\davei\.claude\skills\`
- HOD skill system docs: `C:\Users\davei\.claude\projects\superceo\`

---

## Rules

- No code until plan exists in `C:\Users\davei\.claude\plans\` — run `writing-plans` first
- `_index.md` must be updated before touching any file
- No package installs without Dave approval
- Do not modify anything outside `C:\Users\davei\.claude\projects\jarvis\`
