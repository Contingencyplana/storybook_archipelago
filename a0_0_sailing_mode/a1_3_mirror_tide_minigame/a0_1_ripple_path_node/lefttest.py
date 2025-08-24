from . import leftmain

def test_left_run():
    out = leftmain.run({})
    assert "Current Gate" in out
