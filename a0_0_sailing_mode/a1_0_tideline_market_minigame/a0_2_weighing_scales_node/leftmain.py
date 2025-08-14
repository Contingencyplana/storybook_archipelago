def handle_left(memory: dict) -> str:
    items = [
        "Weigh the tideglass for a fairer price",
        "Balance shells and stories on even pans",
        "Mark the chalk with each small trade",
    ]
    numbered = "\n".join(f"{i+1}) {it}" for i, it in enumerate(items))
    return f"[LEFT]\n{numbered}"
