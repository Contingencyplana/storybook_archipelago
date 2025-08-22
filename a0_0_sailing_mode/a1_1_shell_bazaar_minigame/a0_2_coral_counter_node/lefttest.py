##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_2_coral_counter_node/lefttest.py
# ----------------------------------------------------------------------
# Left Test Layer — Coral Counter Node
#
# Role:
# - Tests left (L) logic for the Coral Counter node.
#
# Purpose:
# - Asserts left output contains the [LEFT] marker.
#
# Expected functions:
# - test_left_marker()
# ------
from . import leftmain

def test_left_marker():
	assert "[LEFT]" in leftmain.handle_left({})
