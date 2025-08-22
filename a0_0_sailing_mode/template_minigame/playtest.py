"""
playtest.py — automated smoke test for {{minigame_name}}

Purpose:
    - Traverse all nodes in sequence (a0_0 → a0_3 by default).
    - Ensure story, left, and right handlers respond without crashing.
    - Catch broken imports, missing functions, or portalmap regressions early.

Usage:
    pytest -q playtest.py
"""

import importlib
import pytest

# Define the node order for this minigame.
# Update if nodes are added/removed.
NODE_PATHS = [
    "a0_0_node",
    "a0_1_node",
    "a0_2_node",
    "a0_3_node",
]

@pytest.mark.parametrize("node", NODE_PATHS)
def test_node_story_loads(node):
    """Every node should load story.py and return a scene string."""
    mod = importlib.import_module(f".{node}.story", package=__package__)
    out = mod.describe_scene({})
    assert isinstance(out, str)
    assert out.strip() != ""

@pytest.mark.parametrize("node", NODE_PATHS)
@pytest.mark.parametrize("side", ["leftmain", "rightmain"])
def test_node_lr_loads(node, side):
    """Each node should load leftmain/rightmain and return a non-empty result."""
    mod = importlib.import_module(f".{node}.{side}", package=__package__)
    func = getattr(mod, "handle_input")
    out = func("test", {})
    assert out is not None
