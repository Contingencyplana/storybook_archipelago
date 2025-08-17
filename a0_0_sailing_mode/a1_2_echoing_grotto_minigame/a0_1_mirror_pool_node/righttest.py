# righttest.py — tests right path logic for mirror pool node

from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.rightmain import handle_right
from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.test_memory import DummyMemory

def test_handle_right_returns_right_marker():
    memory = DummyMemory()
    output = handle_right(memory)
    assert "[RIGHT]" in output
    assert "pool" in output.lower()
