##
# Path: a0_0_sailing_mode/a1_1_shell_bazaar_minigame/a0_3_nautilous_nook_node/integration.py
# ----------------------------------------------------------------------
# Integration Layer — Nautilous Nook Node
#
# Role:
# - Entry point for the Nautilous Nook node in Shell Bazaar minigame.
# - Routes user input (L, R, Enter) to the appropriate logic files.
# - Provides a manual play loop when executed directly.
#
# Expected handlers:
# - story.describe_scene(memory)
# - leftmain.handle_left(memory)
# - rightmain.handle_right(memory)
# ------

from . import story, leftmain, rightmain

def route_input(user_input: str, memory: dict) -> str:
	user_input = (user_input or "").strip().upper()
	if user_input == "L":
		return leftmain.handle_left(memory)
	elif user_input == "R":
		return rightmain.handle_right(memory)
	else:
		return story.describe_scene(memory)

if __name__ == "__main__":
	memory = {}
	print(story.describe_scene(memory))  # show opening scene once
	while True:
		try:
			user_input = input("Press L, R, or Enter: ")
			print(route_input(user_input, memory))
		except (EOFError, KeyboardInterrupt):
			print("\nExiting node.")
			break
