
# lefttest.py — a0_2_weighing_scales_node
# Tests for left path logic.

from .leftmain import handle_left

def test_left_returns_left_marker():
	output = handle_left()
	assert isinstance(output, str)
	assert "[LEFT]" in output
