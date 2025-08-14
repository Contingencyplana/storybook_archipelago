from . import leftmain

def test_left_has_marker():
    out = leftmain.handle_left({})
    assert "[LEFT]" in out
