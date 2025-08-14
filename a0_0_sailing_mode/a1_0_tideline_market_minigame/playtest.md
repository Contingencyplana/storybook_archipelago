# Playtest — tideline_market (Tier‑1)

Quick checks for this minigame’s Tier‑1 slices. Uses the dev playtester; it doesn’t follow portals.

## Quick start (CLI)

- From repo root:
  - Preview pages (non-interactive):
    - python scripts/playtest_node.py --preview a0_0_sailing_mode.a1_0_tideline_market_minigame.a0_0_shell_stalls_node
  - Interactive:
    - python scripts/playtest_node.py a0_0_sailing_mode.a1_0_tideline_market_minigame.a0_0_shell_stalls_node

## Controls (playtester)

- Input [L/R/Enter] — case-insensitive; Enter shows the scene (look/recap).
- Numbers preview list items only; they are not interactive here.
- Pages are labeled "[LEFT PAGE]" / "[RIGHT PAGE]" in preview.
- Ctrl+C exits the tool.

## What to look for

- Left/Right return strings containing "[LEFT]" / "[RIGHT]".
- Scene (Enter) returns a string that mentions the locale (e.g., “grove”, “market”, or “channel”) and contains no portal tags.

## Notes

- No navigation is performed by this tool; use portalmaps for end-to-end flows.
