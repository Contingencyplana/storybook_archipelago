# integration.py — simple input router for the node; returns a string.

from .orchestration import orchestrate

def run(user_text: str | None = None, memory: dict | None = None) -> str:
    t = (user_text or "").strip().lower()
    if t in ("l", "left"):
        return orchestrate(memory, "left")
    if t in ("r", "right"):
        return orchestrate(memory, "right")
    return orchestrate(memory, None)
