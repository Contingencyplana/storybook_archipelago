from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_2_sunlit_shore_node.orchestration import update_memory


def test_update_memory_sets_value():
    mem = {}
    out = update_memory(mem, "zone", "shore")
    assert out["zone"] == "shore"
