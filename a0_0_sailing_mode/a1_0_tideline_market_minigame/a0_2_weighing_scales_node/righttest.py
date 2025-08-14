from . import rightmain

def test_right_includes_marker():
    out = rightmain.handle_right({})
    assert "[RIGHT]" in out
