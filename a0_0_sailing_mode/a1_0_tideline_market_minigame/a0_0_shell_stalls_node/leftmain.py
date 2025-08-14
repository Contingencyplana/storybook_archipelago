def handle_left(memory: dict) -> str:
    # Type-2: Left returns a numbered list cue
    options = [
        "1) Trade a scallop shell for a story",
        "2) Weigh the tideglass for a fairer price",
        "3) Pocket the tiny bell and promise to ring it later",
    ]
    # Join as a simple list; tests look for "1) " marker
    return "[LEFT]\n" + "\n".join(options)
