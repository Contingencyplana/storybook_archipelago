
# righttest.py — a0_2_weighing_scales_node
# Tests for right path logic.

from .rightmain import handle_right

def test_right_returns_right_marker():
	output = handle_right()
	assert isinstance(output, str)
	assert "[RIGHT]" in output
