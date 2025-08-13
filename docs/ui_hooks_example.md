# [markers.py](http://_vscodecontentref_/0)
import re

LEFT = re.compile(r"\[LEFT\]")
RIGHT = re.compile(r"\[RIGHT\]")
PORTAL = re.compile(r"\[PORTAL:")

def strip_markers(text: str) -> str:
    if not text:
        return ""
    return LEFT.sub("", RIGHT.sub("", text))

def detect_direction(text: str) -> dict:
    return {
        "left": bool(LEFT.search(text)),
        "right": bool(RIGHT.search(text)),
    }

def has_portal_tag(text: str) -> bool:
    return bool(PORTAL.search(text))
