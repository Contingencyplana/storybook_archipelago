from leftmain import handle_left

def test_left_has_marker():
    out = handle_left({})
    assert isinstance(out, str)
    assert "[LEFT]" in out
