# camoutest.py — Whispering Arch
from .camouflage import render_camouflage

def test_render_camouflage_returns_string():
	out = render_camouflage({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_render_camouflage_with_level():
	out = render_camouflage({}, level=2)
	assert "[level=2]" in out.lower()

# Mood keyword and variant tests
def test_render_camouflage_contains_keyword():
	out = render_camouflage({})
	assert isinstance(out, str)
	assert "camouflage" in out.lower()

def test_render_camouflage_mood_variants():
	out_echo = render_camouflage({}, mood="echoing")
	out_muted = render_camouflage({}, mood="muted")
	assert "[mood=echoing]" in out_echo.lower()
	assert "[mood=muted]" in out_muted.lower()

