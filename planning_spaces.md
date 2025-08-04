# 🧠 planning_spaces.md
Canonical Planning Folder Structures in Storybook Archipelago

This file defines the expected structure of every planning folder used in Storybook Archipelago.  
Planning zones coordinate recursive structure, node development, and anomaly response across gameplay layers.

---

## 1. 🎮 Minigame Planning (`taskmaps/`)

Each `taskmaps/` folder supports one minigame (Tier 2 node) and defines its stanza layout and task progression.

**Required:**
- `__init__.py` — Python module marker
- `milestones.md` — Node completions and progress tracking
- `README.md` — Context, tone, recursion setup
- `stanzamap_0.md` — The first stanza structure
- `taskmap.md` — Core checklist and implementation guide

**Optional:**
- `stanzamap_1.md`, `stanzamap_2.md`, etc. — Additional stanzas

---

## 2. 🗺️ Mode Planning (`roadmaps/`)

Each `roadmaps/` folder supports one gameplay mode (Tier 1) and defines world-level traversal, poetic progression, and minigame orchestration.

**Required:**
- `__init__.py` — Python module marker
- `milestones.md` — Stanza and minigame completion log
- `README.md` — Game mode purpose, design vision, traversal rules
- `roadstanza_0.md` — First stanza of minigames within the mode
- `roadmap.md` — Planning logic, gameplay goals, routing logic

**Optional:**
- `roadstanza_1.md`, etc. — Additional stanzas as the mode grows

---

## 3. 🧬 Recursive Anomaly Planning (`mirror_decisions/`)

This folder activates **only** when a confirmed recursive anomaly is detected — such as logic loops, memory drift, or unreachable nodes.  
It contains anomaly logs, rollback plans, and containment mappings.

**Required:**
- `__init__.py` — Python marker for AI indexing
- `mirror_decision.md` — Canonical anomaly report
- `fallbackmap.md` — Redirect or recovery instructions
- `README.md` — Summary of purpose, severity, and triggers
- `milestones.md` — Tracks recovery progress or intervention success

---

## 4. 🎭 Special Domains (e.g. `playability_ai/`, `memory_ai/`, `camouflage_ai/`)

Specialized planning folders may emerge to support:

- AI routing
- Memory scaffolding
- Story orchestration
- Gameplay transition layers

**Planning structure will be defined per domain.**  
See:  
- `tiny_steps.md`  
- `ai_agents.md`  
- `camouflage_layers.md`  
- Layer-specific gameplay docs

---

## 🔚 Conclusion

All planning folders must be:
- **Explicitly structured**
- **Minimal but sufficient**
- **Recursively navigable**
- **Traceable by AI, test agents, and contributors**

Storybook Archipelago grows through recursion, but it survives through planning.
