
from .leftmain import handle_left
from .rightmain import handle_right
from .story import describe_scene

def route_input(user_input, memory):
	"""Routes input to left, right, or story handler."""
	if user_input.strip().upper() == "L":
		return handle_left(memory)
	elif user_input.strip().upper() == "R":
		return handle_right(memory)
	else:
		return describe_scene(memory)
