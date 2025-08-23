# righttest.py — Gate of Echoes Node
from .rightmain import handle_right

def test_right():
    assert "echo lags" in handle_right({}).lower()
