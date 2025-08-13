from . import camouflage

def test_camouflage_noop():
    out = camouflage.apply_mood("x", {})
    assert isinstance(out, str)
