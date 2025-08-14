def seed(memory: dict) -> dict:
    mem = dict(memory or {})
    mem.setdefault("entered", True)
    return mem
