from . import story

def test_story_contract():
    out = story.describe_scene({})
    assert "grove" in out.lower()
    assert "[PORTAL:" not in out
