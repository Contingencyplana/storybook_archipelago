from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node import integration


def orchestrate(user_input: str, memory: dict) -> str:
	"""
	Minimal orchestration: could set/adjust memory, then delegate to integration.
	Must return strings only.
	"""
	memory.setdefault("entered_whispering_grove", True)
	return integration.route_input(user_input, memory)
