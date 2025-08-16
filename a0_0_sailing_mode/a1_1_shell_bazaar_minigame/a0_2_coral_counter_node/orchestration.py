def seed_memory_on_entry(memory: dict) -> dict:
	if "coral_counter_visited" not in memory:
		memory = dict(memory)
		memory["coral_counter_visited"] = True
	return memory
