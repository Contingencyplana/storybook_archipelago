import pytest
from . import integration

def test_left_choice():
    out = integration.handle_input("l", {})
    assert "Ripple Path" in out

def test_right_choice():
    out = integration.handle_input("r", {})
    assert "reflection" in out.lower()

def test_observe_choice():
    out = integration.handle_input("", {})
    assert "shore" in out.lower()

def test_fallback_choice():
    out = integration.handle_input("x", {})
    assert "unknown" in out.lower()
