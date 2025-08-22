# lefttest.py — Crystal Vault Node

# lefttest.py — Crystal Vault Node
from .leftmain import handle_left

def test_left_stub():
    assert "[LEFT]" in handle_left({})

from .leftmain import handle_left
def test_left_response():
    output = handle_left({})
    assert "[LEFT]" in output
    assert "Resonance deepens" in output
    assert "echoes grow stronger" in output
