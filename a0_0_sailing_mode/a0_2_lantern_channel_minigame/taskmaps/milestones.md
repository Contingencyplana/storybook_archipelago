# Milestones — Lantern Channel

Status (Aug 2025)

- Tier‑1 slice established and green for the Lantern Channel loop.
- Tests pass across a1_0–a1_3; ingress retargets in place.

Completed

- Tier‑1 node set implemented with tests:
	- a1_0_still_pool_node, a1_1_open_chop_node, a1_2_crescent_moor_node, a1_3_shoal_bend_node
- Ingress wiring updated:
	- a0_3_tolling_gate_node L → a1_3_shoal_bend_node
	- a0_2_count_of_light_node L → a1_3_shoal_bend_node; R → a1_0_still_pool_node
- Runner ergonomics: tools/play_node.py accepts workspace‑prefixed four‑part paths.
- Docs synced: nodestanza_0.md and nodestanza_1.md created and linked from taskmaps and minigame README.
- VS Code Play/Auto‑follow tasks added for key nodes.

Active (short‑term)

- Optional: add a compact index table to the minigame README (nodes + four‑part paths).
- Optional: CI workflow to run pytest and lints on push/PR.
- Add a tiny non‑interactive smoke test for tools/play_node.py.
- Light story polish without changing contracts.

Next (stanza‑2 expansion)

- Scaffold the next stanza (Tier‑1 minimal slice): create node folder(s) with required files and tests per Tier‑1 pattern.
- Follow the 7‑step workflow (Planning → Integration → Camouflage → Orchestration → Left → Right → Story), linking portals only after tests pass.
- Keep portalmap.md targets as four‑part paths and update only when activated.

Validation gates

- Tests: run “Test: repo root (pytest)”.
- Lints: portal‑tag lint (no closed‑bracket portal tags) and non‑string‑return lint for handlers/story.
- Contracts: handlers return strings with [LEFT]/[RIGHT]; story.describe_scene contains “grove” and no portal tags.

References

- See taskmaps/nodestanza_0.md and taskmaps/nodestanza_1.md for per‑stanza details.
