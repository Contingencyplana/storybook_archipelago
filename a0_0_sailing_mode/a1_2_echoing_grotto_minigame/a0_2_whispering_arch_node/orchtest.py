# orchtest.py — Whispering Arch
from .orchestration import orchestrate

def test_orchestrate_default_is_string():
	out = orchestrate({})
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

def test_orchestrate_left_and_right():
	assert "[left]" in orchestrate({}, "left").lower()
	assert "[right]" in orchestrate({}, "right").lower()

# Robust orchestration tests
def test_orchestrate_tolerates_extra_state_keys():
	out = orchestrate({"junk": 1, "meta": {"noise": True}}, "left")
	assert isinstance(out, str)
	assert "[left]" in out.lower()

def test_orchestrate_unknown_path_is_string():
	out = orchestrate({}, "some-new-branch")
	assert isinstance(out, str)
	assert "whispering arch" in out.lower()

