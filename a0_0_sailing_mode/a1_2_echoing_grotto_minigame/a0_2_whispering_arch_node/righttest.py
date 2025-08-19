# righttest.py — Whispering Arch
from .rightmain import handle_right

def test_handle_right_returns_string():
	out = handle_right({})
	assert isinstance(out, str)
	assert "right" in out.lower()

