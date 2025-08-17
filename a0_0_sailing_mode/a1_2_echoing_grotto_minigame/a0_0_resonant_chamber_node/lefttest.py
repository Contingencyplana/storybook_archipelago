# lefttest.py — tests left path logic for resonant chamber node

import pytest
from .leftmain import handle_left
from .test_memory import DummyMemory

def test_handle_left_returns_left_marker():
    memory = DummyMemory()
    output = handle_left(memory)
    assert "[LEFT]" in output
    assert "chamber" in output.lower()
