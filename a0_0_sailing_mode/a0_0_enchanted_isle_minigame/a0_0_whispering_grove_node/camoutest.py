from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node.camouflage import apply_camouflage


def test_camouflage_returns_string():
	out = apply_camouflage({})
	assert isinstance(out, str)
	assert "[PORTAL:" not in out
