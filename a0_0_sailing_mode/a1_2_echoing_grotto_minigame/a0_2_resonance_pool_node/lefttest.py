# lefttest.py — Resonance Pool Node
from .leftmain import handle_left

def test_left():
    assert "touch the ring" in handle_left({}).lower()
