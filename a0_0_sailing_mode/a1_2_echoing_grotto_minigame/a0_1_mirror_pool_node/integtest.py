# integtest.py — tests input routing logic for mirror pool node

from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.integration import route_input
from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.test_memory import DummyMemory

def test_route_input_left():
    memory = DummyMemory()
    output = route_input("L", memory)
    assert "[LEFT]" in output

def test_route_input_right():
    memory = DummyMemory()
    output = route_input("R", memory)
    assert "[RIGHT]" in output

def test_route_input_story():
    memory = DummyMemory()
    output = route_input("something else", memory)
    assert "pool" in output.lower() or "mirror" in output.lower()
