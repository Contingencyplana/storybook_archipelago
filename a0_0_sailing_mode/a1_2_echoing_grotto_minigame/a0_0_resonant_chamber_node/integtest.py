
from .integration import route_input
from .test_memory import DummyMemory

def test_route_input_left():
	memory = DummyMemory()
	output = route_input("L", memory)
	assert "[LEFT]" in output

def test_route_input_right():
	memory = DummyMemory()
	output = route_input("R", memory)
	assert "[RIGHT]" in output

def test_route_input_story():
	memory = DummyMemory()
	output = route_input("something else", memory)
	assert "grove" in output.lower() or "chamber" in output.lower()
