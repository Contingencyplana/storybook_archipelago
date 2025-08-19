# camoutest.py — Whispering Arch
from .camouflage import render_camouflage

def test_render_camouflage_returns_string():
	out = render_camouflage({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_render_camouflage_with_level():
	out = render_camouflage({}, 2)
	assert "[level=2]" in out.lower()

