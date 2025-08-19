import pytest
from .camouflage import apply_camouflage

def test_apply_camouflage_returns_string():
    memory = {}
    result = apply_camouflage("test input", memory)
    assert isinstance(result, str)
    assert "camouflage" in result.lower()
