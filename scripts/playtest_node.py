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
    - Type L or R then Enter to trigger that page
    - Numbers (e.g., 1, 2, 3) are not interactive in this tool; they preview list items only
    - Ctrl+C to exit

Notes:
  - Handlers/story must return strings. This tool only prints them.
  - This does not follow portals; it just exercises the node contract.
"""
import importlib
import os
import re
import sys

def main():
    # Ensure repo root is on sys.path for top-level package imports when run from scripts/ or root
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    # Parse args: allow optional --once and --preview anywhere
    argv = sys.argv[1:]
    once = False
    preview_only = False
    if "--once" in argv:
        once = True
        argv = [a for a in argv if a != "--once"]
    if "--preview" in argv:
        preview_only = True
        argv = [a for a in argv if a != "--preview"]
    if len(argv) != 1:
        print("Usage: python scripts/playtest_node.py [--once] [--preview] <node_package_path>")
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

    def extract_numbered_list(text: str):
        """Return lines that look like numbered options: supports '1) ', '1. ', or '1- ' prefixes."""
        lines = []
        for line in (text or "").splitlines():
            if re.match(r"^\s*\d+[\)\.\-]\s+", line):
                lines.append(line.strip())
        return lines

    def render_preview():
        # Use a shallow copy of memory to avoid mutating interactive state during preview
        memL = dict(memory)
        memR = dict(memory)
        try:
            left_text = integration.route_input("L", memL)
        except Exception as _e:
            left_text = "[LEFT]"
        try:
            right_text = integration.route_input("R", memR)
        except Exception as _e:
            right_text = "[RIGHT]"
        left_list = extract_numbered_list(left_text) if isinstance(left_text, str) else []
        right_list = extract_numbered_list(right_text) if isinstance(right_text, str) else []
        print("[LEFT PAGE]")
        if left_list:
            for ln in left_list:
                print(ln)
        else:
            print("(illustration)")
        print("[RIGHT PAGE]")
        if right_list:
            for ln in right_list:
                print(ln)
        else:
            print("(illustration)")

    if preview_only:
        render_preview()
        return

    print(f"Playtesting node: {pkg}\nCtrl+C to exit. Type L/R or press Enter for scene.\n")
    try:
        numeric_hint_shown = False
        while True:
            try:
                # Show page preview before prompt
                render_preview()
                user = input("\nInput [L/R/<Enter>]: ").strip()
            except EOFError:
                # Allow non-interactive/piped runs to end cleanly
                print("\n[EOF] Exiting playtest.")
                break
            if not user:
                out = integration.route_input("", memory)
            elif re.fullmatch(r"\d+", user):
                if not numeric_hint_shown:
                    print("\n[Hint] Numeric options preview the page lists but aren't interactive here. Use L or R, or press Enter for the scene.\n")
                    numeric_hint_shown = True
                # Do not invoke the node on number input; continue to next loop
                continue
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
