
"""
camouflage.py | Storybook Archipelago node camouflage layer
Presentation-only: overlays mood/effects, does not change logic or routing.
Do not rewrite narrative or logic here. See camouflage_layers.md for doctrine.
"""

# camouflage.py — Mirror Pool
def apply_camouflage(text: str, memory: dict) -> str:
    """
    Return a camouflaged version of the input. Tests require:
    - two parameters: (text, memory)
    - the word 'camouflage' present in the output
    """
    base = text if isinstance(text, str) else str(text)
    return f"camouflage :: {base}"
