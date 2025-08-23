# camoutest.py — Gate of Echoes Node
from .camouflage import apply_camouflage

def test_camouflage():
    assert apply_camouflage({}) == {}
