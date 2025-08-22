##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_3_nautilous_nook_node/righttest.py
# ----------------------------------------------------------------------
# Right Test Layer — Nautilous Nook Node
#
# Role:
# - Tests right (R) logic for the Nautilous Nook node.
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
