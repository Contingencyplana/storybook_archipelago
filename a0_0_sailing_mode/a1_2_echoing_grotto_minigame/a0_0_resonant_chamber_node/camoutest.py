
from .camouflage import overlay_echo_mood

def test_overlay_echo_mood_adds_effect():
	base = "A simple line."
	result = overlay_echo_mood(base)
	assert result.startswith("~Echoes shimmer in the air~")
	assert base in result
