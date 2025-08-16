def test_smoke_story():
	assert True
# storytest.py — a0_1_barter_lane_node
# Tests for story surface.

from .story import describe_scene

def test_story_surface_contract():
	output = describe_scene()
	assert isinstance(output, str)
	assert "grove" in output.lower()
	assert "[PORTAL:" not in output
