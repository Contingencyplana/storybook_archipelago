from . import integration

def test_left_choice():
    out = integration.handle_input("l", {})
    assert "Current Gate" in out

def test_right_choice():
    out = integration.handle_input("r", {})
    assert "remain" in out.lower() or "stillness depth" in out

def test_observe_choice():
    out = integration.handle_input("", {})
    assert "stillness" in out.lower() or "depth" in out.lower()

def test_fallback_choice():
    out = integration.handle_input("x", {})
    assert "unknown" in out.lower()
