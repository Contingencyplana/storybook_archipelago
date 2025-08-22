##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_1_pearl_action_node/storytest.py
# ----------------------------------------------------------------------
# Story Test Layer — Pearl Action Node
#
# Role:
# - Tests story contract for the Pearl Action node.
#
# Purpose:
# - Asserts scene output meets locale contract and lacks portal tags.
#
# Expected functions:
# - test_story_contract()
# ------

from . import story
from conftest import assert_valid_locale

def test_story_contract():
	s = story.describe_scene({})
	assert_valid_locale(s)
	assert "[PORTAL:" not in s
