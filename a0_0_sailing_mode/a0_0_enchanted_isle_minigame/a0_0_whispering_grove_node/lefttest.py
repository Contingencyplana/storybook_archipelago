from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_0_whispering_grove_node.leftmain import handle_left

def test_left_has_marker():
    out = handle_left({})
    assert isinstance(out, str)
    assert "[LEFT]" in out
