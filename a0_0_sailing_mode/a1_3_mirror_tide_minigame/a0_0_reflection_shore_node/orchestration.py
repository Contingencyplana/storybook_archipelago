"""
Orchestration — Reflection Shore Node

Manages state flow and fallback when input does not match known actions.
"""

from . import camouflage

def fallback(choice: str, state: dict) -> str:
    return f"Unknown choice '{choice}'. The tide waits. {camouflage.describe_scene()}"
