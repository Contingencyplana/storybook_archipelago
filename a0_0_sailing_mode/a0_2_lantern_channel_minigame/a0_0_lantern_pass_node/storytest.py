from . import story

def test_story_contract():
    s = story.describe_scene({})
    assert ("grove" in s.lower()) or ("channel" in s.lower())
    assert "[PORTAL:" not in s
