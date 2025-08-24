"""
Orchestration — Current Gate Node
"""

from . import camouflage

def fallback(choice: str, state: dict) -> str:
    return f"Unknown choice '{choice}'. The gate holds its pressure. {camouflage.describe_scene()}"
