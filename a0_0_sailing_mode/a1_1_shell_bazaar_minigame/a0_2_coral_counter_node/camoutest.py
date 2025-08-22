"""
camoutest.py | Storybook Archipelago node camouflage test
Tests camouflage.py overlays/mood effects. Presentation only; logic unchanged.
See test_strategy.md and camouflage_layers.md for doctrine.
"""


from . import camouflage

def test_camouflage_overlay():
	base = "A test string."
	result = camouflage.overlay_mood(base, {})
	assert "coral glow" in result.lower()
