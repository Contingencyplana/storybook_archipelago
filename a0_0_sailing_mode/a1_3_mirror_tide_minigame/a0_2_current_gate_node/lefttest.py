from . import leftmain

def test_left_run():
    out = leftmain.run({})
    assert "Stillness Depth" in out
