
# integration.py — Mirror Pool
from .leftmain import handle_left
from .rightmain import handle_right

def run_routes(state: dict, path: str = "default") -> str:
    p = (path or "default").lower()
    if p == "left":
        return handle_left(state)
    if p == "right":
        return handle_right(state)
    return "Mirror Pool [default]"
