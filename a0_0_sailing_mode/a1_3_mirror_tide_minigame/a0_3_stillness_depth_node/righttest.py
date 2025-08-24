from . import rightmain

def test_right_run():
    out = rightmain.run({})
    assert "remain" in out.lower() or "stillness depth" in out
