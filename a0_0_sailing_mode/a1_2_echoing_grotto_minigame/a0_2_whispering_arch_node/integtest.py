# integtest.py — Whispering Arch
from .integration import integrate

def test_integrate_default_is_string():
	out = integrate({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_integrate_left_and_right():
	assert "[left]" in integrate({}, "left").lower()
	assert "[right]" in integrate({}, "right").lower()

# Edge-case tests
def test_integrate_handles_none_state_and_unknown_path():
	out = integrate(None, "widdershins")  # unknown path
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()  # graceful, no crash

def test_integrate_accepts_case_insensitive_markers():
	assert "[left]" in integrate({}, "LEFT").lower()
	assert "[right]" in integrate({}, "RiGhT").lower()

