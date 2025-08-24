"""
Story Layer — Reflection Shore Node

Narrative content and optional observations.
"""

from . import camouflage

def observe(state: dict) -> str:
    return (
        camouflage.describe_scene()
        + " Seashells dot the edge. You feel both beginning and echo."
    )
