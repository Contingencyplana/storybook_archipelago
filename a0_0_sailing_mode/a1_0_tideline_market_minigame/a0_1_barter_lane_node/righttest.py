from . import rightmain

def test_right_has_marker():
    out = rightmain.handle_right({})
    assert "[RIGHT]" in out
