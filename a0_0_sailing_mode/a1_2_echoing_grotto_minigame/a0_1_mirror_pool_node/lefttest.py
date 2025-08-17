# lefttest.py — tests left path logic for mirror pool node

from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.leftmain import handle_left
from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.test_memory import DummyMemory

def test_handle_left_returns_left_marker():
    memory = DummyMemory()
    output = handle_left(memory)
    assert "[LEFT]" in output
    assert "pool" in output.lower()
