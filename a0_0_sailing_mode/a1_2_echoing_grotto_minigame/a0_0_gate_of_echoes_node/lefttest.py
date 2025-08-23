# lefttest.py — Gate of Echoes Node
from .leftmain import handle_left

def test_left():
    assert "lean into the echo" in handle_left({}).lower()
