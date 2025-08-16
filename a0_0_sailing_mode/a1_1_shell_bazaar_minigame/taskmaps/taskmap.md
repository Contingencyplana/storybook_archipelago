# Taskmap: Shell Bazaar Minigame

## Purpose

Map out the core tasks, flows, and checkpoints for the shell bazaar minigame. Adapted from template_minigame/taskmaps/taskmap.md.

## Core Tasks

- Define the unique mechanics and player actions for each node (stall).
- Establish left/right logic and narrative flavor for each stall.
- Identify key player decisions and their consequences.
- Integrate shell stall theme into all node logic and story.

## Node Breakdown

- a0_0_bazaar_gate_node: Entry portal; sets tone and theme for the bazaar, introduces L/R traversal.
- a0_1_pearl_action_node: Player interacts with a pearl auction, choosing how to bid or observe.
- a0_2_coral_counter_node: Player tallies or exchanges coral tokens, balancing risk and reward.
- a0_3_nautilous_nook_node: Quiet reflection or secret found at the edge of the bazaar; closes the stanza.

## Playtest Checklist

- [x] All node logic and story return strings as per contract.
- [x] L/R logic and story markers present ([LEFT], [RIGHT], "grove" etc.).
- [x] Portalmap and subtaskmap are up to date.
- [x] All tests pass for each node.
- [x] Playtested all nodes interactively (l/r/Enter).

## Notes

- Playtest complete as of August 17, 2025. Ready for polish, overlays, or next stanza.
