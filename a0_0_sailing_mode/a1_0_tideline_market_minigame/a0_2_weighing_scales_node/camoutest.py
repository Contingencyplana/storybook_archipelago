import importlib
camouflage = importlib.import_module(__package__ + '.camouflage')

def test_camouflage_passthrough():
    text = "x"
    assert camouflage.apply_mood(text, {}) == text
