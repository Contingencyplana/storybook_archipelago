# helpers.py — Whispering Arch

def tag(path: str) -> str:
    """Normalize a path marker to a bracketed, lowercase tag."""
    return f"[{(path or 'default').lower()}]"
