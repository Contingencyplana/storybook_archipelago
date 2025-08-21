
from . import story
from conftest import assert_valid_locale

def test_story_contract():
	s = story.describe_scene({})
	assert_valid_locale(s)
	assert "[PORTAL:" not in s

