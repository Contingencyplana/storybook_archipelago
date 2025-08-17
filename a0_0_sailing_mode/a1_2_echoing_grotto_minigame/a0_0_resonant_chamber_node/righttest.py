
import pytest
from .rightmain import handle_right
from .test_memory import DummyMemory

def test_handle_right_returns_right_marker():
	memory = DummyMemory()
	output = handle_right(memory)
	assert "[RIGHT]" in output
	assert "chamber" in output.lower()
