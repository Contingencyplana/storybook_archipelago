#!/usr/bin/env python3
"""
Tiny CLI to playtest a node's integration.route_input() loop with L/R or list numbers.

Usage examples:
  python tools/play_node.py a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_0_whispering_grove_node/ --loop
  python tools/play_node.py a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/ -i L R L

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

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_integration(node_rel_path: str):
    node_path = (REPO_ROOT / node_rel_path).resolve()
    integ_file = node_path / "integration.py"
    if not integ_file.exists():
        raise FileNotFoundError(f"integration.py not found at: {integ_file}")
    spec = importlib.util.spec_from_file_location("node_integration", str(integ_file))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load spec for {integ_file}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    if not hasattr(module, "route_input"):
        raise AttributeError("integration.route_input(user_input, memory) not found")
    return module


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Playtest a node by sending inputs to integration.route_input")
    parser.add_argument("node", help="Four-part relative path starting at repo root, e.g. a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_0_whispering_grove_node/")
    parser.add_argument("-i", "--inputs", nargs="*", default=None, help="Sequence of inputs to send (e.g., L R 1). If omitted with --loop, interactive mode starts.")
    parser.add_argument("--loop", action="store_true", help="Interactive loop: type inputs repeatedly until Ctrl+C.")
    args = parser.parse_args(argv)

    # Normalize node path
    node_rel = args.node.strip("/") + "/"

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
