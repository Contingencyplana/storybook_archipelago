# integration.py — Whispering Arch
from .helpers import tag

def integrate(state: dict | None, path: str = "default") -> str:
	"""Integration router for Whispering Arch node (robust to None/unknown)."""
	p = (path or "default").lower()
	marker = tag(p)
	if p == "left":
		return f"Whispering Arch {marker}"
	if p == "right":
		return f"Whispering Arch {marker}"
	return f"Whispering Arch {marker}"

