from . import camouflage

def test_scene_description():
    out = camouflage.describe_scene()
    assert "shoreline" in out.lower()
    assert "mirrors" in out.lower()
