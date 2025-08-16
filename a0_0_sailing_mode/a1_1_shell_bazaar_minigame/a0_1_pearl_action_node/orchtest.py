from . import orchestration

def test_seed_memory_on_entry():
	mem = {}
	seeded = orchestration.seed_memory_on_entry(mem)
	assert seeded.get("pearl_auction_visited") is True
