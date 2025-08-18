# integration.py — input router for mirror pool node

from .leftmain import handle_left
from .story import describe_scene

def route_input(user_input, memory):
    if user_input == "L":
        return handle_left(memory)
    elif user_input == "R":
        return "[RIGHT] The pool ripples with your reflection."
    else:
        return describe_scene(memory)
