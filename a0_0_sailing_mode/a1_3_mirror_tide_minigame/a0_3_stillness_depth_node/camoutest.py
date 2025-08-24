from . import camouflage

def test_scene_description():
    out = camouflage.describe_scene()
    assert "quiet" in out.lower() or "rest" in out.lower() or "depth" in out.lower()
