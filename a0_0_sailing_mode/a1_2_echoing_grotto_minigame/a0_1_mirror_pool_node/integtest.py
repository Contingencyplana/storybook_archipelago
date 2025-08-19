
# integtest.py — tests input routing logic for mirror pool node
from .integration import run_routes

def test_run_routes():
    assert "[left]" in run_routes({}, "left").lower()
    assert "[right]" in run_routes({}, "right").lower()
    assert "pool" in run_routes({}, "").lower()

