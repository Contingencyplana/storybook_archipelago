# integtest.py — Gate of Echoes Node
from .integration import route_input

def test_enter():
    assert "arch" in route_input('', {}).lower()

def test_left():
    assert "lean into the echo" in route_input('L', {}).lower()

def test_right():
    assert "echo lags" in route_input('R', {}).lower()
