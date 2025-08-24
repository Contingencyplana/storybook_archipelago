from . import camouflage

def test_scene_description():
    out = camouflage.describe_scene()
    assert "ripples" in out.lower() or "path" in out.lower()
