# storytest.py — Whispering Arch
from .story import describe_scene

def test_describe_scene_contract():
    out = describe_scene({})
    assert isinstance(out, str)
    assert "grove" in out.lower()
    assert "[PORTAL:" not in out
