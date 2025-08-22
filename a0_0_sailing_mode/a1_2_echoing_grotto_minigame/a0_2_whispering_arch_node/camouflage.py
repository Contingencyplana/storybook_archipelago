"""
camouflage.py | Storybook Archipelago node camouflage layer
Presentation-only: overlays mood/effects, does not change logic or routing.
Do not rewrite narrative or logic here. See camouflage_layers.md for doctrine.
"""

 # camouflage.py — Whispering Arch
def render_camouflage(state: dict | None, mood: str | None = None, level: int = 0) -> str:
	"""Camouflage layer: returns a tone/mood string with optional markers."""
	if mood is None:
		mood_tag = "[mood=neutral]"
	else:
		mood_str = str(mood).lower() if not isinstance(mood, str) else mood.lower()
		mood_tag = f"[mood={mood_str}]"
	return f"Whispering Arch camouflage {mood_tag} [level={level}]"

