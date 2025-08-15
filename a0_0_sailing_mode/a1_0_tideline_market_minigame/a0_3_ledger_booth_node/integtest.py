from . import integration

def test_routes_left_right_and_scene():
    mem = {}
    assert "[LEFT]" in integration.route_input("L", mem)
    assert "[RIGHT]" in integration.route_input("R", mem)
    scene = integration.route_input("", mem)
    assert isinstance(scene, str) and scene
