
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

if __name__ == "__main__":
    memory = {}
    print("Welcome to Tideline Market. Press Ctrl+C to exit.")
    try:
        while True:
            user_input = input("(press l for left, r for right, or enter to look around.) ")
            output = route_input(user_input, memory)
            print(output)
    except KeyboardInterrupt:
        print("\r\nExiting...")
