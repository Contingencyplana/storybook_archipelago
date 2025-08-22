##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_0_bazaar_gate_node/lefttest.py
# ----------------------------------------------------------------------
# Left Test Layer — Bazaar Gate Node
#
# Role:
# - Tests left (L) logic for the Bazaar Gate node.
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

