from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_3_wavesong_pier_node.camouflage import apply_overlay


def test_camouflage_is_pass_through():
    assert apply_overlay("x", {}) == "x"
