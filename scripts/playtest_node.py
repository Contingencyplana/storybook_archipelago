#!/usr/bin/env python3
"""
Interactive playtest for a Tier-1 node.
Usage (PowerShell):
    # Interactive
    python scripts/playtest_node.py <node_package_path>

    # Non-interactive: render scene once and exit 0
    python scripts/playtest_node.py --once <node_package_path>

Controls:
  - Press Enter to view the scene (story)
  - Type L or R then Enter to trigger that path
  - Ctrl+C to exit

Notes:
  - Handlers/story must return strings. This tool only prints them.
  - This does not follow portals; it just exercises the node contract.
"""
import importlib
import os
import sys

def main():
    # Ensure repo root is on sys.path for top-level package imports when run from scripts/ or root
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    # Parse args: allow optional --once anywhere
    argv = sys.argv[1:]
    once = False
    if "--once" in argv:
        once = True
        argv = [a for a in argv if a != "--once"]
    if len(argv) != 1:
        print("Usage: python scripts/playtest_node.py [--once] <node_package_path>")
        sys.exit(1)
    pkg = argv[0].rstrip("/")
    try:
        integration = importlib.import_module(pkg + '.integration')
    except Exception as e:
        print(f"Failed to import {pkg}.integration: {e}")
        sys.exit(2)

    memory = {}
    if once:
        out = integration.route_input("", memory)
        if not isinstance(out, str):
            print("[ERROR] Non-string output from node. Aborting.")
            sys.exit(3)
        print(out)
        return
    print(f"Playtesting node: {pkg}\nCtrl+C to exit. Type L/R or press Enter for scene.\n")
    try:
        while True:
            try:
                user = input("Input [L/R/<Enter>]: ").strip()
            except EOFError:
                # Allow non-interactive/piped runs to end cleanly
                print("\n[EOF] Exiting playtest.")
                break
            if not user:
                out = integration.route_input("", memory)
            else:
                out = integration.route_input(user, memory)
            if not isinstance(out, str):
                print("[ERROR] Non-string output from node. Aborting.")
                sys.exit(3)
            print("\n--- OUTPUT ---\n" + out + "\n---------------\n")
    except KeyboardInterrupt:
        print("\nExiting playtest.")

if __name__ == '__main__':
    main()
