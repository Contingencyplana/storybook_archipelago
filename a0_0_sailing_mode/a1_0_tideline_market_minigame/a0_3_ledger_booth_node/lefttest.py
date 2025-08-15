from . import leftmain

def test_left_marker_present():
    out = leftmain.handle_left({})
    assert isinstance(out, str)
    assert "[LEFT]" in out
