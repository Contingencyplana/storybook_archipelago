# integration.py — Whispering Arch
def integrate(state: dict, path: str = "default") -> str:
	"""First-pass integration router for Whispering Arch."""
	tag = f"[{path.upper() if path else 'DEFAULT'}]"
	if (path or "").lower() == "left":
		return f"Whispering Arch {tag} — the arch leans toward hushed echoes"
	if (path or "").lower() == "right":
		return f"Whispering Arch {tag} — the arch carries answering whispers"
	return f"Whispering Arch [DEFAULT] — the arch holds its breath"

