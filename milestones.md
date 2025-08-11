<!-- Save to: storybook_archipelago/milestones.md -->

# ✅ Milestone Log – Storybook Archipelago

This file tracks major design, development, and recursive breakthroughs across the entire *Storybook Archipelago* project.  
Each entry marks a confirmed structural shift, system emergence, or traversal milestone.  
Use this file to monitor cross-mode growth, recursive integrity, and player readiness.

---

## 🌀 PHASE 0 – Genesis & Framework Lock-In

### ✅ Project Initialization
- 🛠️ Created `storybook_archipelago/` folder and activated `.venv`
- 🛠️ Initialized Git repository and published to GitHub
- 🛠️ Added `.gitignore` (Python, VSC, logs, recursion artifacts)

### ✅ Core Structure Canonized
- 📐 Canonized 16 game modes using stanza layout: `a0_0` to `a3_3`
- 📐 Established naming conventions:
  - `_mode/` → game modes (Layer 1)
  - `_minigame/` → minigames (Layer 2)
  - `_node/` → minigame nodes (Layer 3)

---

## 🗺️ STRUCTURE – Canonical Game Modes

| Pos   | Folder                 | Type         | Description                                     |
|-------|------------------------|--------------|-------------------------------------------------|
| a0_0  | a0_0_sailing_mode/     | Poetic       | 🚢 Entry point to gameplay; ocean traversal     |
| a0_1  | a0_1_isle_mode/        | Poetic       | 🏝️ Local exploration and scene routing          |
| a0_2  | a0_2_dreaming_mode/    | Poetic       | 🌀 Memory tone and recursion seeding            |
| a0_3  | a0_3_high_command_mode/| System       | 🎛️ Global orchestration and strain regulation   |
| a1_0  | a1_0_memory_mode/      | System       | 🧠 Loop memory keeper and timeline navigator    |
| a1_1  | a1_1_filename_mode/    | System       | 🔖 Canonical naming and indexing logic          |
| a1_2  | a1_2_camouflage_mode/  | System       | 🎭 Narrative, textual, and visual concealment   |
| a1_3  | a1_3_narrative_mode/   | System       | 📖 Story structure, branching, and pacing       |
| a2_0  | a2_0_visualizer_mode/  | Hybrid       | 🗺️ Debug overlays, maps, and recursive views    |
| a2_1  | a2_1_automation_mode/  | System       | 🧰 Recursive builder and compiler pipelines     |
| a2_2  | a2_2_codex_builder_mode/| System      | 📘 Generates taskmaps, stanzamaps, and docs     |
| a2_3  | a2_3_psychiatrist_mode/| System       | 🧪 Detects recursion errors and breakdowns      |
| a3_0  | a3_0_sentinel_mode/    | System       | 🧱 Canon guardian and access control            |
| a3_1  | a3_1_quarantine_mode/  | System       | 🚨 Recursion anomaly containment                |
| a3_2  | a3_2_archivist_mode/   | System       | 🗂️ Logs, snapshots, and recursion lineage       |
| a3_3  | a3_3_testing_mode/     | Experimental | 🧪 Safe zone for experimental logic             |

---

## 🔜 Next Milestones

- [x] Add global scaffolding files: `README.md`, `camouflage_layers.md`, and this milestone log
- [ ] Document `a0_0_sailing_mode/` and `a0_1_isle_mode/`
- [x] Begin building first playable minigame node: `whispering_grove_node/`
- [ ] Start `a0_1_drifting_glade_node` (planning shell)

---

## 📝 Notes

- This file tracks **global** milestones across all modes.
- Each game mode and minigame will also maintain its own `milestones.md` file.

---

## Milestone: Overarching Docs & Guardrails — 2025-08-10

**Completed**

- Standardized narrative references to `story.py` and added `describe_scene(memory)` note.
- Added VS Code pytest tasks (`Test: repo root`, `Test: current node`).
- Canonicalized Return Value Contract v1 and added Tier-3 exception for markers.
- Normalized disallowed substring to `[PORTAL:` across docs/tests.
- Renamed registry id to `storybook_core` (+ legacy note).
- Added guardrails:
  - VS Code + CI: disallow the closed-bracket portal tag variant; use `[PORTAL:` only.
  - VS Code + CI: disallow non-string returns in handlers/story (dict/list literals, `json.dumps`)
- Cleaned README duplication and updated registry note to present tense.

**Key commits**

- 322317b, 1f8dea3, 0115ce7, 0e09383, a3694ce, 8ad91b3, 24e738c, d76163e, 288d910, 6523b20, 284a366, 67172a8, baeaf3e, 91d1be8

**Next**

- Audit `a0_0_sailing_mode` for contract compliance and naming consistency.

---

## Milestone: Whispering Grove activated — 2025-08-11

**Completed**

- Activated portals in `a0_0_whispering_grove_node/portalmap.md` (L/R → drifting_glade).
- Node test suite green (integration, left/right, story, camouflage, orchestration).

**Key commits**

- 284a366, 67172a8, baeaf3e, 91d1be8

---
