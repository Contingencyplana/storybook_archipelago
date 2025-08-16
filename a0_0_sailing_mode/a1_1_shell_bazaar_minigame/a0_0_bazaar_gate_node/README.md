# Template Node — a0_0_node

This is a minimal Tier‑1 node skeleton. Contracts:

- integration.route_input("L"|"R"|other) -> str
- leftmain.handle_left(memory) -> str (includes [LEFT])
- rightmain.handle_right(memory) -> str (includes [RIGHT])
- story.describe_scene(memory) -> str (includes "grove", no [PORTAL:)
- orchestration.seed(memory) -> dict (sets entered=True)
- camouflage.apply_mood(text, memory) -> str (presentation only)

Run local tests via the repo task: Test: current node (pytest).
