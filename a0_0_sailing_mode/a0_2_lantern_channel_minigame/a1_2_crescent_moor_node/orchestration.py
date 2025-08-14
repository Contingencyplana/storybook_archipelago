def seed(memory: dict) -> dict:
    memory = memory or {}
    memory.setdefault("entered", True)
    return memory
