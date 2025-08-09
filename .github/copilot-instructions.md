# Copilot Instructions for Storybook Archipelago

**Purpose:** Make AI coding agents productive immediately by following our recursive architecture, pathing rules, and 7‑step authoring workflow. Keep outputs tiny, testable, and aligned to node tiers.

## Big Picture
- Repo uses **four-part paths**: `{workspace}/{mode}/{minigame}/{node}/`.
- Content layers (suffixes are canonical):
  - `_mode/` – world/mode level
  - `_minigame/` – content cluster
  - `_node/` – playable scene
- Nodes present **L/R traversal** (Type 1–4 subtypes). Story and logic are co‑equal.
- Tiers define file counts/capabilities (see `node_tiers.md` + tier docs).

## Authoring Workflow (Tiny Steps)
- Follow **7 steps** in `workflow.md`: Planning → Integration → Camouflage → Orchestration → Left → Right → Story.
- Build **one file at a time**; pair each logic file with its test (e.g., `leftmain.py` ↔ `lefttest.py`).
- Minimum viable Tier‑1 slice *before linking*: router routes L/R, ≥1 side test passes, portalmap uses **four-part paths**.

## Naming & Paths (Must Follow)
- Lowercase `snake_case`. Folder suffixes: `_mode/`, `_minigame/`, `_node/`.
- All portals use fully qualified **four‑part relative paths** (no OS‑absolute):
  `storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/`
- Valid workspaces are listed in `workspace_registry.md`. **Reject** links to unknown workspaces.

## Tier‑1 Node Pattern (Example)
- Required files (16 total incl. tests):  
  `README.md`, `portalmap.md`, `subtaskmap.md`,  
  `integration.py` + `integtest.py`,  
  `camouflage.py` + `camoutest.py`,  
  `orchestration.py` + `orchtest.py`,  
  `leftmain.py` + `lefttest.py`,  
  `rightmain.py` + `righttest.py`,  
  `story.py` + `storytest.py`, `__init__.py`.
- Contracts:
  - `integration.py` routes input (`"L"`, `"R"`, other → `story.describe_scene`).
  - `leftmain.py` / `rightmain.py` handle direction-specific logic.
  - `story.py` exposes narrative surface and L/R poetic options.
  - `camouflage.py` overlays mood/effects; **does not** change logic.
  - `orchestration.py` manages memory/state (e.g., first‑entry seed).

## Return‑Value Conventions (for tests)
- Handlers return **strings** (player‑facing text or signals).  
  Tests can `assertIn("left", output.lower())`, etc. Keep outputs stable.

## Testing Expectations
- See `test_strategy.md`. Tier‑1 requires tests for routing, camouflage triggers, memory flow, L/R logic, and story branching.
- Link activation in `portalmap.md` only after `camoutest.py`, `orchtest.py`, `storytest.py` pass.

## Camouflage Doctrine
- Escalate presentation layers if not fun yet (see `camouflage_layers.md`).  
- Do **not** rewrite narrative or routing logic in camouflage.

## Safety & Scope
- No OS‑absolute paths. Use four‑part project paths only.
- For cross‑workspace links, ensure workspace exists in `workspace_registry.md`.
- If a target node is missing, propose it and mark portal as **Pending**.

## Quick Start for a New Tier‑1 Node
1) Create folder with `_node/` suffix + `__init__.py`.  
2) Add `README.md`, `portalmap.md` (four‑part paths), `subtaskmap.md`.  
3) Implement `integration.py` + `integtest.py`.  
4) Implement **one** side (`leftmain.py` + `lefttest.py`) and get tests passing.  
5) Add remaining files step‑by‑step; only link after all tests pass.

_References: `portals_and_four_part_paths.md`, `workflow.md`, `node_tiers.md`, tier structure docs, `workspace_registry.md`, `test_strategy.md`, `camouflage_layers.md`._
