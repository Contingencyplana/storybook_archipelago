from . import story

def test_story_mentions_locale_and_no_portal():
    s = story.describe_scene({})
    assert "grove" in s.lower() or "market" in s.lower()
    assert "[PORTAL:" not in s
