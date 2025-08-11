from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node.story import describe_scene


def test_story_contains_grove_no_portal():
	out = describe_scene({})
	assert isinstance(out, str)
	assert "grove" in out.lower()
	assert "[PORTAL:" not in out
