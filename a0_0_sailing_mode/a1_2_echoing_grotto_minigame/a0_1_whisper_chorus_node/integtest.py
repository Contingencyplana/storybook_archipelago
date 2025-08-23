# integtest.py — Whisper Chorus Node
from .integration import route_input

def test_enter():
    assert "voices" in route_input('', {}).lower() or "breath" in route_input('', {}).lower()

def test_left():
    assert "join the hush" in route_input('L', {}).lower()

def test_right():
    assert "voice apart" in route_input('R', {}).lower()
