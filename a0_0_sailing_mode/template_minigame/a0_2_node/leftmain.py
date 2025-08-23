def handle_input(user_input: str, memory: dict) -> str:
    return "[LEFT] placeholder"

# Alias for backward compatibility with tests
def handle_left(memory: dict) -> str:
    return handle_input("L", memory)
