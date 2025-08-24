from . import leftmain

def test_left_run():
    out = leftmain.run({})
    assert "Ripple Path" in out
