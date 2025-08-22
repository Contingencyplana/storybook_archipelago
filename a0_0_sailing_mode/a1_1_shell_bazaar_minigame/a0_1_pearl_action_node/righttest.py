##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_1_pearl_action_node/righttest.py
# ----------------------------------------------------------------------
# Right Test Layer — Pearl Action Node
#
# Role:
# - Tests right (R) logic for the Pearl Action node.
#
# Purpose:
# - Asserts right output contains the [RIGHT] marker.
#
# Expected functions:
# - test_right_marker()
# ------
from . import rightmain

def test_right_marker():
	assert "[RIGHT]" in rightmain.handle_right({})
