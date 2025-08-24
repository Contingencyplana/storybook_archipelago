"""
Orchestration — Ripple Path Node
"""

from . import camouflage

def fallback(choice: str, state: dict) -> str:
    return f"Unknown choice '{choice}'. The path shivers. {camouflage.describe_scene()}"
