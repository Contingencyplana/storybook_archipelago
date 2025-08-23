# storytest.py — Gate of Echoes Node
from .story import describe_scene

def test_story():
    output = describe_scene({})
    assert "arch" in output.lower() and "echo" in output.lower()
