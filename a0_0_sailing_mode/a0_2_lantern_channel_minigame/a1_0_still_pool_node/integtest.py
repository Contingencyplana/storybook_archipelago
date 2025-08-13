from . import integration

def test_integration_routes():
    assert "[LEFT]" in integration.route_input("L", {})
    assert "[RIGHT]" in integration.route_input("R", {})
    scene = integration.route_input("?", {})
    assert "channel" in scene.lower() or "pool" in scene.lower()
    assert "[PORTAL:" not in scene
