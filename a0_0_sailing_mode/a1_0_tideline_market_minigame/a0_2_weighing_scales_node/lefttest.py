import re
from . import leftmain

def test_left_includes_marker_and_numbered_list():
    out = leftmain.handle_left({})
    assert "[LEFT]" in out
    assert re.search(r"\n1\) ", out)
