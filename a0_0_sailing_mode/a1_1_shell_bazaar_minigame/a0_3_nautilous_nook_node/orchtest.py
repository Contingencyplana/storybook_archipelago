from . import orchestration

def test_seed_memory_on_entry():
	mem = {}
	seeded = orchestration.seed_memory_on_entry(mem)
	assert seeded.get("nautilous_nook_visited") is True
