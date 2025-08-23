# storytest.py — Whisper Chorus Node
from .story import describe_scene

def test_story():
    output = describe_scene({})
    assert "voices" in output.lower() or "breath" in output.lower()
