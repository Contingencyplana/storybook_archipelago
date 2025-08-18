# test_memory.py — dummy memory object for tests

def test_memory_roundtrip():
    from .orchestration import orchestrate
    mem = {}
    _ = orchestrate(mem, "left")
    assert mem.get("route") == "left"
