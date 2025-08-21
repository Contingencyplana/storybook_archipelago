from . import story

def test_story_contract():
    s = story.describe_scene({}).lower()
    assert ("market" in s) or ("grove" in s)
    assert "[PORTAL:" not in s
