"""
Story Layer — Current Gate Node
"""

from . import camouflage

def observe(state: dict) -> str:
    return (
        camouflage.describe_scene()
        + " You sense an open hinge below and a pull behind—depth ahead, path behind."
    )
