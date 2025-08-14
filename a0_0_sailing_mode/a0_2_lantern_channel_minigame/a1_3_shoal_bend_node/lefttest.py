from . import leftmain

def test_left_marker_and_portal_hint():
    out = leftmain.handle_left({})
    assert "[LEFT]" in out
    assert "[PORTAL:" in out
