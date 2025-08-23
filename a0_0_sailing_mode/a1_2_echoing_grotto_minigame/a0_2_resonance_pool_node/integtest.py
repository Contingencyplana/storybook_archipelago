# integtest.py — Resonance Pool Node
from .integration import route_input

def test_enter():
    assert "ripple" in route_input('', {}).lower() or "pool" in route_input('', {}).lower() or "resonance" in route_input('', {}).lower()

def test_left():
    assert "touch the ring" in route_input('L', {}).lower()

def test_right():
    assert "scatter the surface" in route_input('R', {}).lower()
