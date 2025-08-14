#!/usr/bin/env python3
"""
Tiny CLI to playtest a node's integration.route_input() loop with L/R or list numbers.

Usage examples:
    python tools/play_node.py a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_0_whispering_grove_node --loop
    python tools/play_node.py a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node -i L R L
    # Windows separators also work:
    python tools/play_node.py a0_0_sailing_mode\\a0_0_enchanted_isle_minigame\\a0_0_whispering_grove_node --loop

Contract assumptions:
- Each node exposes integration.route_input(user_input, memory) -> str
- Handlers and story return strings containing markers like [LEFT], [RIGHT].
- The integration module lives at <node_path>/integration.py

Notes:
- This runner keeps a simple in-memory dict for "memory" across inputs.
- It prints output after each input.
- It does not activate or follow portals; it's just for local node I/O.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path
import importlib

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_integration(node_rel_path: str):
    """
    Import the node's integration module using its package path so that
    relative imports inside the node (e.g., `from . import leftmain`) work.
    """
    pkg_path = node_rel_path.strip("/\\")
    # Ensure repo root is on sys.path for package imports
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))

    module_name = pkg_path.replace("/", ".").replace("\\", ".") + ".integration"
    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        # Fallback: helpful diagnostics about missing __init__.py or bad path
        node_path = (REPO_ROOT / pkg_path)
        raise ImportError(
            f"Failed to import '{module_name}'. Ensure each folder has __init__.py and the path is correct.\n"
            f"Tried from repo root: {REPO_ROOT}\n"
            f"Node path: {node_path}\n"
            f"Original error: {e}"
        )

    if not hasattr(module, "route_input"):
        raise AttributeError("integration.route_input(user_input, memory) not found")
    return module


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Playtest a node by sending inputs to integration.route_input")
    parser.add_argument("node", help="Four-part relative path starting at repo root, e.g. a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_0_whispering_grove_node (trailing slash optional; Windows backslashes ok)")
    parser.add_argument("-i", "--inputs", nargs="*", default=None, help="Sequence of inputs to send (e.g., L R 1). If omitted with --loop, interactive mode starts.")
    parser.add_argument("--loop", action="store_true", help="Interactive loop: type inputs repeatedly until Ctrl+C.")
    args = parser.parse_args(argv)

    # Normalize node path: accept forward/back slashes and optional trailing slash
    node_rel = args.node.replace("\\", "/").strip("/")

    # Allow leading workspace folder name (repo basename) in four-part paths,
    # e.g., "storybook_archipelago/a0_0_sailing_mode/..." → "a0_0_sailing_mode/..."
    if node_rel:
        first_seg = node_rel.split("/", 1)[0]
        if first_seg.lower() == REPO_ROOT.name.lower():
            node_rel = node_rel.split("/", 1)[1] if "/" in node_rel else ""

    # If a minigame folder is provided (no integration.py here), pick the first *_node child with integration.py
    candidate_dir = REPO_ROOT / node_rel
    if candidate_dir.is_dir() and not (candidate_dir / "integration.py").exists():
        node_dirs = sorted([p for p in candidate_dir.iterdir() if p.is_dir() and p.name.endswith("_node")])
        for nd in node_dirs:
            if (nd / "integration.py").exists():
                node_rel = str(nd.relative_to(REPO_ROOT)).replace("\\", "/")
                break

    integ = load_integration(node_rel)

    memory: dict = {}

    def do_input(user_input: str):
        out = integ.route_input(user_input, memory)  # type: ignore[attr-defined]
        if not isinstance(out, str):
            raise TypeError("route_input must return a string")
        print(out)

    # One-shot sequence
    if args.inputs:
        for token in args.inputs:
            do_input(token)
        return 0

    # Interactive loop
    if args.loop:
        print("Interactive mode. Enter inputs like L, R, or a number. Ctrl+C to exit.")
        try:
            while True:
                token = input("> ").strip()
                if not token:
                    continue
                do_input(token)
        except KeyboardInterrupt:
            print("\nBye.")
            return 0

    # Default: single describe_scene (empty/other input)
    do_input("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
