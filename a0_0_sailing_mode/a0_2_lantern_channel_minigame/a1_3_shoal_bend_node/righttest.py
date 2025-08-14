from . import rightmain

def test_right_marker_and_portal_hint():
    out = rightmain.handle_right({})
    assert "[RIGHT]" in out
    assert "[PORTAL:" in out
