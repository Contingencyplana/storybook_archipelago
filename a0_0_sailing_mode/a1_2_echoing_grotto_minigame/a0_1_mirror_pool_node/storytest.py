# storytest.py — tests story branching for mirror pool node


from a0_0_sailing_mode.a1_2_echoing_grotto_minigame.a0_1_mirror_pool_node.story import describe_scene
from .test_memory import DummyMemory
from conftest import assert_valid_locale

def test_describe_scene_contains_grove():
    memory = DummyMemory()
    output = describe_scene(memory)
    assert_valid_locale(output)
    assert "[PORTAL:" not in output
