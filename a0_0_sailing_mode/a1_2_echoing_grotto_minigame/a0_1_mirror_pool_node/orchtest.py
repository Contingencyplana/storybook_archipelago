import pytest
from orchestration import orchestrate

def test_orchestrate_returns_string():
    memory = {}
    result = orchestrate(memory)
    assert isinstance(result, str)
    assert "orchestrate" in result.lower()
