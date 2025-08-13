from . import leftmain

def test_left_marker():
    out = leftmain.handle_left({})
    assert "[LEFT]" in out
