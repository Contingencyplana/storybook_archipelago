from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_1_drifting_glade_node.integration import route_input


def test_routes_left_and_right_and_story():
    mem = {}
    assert "[LEFT]" in route_input("L", mem)
    assert "[RIGHT]" in route_input("R", mem)
    out = route_input("", mem)
    assert isinstance(out, str)
