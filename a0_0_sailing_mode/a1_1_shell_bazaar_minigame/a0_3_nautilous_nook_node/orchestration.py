def seed_memory_on_entry(memory: dict) -> dict:
	if "nautilous_nook_visited" not in memory:
		memory = dict(memory)
		memory["nautilous_nook_visited"] = True
	return memory
