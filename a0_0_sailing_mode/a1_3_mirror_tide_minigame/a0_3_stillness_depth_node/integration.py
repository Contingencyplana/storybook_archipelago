"""
Integration Router — Stillness Depth Node
"""

from . import camouflage

def handle_input(user_input: str, state: dict) -> str:
    """Master router for Stillness Depth node."""
    user_input = user_input.strip().lower()

    if user_input in ("l", "left"):
        return "You press left — currents swirl back toward Reflection Shore."
    elif user_input in ("r", "right"):
        return "You press right — a faint ripple path extends outward."
    else:
        # Default observation path
        return observe(state)

def observe(state: dict) -> str:
    """Default observation when no L/R is pressed."""
    return camouflage.describe_scene() + " You realize this is the Stillness Depth."

