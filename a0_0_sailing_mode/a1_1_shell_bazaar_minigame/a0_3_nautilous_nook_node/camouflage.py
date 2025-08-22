"""
camouflage.py | Storybook Archipelago node camouflage layer
Presentation-only: overlays mood/effects, does not change logic or routing.
Do not rewrite narrative or logic here. See camouflage_layers.md for doctrine.
"""

def overlay_mood(text: str, memory: dict) -> str:
	# Adds a subtle spiral shimmer effect to the output, without changing logic
	return text + "\nA spiral shimmer glints along the shell’s edge."
