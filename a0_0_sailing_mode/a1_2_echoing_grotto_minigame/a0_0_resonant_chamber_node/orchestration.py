
def mark_first_entry(memory):
	"""Marks the first entry into the node."""
	if not memory.get('entered'):
		memory['entered'] = True
		return "First entry registered."
	return "Already entered."
