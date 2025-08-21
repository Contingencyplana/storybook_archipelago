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
from . import leftmain, rightmain, story
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

def route_input(user_input: str, memory: dict) -> str:
    user_input = (user_input or "").upper()
    if user_input == "L":
        return leftmain.handle_left(memory)
    if user_input == "R":
        return rightmain.handle_right(memory)
    return story.describe_scene(memory)
