from rightmain import handle_right


def test_right_has_marker():
	out = handle_right({})
	assert isinstance(out, str)
	assert "[RIGHT]" in out
