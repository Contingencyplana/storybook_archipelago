# orchtest.py — Gate of Echoes Node
from .orchestration import orchestrate

def test_orchestrate():
    memory = {"visited": False}
    assert orchestrate(memory) == memory
