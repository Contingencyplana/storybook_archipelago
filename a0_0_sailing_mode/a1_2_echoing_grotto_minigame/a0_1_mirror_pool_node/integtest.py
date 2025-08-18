# integtest.py — tests input routing logic for mirror pool node

from .integration import run

def test_run_routes():
    assert "[left]" in run("left", {})
    assert "[right]" in run("right", {})
    assert "pool" in run("", {})

