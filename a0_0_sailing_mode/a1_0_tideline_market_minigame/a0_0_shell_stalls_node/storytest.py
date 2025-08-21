from . import story

def test_story_contract():
    out = story.describe_scene({})
    s = out.lower()
    assert ("market" in s) or ("grove" in s)
    assert "[PORTAL:" not in out
