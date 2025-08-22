# storytest.py — Crystal Vault Node

def test_story_surface():
    output = describe_scene({})
    assert "vault" in output.lower()
    assert "[PORTAL:" not in output

from .story import describe_scene
