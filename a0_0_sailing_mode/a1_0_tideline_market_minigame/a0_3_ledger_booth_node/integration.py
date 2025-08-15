from . import leftmain
from . import rightmain
from . import story

def route_input(user_input, memory):
    if user_input == "L":
        return leftmain.handle_left(memory)
    elif user_input == "R":
        return rightmain.handle_right(memory)
    else:
        return story.describe_scene(memory)
