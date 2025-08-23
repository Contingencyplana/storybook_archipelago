# storytest.py — Resonance Pool Node
from .story import describe_scene

def test_story():
    output = describe_scene({})
    assert "ripple" in output.lower() or "pool" in output.lower() or "resonance" in output.lower()
