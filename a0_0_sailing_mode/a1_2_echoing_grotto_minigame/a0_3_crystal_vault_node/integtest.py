# integtest.py — Crystal Vault Node

# integtest.py — Crystal Vault Node
from .integration import route_input

def test_integration_stub():
    assert True
from .integration import route_input

def test_route_left():
    output = route_input("L", {})
    assert "[LEFT]" in output
    assert "Resonance deepens" in output

def test_route_right():
    output = route_input("R", {})
    assert "[RIGHT]" in output
    assert "Fracture splits the crystal" in output

def test_route_touch_crystal():
    output = route_input("1", {})
    assert "touch a crystal" in output or "hums faintly" in output

def test_route_listen_echo():
    output = route_input("2", {})
    assert "listen to an echo" in output or "repeats, slightly changed" in output

def test_route_break_shard():
    output = route_input("3", {})
    assert "break a shard" in output or "vault shivers" in output
