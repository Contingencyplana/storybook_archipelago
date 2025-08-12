from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_2_sunlit_shore_node.rightmain import handle_right


def test_right_has_marker():
    out = handle_right({})
    assert isinstance(out, str)
    assert "[RIGHT]" in out
