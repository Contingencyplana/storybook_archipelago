from . import integration

def test_integration_routes():
    assert "[LEFT]" in integration.route_input("L", {})
    assert "[RIGHT]" in integration.route_input("R", {})
    s = integration.route_input("", {})
    assert isinstance(s, str) and s
