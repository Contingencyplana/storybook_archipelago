# a1_3_shoal_bend_node — Lantern Channel

Status: Active (Tier‑1)

Behavior

- L: skirts the shoal — includes a [PORTAL: hint
- R: tests the inner bend — includes a [PORTAL: hint

Portals (four‑part paths)

- L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_0_still_pool_node/
- R → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_2_crescent_moor_node/

Files & tests

- Logic: integration.py, leftmain.py, rightmain.py, story.py, camouflage.py, orchestration.py
- Tests: integtest.py, lefttest.py, righttest.py, storytest.py, camoutest.py, orchtest.py
- Maps/Docs: portalmap.md, subtaskmap.md, README.md

Contract

- Handlers return strings and include markers: [LEFT]/[RIGHT]
- Story must include the word "grove" (or “channel”/"pool") and must not include any [PORTAL: tags
