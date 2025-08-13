def seed(memory: dict) -> dict:
	memory = dict(memory or {})
	memory.setdefault("entered", True)
	return memory

