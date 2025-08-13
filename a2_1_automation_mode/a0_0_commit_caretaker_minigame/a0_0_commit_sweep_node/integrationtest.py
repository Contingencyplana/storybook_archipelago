from . import integration

def test_routes_left():
    out = integration.route_input("L", {})
    assert "[LEFT]" in out

def test_routes_right():
    out = integration.route_input("R", {})
    assert "[RIGHT]" in out

def test_routes_other_to_story():
    out = integration.route_input("?", {})
    assert "grove" in out.lower()
    assert "[PORTAL:" not in out
