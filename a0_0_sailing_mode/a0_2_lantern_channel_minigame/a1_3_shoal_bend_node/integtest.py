from . import integration


def test_routing_left_right_and_story():
    out = integration.route_input("L", {})
    assert "[LEFT]" in out
    out = integration.route_input("R", {})
    assert "[RIGHT]" in out
    out = integration.route_input("", {})
    assert isinstance(out, str)
