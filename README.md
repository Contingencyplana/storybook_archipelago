<!-- Save to: storybook_archipelago/README.md -->

# 🏝️ Storybook Archipelago – Multiplayer Game Framework

**Storybook Archipelago** is a poetic, recursive multiplayer video game.  
It is both a world and a builder of worlds — a modular platform where gameplay, story structure, and system logic intertwine through a network of branching narrative nodes.  
This project canonizes the playable expression of *Storybook* (game maker), *FUN Factory* (its test), and *Primordial Soup* (its recursive origin), all within a unified, immersive game experience.

---

## 1. 🌊 Project Overview

At its core, **Storybook Archipelago** is a recursive exploration game.  
Players traverse islands, story fragments, and logic layers, guided by poetic decision-making and modular AI-driven orchestration.  
Every interaction — left, right, list, or loop — echoes into future modes, creating a living world shaped by narrative recursion and system design.

---

## 2. 🧱 Layer Structure

| Layer | Suffix       | Description                              |
|-------|--------------|------------------------------------------|
| 1     | `_mode/`     | Game modes (e.g. `sailing_mode/`)        |
| 2     | `_minigame/` | Bundled content arcs within a mode       |
| 3     | `_node/`     | Individual interactive scenes or choices |

Each layer nests into the next, forming a recursive stanza of traversal and gameplay.

---

## 3. 🎭 Dual Structure per Node

Each `_node/` (Layer 3) has two complementary components:

- **`story.py`** – Defines the poetic stanza, list entries, L/R logic, and player-facing narrative.
- **`leftmain.py` / `rightmain.py`** – Handle gameplay logic, branching, and recursive orchestration.

Use the `story.py` API; the narrative surface is `describe_scene(memory)`.

Additional helpers (e.g., `camouflage.py`, `orchestration.py`) may appear in advanced nodes.

> In Tier‑1 (capability) nodes, **story.py** exposes the player‑facing narrative via `describe_scene(memory)`.

---

## 4. 🗺️ Canonical Game Mode Directory

| Pos   | Folder                 | Type         | Description                                     |
|-------|------------------------|--------------|-------------------------------------------------|
| a0_0  | `sailing_mode/`        | Poetic       | 🚢 Entry point to gameplay; ocean traversal     |
| a0_1  | `isle_mode/`           | Poetic       | 🏝️ Local exploration and scene routing          |
| a0_2  | `dreaming_mode/`       | Poetic       | 🌀 Memory tone and recursion seeding            |
| a0_3  | `high_command_mode/`   | System       | 🎛️ Global orchestration and strain regulation   |
| a1_0  | `memory_mode/`         | System       | 🧠 Loop memory keeper and timeline navigator    |
| a1_1  | `filename_mode/`       | System       | 🔖 Canonical naming and indexing logic          |
| a1_2  | `camouflage_mode/`     | System       | 🎭 Narrative, textual, and visual concealment   |
| a1_3  | `narrative_mode/`      | System       | 📖 Story structure, branching, and pacing       |
| a2_0  | `visualizer_mode/`     | Hybrid       | 🗺️ Debug overlays, maps, and recursive views    |
| a2_1  | `automation_mode/`     | System       | 🧰 Recursive builder and compiler pipelines     |
| a2_2  | `codex_builder_mode/`  | System       | 📘 Generates taskmaps, nodestanza maps, and docs |
| a2_3  | `psychiatrist_mode/`   | System       | 🧪 Detects recursion errors and breakdowns      |
| a3_0  | `sentinel_mode/`       | System       | 🧱 Canon guardian and access control            |
| a3_1  | `quarantine_mode/`     | System       | 🚨 Recursion anomaly containment                |
| a3_2  | `archivist_mode/`      | System       | 🗂️ Logs, snapshots, and recursion lineage       |
| a3_3  | `testing_mode/`        | Experimental | 🧪 Safe zone for experimental logic             |

---

## 5. 🧬 Development Philosophy

Storybook Archipelago follows several key principles:

- **Recursion as Gameplay** – The game is both recursive in structure and in theme.
- **Tiny Step Doctrine** – Each node performs a singular, traceable action.
- **Dualism of Story and Logic** – `story.py` and the `.py` files are co-equal.
- **L/R Decision Flow** – Every node responds to Left/Right input, with optional numbered lists.
- **Camouflage Layers** – A visual and narrative layer system that filters and remaps perception.

---

See: docs/return_value_contract_v1.md

## 6. 🚀 Getting Started

- Launch development in the safe zone: `a3_3_testing_mode/`
- Start building your first live node in `a0_0_sailing_mode/`
- Use `milestones.md` to track major progress
- Use `camouflage_layers.md` to define layer logic and visibility
- All traversal begins with player input: `L`, `R`, or a number.

Use VS Code tasks ‘Test: repo root (pytest)’ or ‘Test: current node (pytest)’ to run tests.

---

## � Portal conventions

- Paths are four-part and relative: `{workspace}/{mode}/{minigame}/{node}/`.
- Use only the open tag form when hinting in strings: `[PORTAL:` (no closing bracket).
- Workspaces must exist in `workspace_registry.md`.

Example:

`storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/`

See: `portals_and_four_part_paths.md`, `docs/return_value_contract_v1.md`.

---

## �📝 Notes

This file defines the global scope and structure of *Storybook Archipelago*.  
Each mode and minigame may include its own `README.md` or `story.py` as needed.
Welcome to the archipelago.
