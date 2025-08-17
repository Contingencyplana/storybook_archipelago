
from .orchestration import mark_first_entry
from .test_memory import DummyMemory

def test_first_entry_marks_memory():
	memory = DummyMemory()
	result = mark_first_entry(memory)
	assert result == "First entry registered."
	assert memory['entered'] is True

def test_second_entry_detects_existing():
	memory = DummyMemory({'entered': True})
	result = mark_first_entry(memory)
	assert result == "Already entered."
