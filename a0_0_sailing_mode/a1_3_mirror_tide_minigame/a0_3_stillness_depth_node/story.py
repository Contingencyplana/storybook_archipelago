"""
Story Layer — Stillness Depth Node
"""

from . import camouflage

def observe(state: dict) -> str:
    return (
        camouflage.describe_scene()
        + " Breathing slows; the world narrows to pressure, pulse, and a soft drift."
    )
