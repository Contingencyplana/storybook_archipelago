# lefttest.py — Whispering Arch
from .leftmain import handle_left

def test_handle_left_returns_string():
	out = handle_left({})
	assert isinstance(out, str)
	assert "left" in out.lower()

