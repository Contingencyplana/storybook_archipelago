# righttest.py — Whisper Chorus Node
from .rightmain import handle_right

def test_right():
    assert "voice apart" in handle_right({}).lower()
