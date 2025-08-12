# 🧠 integration.py — a0_2_sunlit_shore_node
from . import leftmain, rightmain, story

def route_input(user_input: str, memory: dict) -> str:
    user_input = user_input.strip().upper()
    if user_input == "L":
        return leftmain.handle_left(memory)
    elif user_input == "R":
        return rightmain.handle_right(memory)
    else:
        return story.describe_scene(memory)
