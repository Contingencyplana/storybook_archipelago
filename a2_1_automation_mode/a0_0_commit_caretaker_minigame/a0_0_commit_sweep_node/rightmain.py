def handle_right(memory: dict) -> str:
    # Speed/guard improvements (narrative surface only here)
    steps = (
        "You fit the tools to the task. [RIGHT]\n"
        "- Non-interactive flows only\n"
        "- Cancel anything over 15s\n"
        "- Keep tests under a breath"
    )
    return steps
