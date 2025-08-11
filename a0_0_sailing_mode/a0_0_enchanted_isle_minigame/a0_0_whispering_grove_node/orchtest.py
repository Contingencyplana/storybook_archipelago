from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node.orchestration import orchestrate


def test_orchestrate_left_right_story():
	out_l = orchestrate("L", {})
	out_r = orchestrate("R", {})
	out_z = orchestrate("Z", {})
	assert isinstance(out_l, str) and "[LEFT]" in out_l
	assert isinstance(out_r, str) and "[RIGHT]" in out_r
	assert isinstance(out_z, str) and "grove" in out_z.lower() and "[PORTAL:" not in out_z
