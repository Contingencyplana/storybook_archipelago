"""
Orchestration — Stillness Depth Node
"""

from . import camouflage

def fallback(choice: str, state: dict) -> str:
    return f"Unknown choice '{choice}'. You settle back into the quiet. {camouflage.describe_scene()}"
