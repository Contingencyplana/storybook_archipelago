# storytest.py — Whispering Arch

from .story import describe_scene
from conftest import assert_valid_locale

def test_describe_scene_contract():
    out = describe_scene({})
    assert isinstance(out, str)
    assert_valid_locale(out)
    assert "[PORTAL:" not in out
