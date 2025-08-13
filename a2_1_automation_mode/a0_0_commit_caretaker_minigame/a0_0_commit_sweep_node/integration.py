from . import story, leftmain, rightmain

def route_input(user_input: str, memory: dict) -> str:
    if user_input == "L":
        return leftmain.handle_left(memory)
    if user_input == "R":
        return rightmain.handle_right(memory)
    # default to scene description
    return story.describe_scene(memory)
