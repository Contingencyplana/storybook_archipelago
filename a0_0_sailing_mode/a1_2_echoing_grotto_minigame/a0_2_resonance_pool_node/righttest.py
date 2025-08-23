# righttest.py — Resonance Pool Node
from .rightmain import handle_right

def test_right():
    assert "scatter the surface" in handle_right({}).lower()
