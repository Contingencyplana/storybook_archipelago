from . import camouflage

def test_camouflage_passthrough():
    text = "x"
    assert camouflage.apply_mood(text, {}) == text
