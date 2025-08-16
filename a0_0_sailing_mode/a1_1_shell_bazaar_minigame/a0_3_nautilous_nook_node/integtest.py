from . import integration, leftmain, rightmain, story

def test_route_left():
	out = integration.route_input("L", {})
	assert "[LEFT]" in out

def test_route_right():
	out = integration.route_input("R", {})
	assert "[RIGHT]" in out

def test_route_story():
	out = integration.route_input("", {})
	assert "grove" in out.lower()
