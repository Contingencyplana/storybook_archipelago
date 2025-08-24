from . import rightmain

def test_right_run():
    out = rightmain.run({})
    assert "Stillness Depth" in out
