from . import leftmain
from . import rightmain
from . import story

def route_input(user_input: str, memory: dict) -> str:
    s = (user_input or "").strip().lower()
    if s == "l":
        return leftmain.handle_left(memory)
    if s == "r":
        return rightmain.handle_right(memory)
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
