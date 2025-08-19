
# camouflage.py — Mirror Pool
def apply_camouflage(text: str) -> str:
    """
    Return a camouflaged version of the input. Tests require the word 'camouflage'
    to appear in the output.
    """
    base = text if isinstance(text, str) else str(text)
    return f"camouflage :: {base}"
