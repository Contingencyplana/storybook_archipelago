import os
from pathlib import Path

BASE = Path("a0_0_sailing_mode") / "a1_2_echoing_grotto_minigame"

REQUIRED = {
    "__init__.py",
    "README.md",
    "integration.py",
    "integtest.py",
    "camouflage.py",
    "camoutest.py",
    "orchestration.py",
    "orchtest.py",
    "leftmain.py",
    "lefttest.py",
    "rightmain.py",
    "righttest.py",
    "story.py",
    "storytest.py",
    "portalmap.md",
    "subtaskmap.md",
}

def _node_dirs():
    if not BASE.exists():
        return []
    return [p for p in BASE.iterdir() if p.is_dir() and p.name.startswith(("a0_0_", "a0_1_", "a0_2_"))]

def test_echoing_grotto_nodes_are_canonical_or_absent():
    offenders = []
    for node in _node_dirs():
        files = {p.name for p in node.glob("*") if p.is_file()}
        # Allow a node to be completely absent; but if present, it must be complete.
        if files:
            missing = REQUIRED - files
            # treat empty dir as missing everything
            if missing:
                offenders.append(f"{node} missing: {', '.join(sorted(missing))}")
    assert not offenders, "Echoing Grotto nodes must be 16/16 if present:\n- " + "\n- ".join(offenders)
