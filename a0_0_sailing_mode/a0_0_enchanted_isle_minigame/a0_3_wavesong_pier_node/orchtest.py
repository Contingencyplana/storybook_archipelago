from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_3_wavesong_pier_node.orchestration import update_memory


def test_update_memory_sets_value():
    mem = {}
    out = update_memory(mem, "zone", "pier")
    assert out["zone"] == "pier"
