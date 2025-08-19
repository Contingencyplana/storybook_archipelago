# orchtest.py — Whispering Arch
from .orchestration import orchestrate

def test_orchestrate_default_is_string():
	out = orchestrate({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_orchestrate_left_and_right():
	assert "[left]" in orchestrate({}, "left").lower()
	assert "[right]" in orchestrate({}, "right").lower()

