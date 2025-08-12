from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_1_drifting_glade_node.orchestration import update_memory


def test_update_memory_sets_value():
    mem = {}
    out = update_memory(mem, "zone", "glade")
    assert out["zone"] == "glade"
