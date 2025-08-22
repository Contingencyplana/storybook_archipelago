# righttest.py — Crystal Vault Node

# righttest.py — Crystal Vault Node
from .rightmain import handle_right

def test_right_stub():
    assert "[RIGHT]" in handle_right({})

from .rightmain import handle_right
def test_right_response():
    output = handle_right({})
    assert "[RIGHT]" in output
    assert "Fracture splits the crystal" in output
    assert "shard branches away" in output
