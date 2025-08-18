# Orchestrates route selection and returns a narrative string.

from .story import describe_scene
from .leftmain import handle_left
from .rightmain import handle_right

def orchestrate(memory: dict | None = None, route: str | None = None) -> str:
    memory = memory or {}
    route = (route or memory.get("route") or "").strip().lower()

    if route in ("l", "left"):
        memory["route"] = "left"
        return handle_left(memory)

    if route in ("r", "right"):
        memory["route"] = "right"
        return handle_right(memory)

    # Default landing text
    memory["route"] = "neutral"
    return describe_scene(memory)
