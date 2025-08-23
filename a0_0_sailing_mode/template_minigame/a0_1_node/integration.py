from . import leftmain, rightmain, story

def route_input(user_input: str, memory: dict) -> str:
    user_input = (user_input or "").upper()
    if user_input == "L":
        return leftmain.handle_input(user_input, memory)
    elif user_input == "R":
        return rightmain.handle_input(user_input, memory)
    else:
        return story.describe_scene(memory)
