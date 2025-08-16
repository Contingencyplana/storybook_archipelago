from . import camouflage

def test_camouflage_overlay():
	base = "A test string."
	result = camouflage.overlay_mood(base, {})
	assert "shimmer" in result.lower()
