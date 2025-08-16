from . import leftmain

def test_left_marker():
	assert "[LEFT]" in leftmain.handle_left({})
