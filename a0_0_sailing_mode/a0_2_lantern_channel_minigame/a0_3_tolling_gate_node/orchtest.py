from . import orchestration

def test_seed_sets_entered():
    m = orchestration.seed({})
    assert m.get("entered") is True
