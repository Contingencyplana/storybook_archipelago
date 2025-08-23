# integration.py — Gate of Echoes Node
from . import story, leftmain, rightmain

def route_input(user_input, memory):
    u = user_input.strip().upper() if isinstance(user_input, str) else ""
    if u == "L":
        return leftmain.handle_left(memory)
    elif u == "R":
        return rightmain.handle_right(memory)
    else:
        return story.describe_scene(memory)

if __name__ == "__main__":
    memory = {}
    print(story.describe_scene(memory))
    try:
        while True:
            user_input = input("Press L, R, or Enter: ")
            print(route_input(user_input, memory))
    except (EOFError, KeyboardInterrupt):
        print("Exiting node.")
