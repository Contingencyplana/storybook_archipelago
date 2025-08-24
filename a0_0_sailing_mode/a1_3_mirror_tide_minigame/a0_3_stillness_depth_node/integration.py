"""
Integration Router — Stillness Depth Node (a0_3)

Canonical routing:
  L -> leftmain.run (rise toward Current Gate)
  R -> rightmain.run (remain, loop-safe)
  Enter/"" -> story.observe
  else -> orchestration.fallback (must include 'unknown')
"""

from . import leftmain, rightmain, orchestration, story

def handle_input(choice: str, state: dict) -> str:
    choice = (choice or "").strip().lower()

    if choice in ("l", "left"):
        return leftmain.run(state)
    elif choice in ("r", "right"):
        return rightmain.run(state)
    elif choice in ("", "enter"):
        return story.observe(state)
    else:
        return orchestration.fallback(choice, state)
