# Playtest — lantern_channel (Tier‑1)

How to quickly exercise nodes in this minigame during development. Keeps to the string contracts; no portals are followed by this tool.

## Quick start (CLI)

- From repo root:
	- Preview pages (non-interactive):
		- python scripts/playtest_node.py --preview a0_0_sailing_mode.a0_2_lantern_channel_minigame.a0_0_lantern_pass_node
	- Interactive:
		- python scripts/playtest_node.py a0_0_sailing_mode.a0_2_lantern_channel_minigame.a0_0_lantern_pass_node

## Controls (playtester)

- Input [L/R/Enter] — case-insensitive; Enter shows the scene (look/recap).
- Numbers preview list items only; they are not interactive here.
- Pages are labeled in the preview as "[LEFT PAGE]" / "[RIGHT PAGE]".
- Ctrl+C exits the tool.

## What to look for

- Left/Right return strings containing "[LEFT]" / "[RIGHT]".
- Scene (Enter) returns a string that mentions "grove" or "channel" and contains no portal tags.

## Notes

- This tool does not activate navigation; use the node’s portal maps and higher-level runners for end-to-end flows.
