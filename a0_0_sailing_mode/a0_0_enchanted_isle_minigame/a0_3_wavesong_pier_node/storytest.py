from a0_0_sailing_mode.a0_0_enchanted_isle_minigame.a0_3_wavesong_pier_node.story import describe_scene


def test_story_includes_grove_and_no_portal():
    out = describe_scene({})
    assert isinstance(out, str)
    assert "grove" in out.lower()
    assert "[PORTAL:" not in out
