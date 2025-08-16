def seed_memory_on_entry(memory: dict) -> dict:
	if "pearl_auction_visited" not in memory:
		memory = dict(memory)
		memory["pearl_auction_visited"] = True
	return memory
