from . import story, leftmain, rightmain

def route_input(user_input: str, memory: dict) -> str:
    user_input = user_input.upper()
    if user_input == "L":
        return leftmain.handle_left(memory)
    if user_input == "R":
        return rightmain.handle_right(memory)
    return story.describe_scene(memory)
