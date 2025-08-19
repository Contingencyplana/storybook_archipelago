# test_memory.py — dummy memory object for tests

def test_memory_roundtrip():
    from .orchestration import orchestrate
    mem = {}
    _ = orchestrate(mem, "left")
    assert mem.get("route") == "left"


# Minimal DummyMemory stub for tests
class DummyMemory:
    """Minimal stub used by tests; expand as needed by node logic."""
    def __init__(self, data=None):
        self._data = dict(data or {})

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
