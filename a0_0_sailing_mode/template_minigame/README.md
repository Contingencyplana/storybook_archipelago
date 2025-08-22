
# template_minigame

This is a scaffold for new minigames. Pair this root README (overview) with `taskmaps/README.md` (planning index).

## How to use this template

1. Copy the entire template_minigame folder to your new minigame location and rename appropriately.
2. Rename all node folders and files to match your minigame's theme and node names.
3. Update README.md files for the minigame and each node with theme and description.
4. Fill out taskmaps/taskmap.md with your minigame's specific tasks and checkboxes.
5. Log progress and blockers in taskmaps/milestones.md as you work.
6. Implement logic and test files for each node, following the template contracts.
7. Only activate portals after all tests pass.
8. Keep documentation up to date for future reference.


## Bare Bones Skeletal of Text

This template uses a minimal, text-first scaffold for all nodes, with explicit labels and placeholders for future graphics, sound, and UI. See ../../bare_bones_skeletal_of_text.md for the full philosophy and guidelines.

## Canonical File Placement Rules for Tier-1 Minigame Nodes

**Minigame root may contain:**

- Minigame node folders (`a0_0`, `a0_1`, etc.)
- `taskmaps/` folder
- `__init__.py`
- `README.md`
- `playtest.md`

**Minigame root must not contain files reserved for nodes, including:**

- `portalmap.md`
- `subtaskmap.md`
- `nodestanza_#.md`
- Any of the 16 Tier-1 node files (`integration.py`, `story.py`, `camouflage.py`, `orchestration.py`, `leftmain.py`, `rightmain.py`, `leftrightmain.py`, and all associated `*test.py` files).

All 16 node files must live only inside **node folders**, never in the root of a minigame. This ensures clean separation between minigame-level and node-level logic, documentation, and tests.

Quick links

- taskmaps/README.md — author/planning index
- taskmaps/nodestanza_0.md — initial stanza
- taskmaps/milestones.md — progress ledger
