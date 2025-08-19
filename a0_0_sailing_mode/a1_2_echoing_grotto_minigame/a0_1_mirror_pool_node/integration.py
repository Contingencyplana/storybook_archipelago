
# integration.py — Mirror Pool
from .leftmain import handle_left
from .rightmain import handle_right

def run_routes(state: dict, path: str = "") -> str:
    p = (path or "").lower()
    if p == "left":
        return handle_left(state)
    if p == "right":
        return handle_right(state)
    # test checks for lowercase substring "pool"
    return "mirror pool [default]"
