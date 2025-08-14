from . import integration

def test_integration_routes():
    left = integration.route_input("L", {})
    right = integration.route_input("R", {})
    scene = integration.route_input("?", {})
    assert "[LEFT]" in left
    assert "1) " in left  # Type-2 numbered list cue on Left
    assert "[RIGHT]" in right
    assert "grove" in scene.lower()
    assert "[PORTAL:" not in scene
