# _index.md — Jarvis

Internal HOD AI agent system. Adapts OpenJarvis for our operational workflow.

## Status
Phase 0 — Planning. No code yet.

---

## What We're Building

| Component | Purpose | Source |
|---|---|---|
| Agent runtime | Run on-demand, scheduled, and continuous agents locally | OpenJarvis core |
| Skills system | Agents discover and invoke tools from a catalog | OpenJarvis skills + HOD skills |
| Scheduling engine | Replace manual Coach/cron with proper agent scheduling | OpenJarvis scheduled agents |
| Desktop GUI | Native app to manage agents, view output | OpenJarvis Tauri frontend |

---

## OpenJarvis Source Map — Real Architecture

Explored 2026-06-24. Source: https://github.com/open-jarvis/OpenJarvis

### Top-Level Repo Structure

| Path | Purpose |
|---|---|
| `/src/openjarvis/` | Core Python package (~83% of codebase) |
| `/frontend/` | TypeScript UI components |
| `/rust/` | Rust extensions (performance-critical, ~9%) |
| `/desktop/src-tauri/` | Native desktop app (Tauri) |
| `/configs/openjarvis/` | TOML preset configs (morning-digest, deep-research, etc.) |
| `/examples/` | Starter configs and tutorials |
| `/tests/` | Test suite |
| `/docs/` | mkdocs documentation |
| `/tools/pearl-reference-oracle/` | Internal tooling |

### Core Python Modules (`/src/openjarvis/`)

| Module | What it does |
|---|---|
| `sdk.py` | Main entry point. `Jarvis` class: `ask()`, `ask_full()`, `ask_stream()`, streaming variants, `list_models()`, `list_engines()`, context manager. `MemoryHandle`: index/search/stats. |
| `_rust_bridge.py` | Python↔Rust FFI layer |
| `agents/` | All agent implementations (see below) |
| `skills/` | Skill catalog, loading, execution (see below) |
| `scheduler/` | `scheduler.py`, `store.py`, `tools.py` — scheduled/continuous agent execution |
| `engine/` | Main execution engine |
| `core/` | Core framework primitives |
| `daemon/` | Background service management (Windows: scheduled-task service) |
| `memory/` | Persistent context, semantic search (FAISS, ColBERT optional) |
| `mcp/` | MCP (Model Context Protocol) integration |
| `channels/` | External integrations: Telegram, Discord, Slack, etc. |
| `connectors/` | External service adapters |
| `cli/` | `jarvis` CLI entry point (`openjarvis.cli:main`) |
| `evals/` | Eval CLI (`openjarvis-eval`) and benchmarking |
| `traces/` | Execution trace logging |
| `learning/` | Trace-based skill optimization |
| `analytics/` | Metrics and telemetry |
| `telemetry/` | Monitoring and observability |
| `security/` | Auth and guardrails |
| `sessions/` | Session management |
| `prompt/` | Prompt engineering utilities |
| `sandbox/` | Isolated execution environments |
| `workflow/` | Workflow definition and execution |
| `recipes/` | Pre-built workflow configurations |
| `templates/` | Reusable prompt/config templates |
| `speech/` | TTS/audio processing (used by morning_digest) |
| `intelligence/` | AI model abstraction layer |
| `operators/` | Task executors |
| `mining/` | Knowledge extraction |
| `a2a/` | Agent-to-agent communication |
| `bench/` | Benchmarking tools |
| `server/` | Web server (REST/WebSocket) |
| `system/` | System-level utilities |
| `tools/` | Utility helpers |

### Agents (`/src/openjarvis/agents/`)

Three execution modes, each with real agent files:

| Mode | Agent file | What it does |
|---|---|---|
| Scheduled | `morning_digest.py` | Daily briefing — email, calendar, news with TTS audio |
| On-demand | `deep_research.py` | Multi-hop research with citations |
| On-demand | `orchestrator.py` | Coordinates other agents |
| On-demand | `native_react.py` | ReAct-style reasoning loop |
| On-demand | `native_openhands.py` | OpenHands integration |
| On-demand | `simple.py` | Lightweight chat |
| On-demand | `opencode.py` | OpenCode agent integration |
| On-demand | `claude_code.py` | Claude Code agent runner |
| Continuous | `monitor_operative.py` | Long-horizon monitoring with memory + compression |
| Continuous | `operative.py` | General continuous agent |
| Support | `proactive_agent.py` | Proactive action triggering |
| Support | `channel_agent.py` | Handles external channel events (Telegram etc.) |
| Support | `manager.py` | Agent lifecycle management |
| Support | `scheduler.py` | Per-agent scheduling logic |
| Support | `executor.py` | Agent execution wrapper |
| Support | `loop_guard.py` | Runaway loop protection |
| Support | `digest_store.py` | Digest state persistence |
| Support | `research_loop.py` | Research iteration logic |
| Support | `rlm.py`, `rlm_repl.py` | Reinforcement Learning from Memory |
| Support | `prompt_loader.py` | Agent prompt loading |
| Templates | `templates/` | Agent configuration templates |
| Hybrid | `hybrid/` | Hybrid agent implementations |

### Skills Module (`/src/openjarvis/skills/`)

| File | Role |
|---|---|
| `types.py` | Base classes and skill interface definition |
| `manager.py` | Skill catalog management — discovery and lifecycle |
| `loader.py` | Loads skills from disk and remote sources |
| `importer.py` | Imports from GitHub repos (agentskills.io spec) |
| `executor.py` | Invokes skills |
| `parser.py` | Parses skill schemas |
| `tool_adapter.py` | Adapts skills as agent tools |
| `tool_translator.py` | Translates between skill formats |
| `index.py` | Skill catalog index |
| `overlay.py` | Skill overrides/customization layer |
| `dependency.py` | Skill dependency resolution |
| `security.py` | Skill security sandboxing |
| `data/` | Built-in skill data |
| `sources/` | Skill source connectors (Hermes ~150 skills, OpenClaw ~13,700) |

---

## Dependency Analysis

### Hard Requirements

| Dependency | Why |
|---|---|
| Python ≥3.10, <3.14 | Runtime (3.10–3.13 supported) |
| Ollama | Local LLM runtime — required for local-first mode |
| uv | Python package manager used by installer |
| Rust toolchain | `_rust_bridge.py` + `/rust/` extension — needed for build, not runtime if pre-built |
| `click` ≥8 | CLI |
| `openai` ≥1.30 | API client (used even in local mode for OpenAI-compatible endpoints) |
| `rich` ≥13 | Terminal output |
| `httpx` ≥0.27 | Async HTTP |
| `websockets` ≥15 | Real-time server/client |
| `tomlkit` ≥0.12 | Config parsing |
| `datasets` ≥4.5 | Training data / eval |
| `ddgs` ≥9.11.4 | DuckDuckGo search |
| `posthog` ≥3.0 | Telemetry (can likely be disabled) |
| `nvidia-ml-py` ≥12 | GPU metrics (optional in practice) |
| `python-telegram-bot` ≥22.6 | Telegram channel support |

### Optional Groups (relevant to HOD)

| Group | Installs | HOD relevance |
|---|---|---|
| `memory` | FAISS, ColBERT, PDF support | Yes — persistent agent memory |
| `server` | Web server / API | Yes — local API for HOD agents |
| `channels` | Telegram, Discord, Slack | Maybe — Telegram for Dave notifications |
| `mlx` / `vllm` | Local inference | Only if GPU/Apple Silicon |
| `desktop` | Tauri bindings | Phase 4 only |

---

## Reusability Assessment

### Directly Reusable (low adaptation cost)
- `sdk.py` — `Jarvis` class is a clean Python API; can wrap HOD agents around it
- `agents/claude_code.py`, `agents/opencode.py` — HOD already uses Claude Code as primary agent
- `skills/` module — agentskills.io spec is compatible with building HOD skill packages
- `scheduler/` — cron + continuous modes match exactly what HOD needs to replace Coach
- `memory/` — persistent memory across agent runs is directly useful
- `mcp/` — HOD already uses MCP (Home Assistant MCP server)
- `channels/` — Telegram integration matches HOD's notification needs

### Needs Adaptation
- `agents/morning_digest.py` — useful template, but HOD digest = business pipeline + cash, not email/news
- `skills/sources/` — Hermes/OpenClaw sources irrelevant; HOD needs its own source pointing at `C:\Users\davei\.claude\skills\`
- `connectors/` — need HOD-specific connectors (HA MCP, QuickBooks, etc.)
- `configs/` — need HOD presets (ceo-daily, job-follow-up, cash-check)

### Tightly Coupled / Risky
- `_rust_bridge.py` — Rust build adds complexity; Windows build chain is non-trivial
- `learning/` + `traces/` — trace-based optimization assumes usage volume HOD won't have initially
- `evals/` — benchmarking infrastructure is overkill for Phase 1
- `posthog` telemetry — phones home by default; review privacy implications
- `nvidia-ml-py` — GPU dependency on a non-GPU dev machine will need to be optional

### Windows Compatibility
- Native Windows supported: PowerShell installer, scheduled-task service for daemon, `.exe`/`.msi` desktop
- WSL2 path also documented — HOD dev machine (Windows 11) can use either
- Rust extension must be compiled or pre-built wheel used — potential friction point
- Recommendation: use WSL2 path for development, native Windows only for final deployment

---

## HOD Context

- Existing skills live in `C:\Users\davei\.claude\skills\` — flat markdown files, manually invoked by Claude Code
- Current workflow is manual Claude Code sessions — Jarvis will automate the recurring parts
- Coach (HA app) handles daily scheduling — Jarvis should replace or augment it
- MCP already in use: Home Assistant MCP server (`ha-mcp@latest` via uvx)

---

## Quick Reference

| To find... | Go to... |
|---|---|
| Pending tasks | `WORKLOG.md` |
| Implementation plan | `C:\Users\davei\.claude\plans\2026-06-24-jarvis-phase0-plan.md` |
| HOD skill definitions | `C:\Users\davei\.claude\skills\` |
| OpenJarvis source | https://github.com/open-jarvis/OpenJarvis |
| OpenJarvis skills spec | https://agentskills.io |
