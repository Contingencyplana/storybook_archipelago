from . import story


def test_story_contains_grove_and_no_portal_tag():
	s = story.describe_scene({})
	assert isinstance(s, str)
	assert "grove" in s.lower()
	assert "[PORTAL:" not in s

