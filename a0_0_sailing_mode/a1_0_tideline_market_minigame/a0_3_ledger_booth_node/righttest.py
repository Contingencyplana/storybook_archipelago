from . import rightmain

def test_right_marker_present(): out = rightmain.handle_right({}) assert isinstance(out, str) assert "[RIGHT]" in out
