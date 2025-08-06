# 🧠 integration.py
# Routes input to the appropriate logic handler (L, R, or story)

from . import leftmain, rightmain, story

def route_input(user_input: str, memory: dict) -> str:
    """
    Routes the user input ('L' or 'R') to the correct handler.
    Returns the resulting output string (narrative or signal).
    """
    user_input = user_input.strip().upper()

    if user_input == "L":
        return leftmain.handle_left(memory)
    elif user_input == "R":
        return rightmain.handle_right(memory)
    else:
        return story.describe_scene(memory)
