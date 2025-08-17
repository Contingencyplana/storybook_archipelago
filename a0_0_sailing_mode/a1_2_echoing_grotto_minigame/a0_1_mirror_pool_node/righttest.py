# righttest.py — tests right path logic for mirror pool node

from .rightmain import handle_right
from .test_memory import DummyMemory

def test_handle_right_returns_right_marker():
    memory = DummyMemory()
    output = handle_right(memory)
    assert "[RIGHT]" in output
    assert "pool" in output.lower()
