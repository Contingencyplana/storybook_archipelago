# a1_1_open_chop_node — Lantern Channel

Status: Active (Tier‑1)

Behavior

- L: heads toward crescent_moor — includes a [PORTAL:] hint
- R: heads toward still_pool — includes a [PORTAL:] hint

Portals (four‑part paths)

- L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_2_crescent_moor_node/
- R → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_0_still_pool_node/

Files & tests

- Logic: integration.py, leftmain.py, rightmain.py, story.py, camouflage.py, orchestration.py
- Tests: integtest.py, lefttest.py, righttest.py, storytest.py, camoutest.py, orchtest.py
- Maps/Docs: portalmap.md, subtaskmap.md, README.md

Contract

- Handlers return strings with markers: [LEFT]/[RIGHT]
- story.describe_scene returns a string (no [PORTAL:) and mentions grove/channel/pool
