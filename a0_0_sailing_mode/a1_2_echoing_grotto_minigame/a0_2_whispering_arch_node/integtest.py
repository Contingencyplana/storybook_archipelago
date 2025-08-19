# integtest.py — Whispering Arch
from .integration import integrate

def test_integrate_default_is_string():
	out = integrate({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_integrate_left_and_right():
	assert "[left]" in integrate({}, "left").lower()
	assert "[right]" in integrate({}, "right").lower()

