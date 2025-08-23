def handle_input(user_input: str, memory: dict) -> str:
    return "[RIGHT] placeholder"

# Alias for backward compatibility with tests
def handle_right(memory: dict) -> str:
    return handle_input("R", memory)
