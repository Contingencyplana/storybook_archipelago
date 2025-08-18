from .orchestration import orchestrate

def test_orchestrate_default_is_string():
    out = orchestrate({})
    assert isinstance(out, str)
    assert "pool" in out.lower()

def test_orchestrate_left_path():
    out = orchestrate({}, "left")
    assert isinstance(out, str)
    assert "[left]" in out.lower()

def test_orchestrate_right_path():
    out = orchestrate({}, "right")
    assert isinstance(out, str)
    assert "[right]" in out.lower()
