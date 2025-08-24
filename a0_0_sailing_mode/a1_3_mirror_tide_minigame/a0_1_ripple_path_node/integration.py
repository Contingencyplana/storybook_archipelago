"""
Integration Router — Ripple Path Node
"""

from . import leftmain, rightmain, orchestration, story

def handle_input(choice: str, state: dict) -> str:
    choice = (choice or "").strip().lower()

    if choice == "l":
        return leftmain.run(state)
    elif choice == "r":
        return rightmain.run(state)
    elif choice in ("", "enter"):
        return story.observe(state)
    else:
        return orchestration.fallback(choice, state)
