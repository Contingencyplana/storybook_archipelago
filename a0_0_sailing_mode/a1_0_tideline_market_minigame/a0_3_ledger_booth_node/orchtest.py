from . import orchestration
def test_seed_sets_entered(): mem = orchestration.seed({}) assert mem.get("entered") is True
