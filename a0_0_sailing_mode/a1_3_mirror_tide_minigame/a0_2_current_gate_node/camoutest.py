from . import camouflage

def test_scene_description():
    out = camouflage.describe_scene()
    assert "gate" in out.lower() or "current" in out.lower()
