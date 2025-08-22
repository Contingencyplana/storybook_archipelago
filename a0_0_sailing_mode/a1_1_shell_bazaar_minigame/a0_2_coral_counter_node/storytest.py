##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_2_coral_counter_node/storytest.py
# ----------------------------------------------------------------------
# Story Test Layer — Coral Counter Node
#
# Role:
# - Tests story contract for the Coral Counter node.
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
