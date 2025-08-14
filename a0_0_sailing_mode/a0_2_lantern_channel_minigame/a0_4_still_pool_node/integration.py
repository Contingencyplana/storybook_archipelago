from . import leftmain, rightmain, story


def route_input(user_input: str, memory: dict) -> str:
	s = (user_input or "").strip().lower()
	if s == "l":
		return leftmain.handle_left(memory)
	if s == "r":
		return rightmain.handle_right(memory)
	return story.describe_scene(memory)

