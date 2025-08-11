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

VS Code tasks (build/test)
We provide two convenient tasks:

Test: repo root (pytest) – runs pytest from the workspace root.

Test: current node (pytest) – runs pytest in the folder of the currently opened file (handy for node‑local test loops).

Portal examples (four‑part paths)
Canonical examples for portalmap.md rows:

L → storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/

R → storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/

Cross‑workspace example:

L → storybook_primordial_soup/a1_0_cell_mode/a0_2_first_membrane_minigame/a0_0_warm_pool_node/

Rules:

Paths must be four‑part: {workspace}/{mode}/{minigame}/{node}/

{workspace} must appear in workspace_registry.md

No OS‑absolute paths

Return value contract (handlers & story) — v1
Purpose: keep tests stable and strings human‑readable.

integration.route_input(user_input, memory) -> str

leftmain.handle_left(memory) -> str

rightmain.handle_right(memory) -> str

story.describe_scene(memory) -> str

String markers (for tests):

Left path MUST include the token "[LEFT]" somewhere in the returned string.

Right path MUST include the token "[RIGHT]".

If a handler wants to indicate a portal choice (even if not followed yet), include a single open portal tag on one line, e.g.:
[PORTAL: storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/

story.describe_scene() MUST include the word "grove" (lowercase ok) and MUST NOT include [PORTAL: tags.

Examples (not prescriptive prose, just shape):

Left: "The fog leans with you. [LEFT] The hush thickens."

Right: "You answer the wind by not answering. [RIGHT] The leaves tilt."

With portal hint (optional):
"You part the boughs. [LEFT]\n[PORTAL: storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/"

Story: "In the whispering grove, the air listens back."

Test hooks:

lefttest.py: assert "[LEFT]" in output

righttest.py: assert "[RIGHT]" in output

storytest.py: assert "grove" in output.lower() and assert "[PORTAL:" not in output

Do NOT switch to JSON payloads. We stay with strings + lightweight markers.
