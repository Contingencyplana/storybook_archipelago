##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_2_coral_counter_node/rightmain.py
# ----------------------------------------------------------------------
# Right Logic Layer — Coral Counter Node
#
# Role:
# - Handles right (R) input logic for the Coral Counter node.
#
# Purpose:
# - Returns the right path output string.
# - Used by integration and test layers for contract validation.
#
# Expected functions:
# - handle_right(memory)
# ------
def handle_right(memory: dict) -> str:
	return "You rearrange the corals, right to left. [RIGHT] The pattern dissolves and reforms."
