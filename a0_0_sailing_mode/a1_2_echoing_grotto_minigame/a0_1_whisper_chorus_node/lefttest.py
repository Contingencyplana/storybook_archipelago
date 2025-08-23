# lefttest.py — Whisper Chorus Node
from .leftmain import handle_left

def test_left():
    assert "join the hush" in handle_left({}).lower()
