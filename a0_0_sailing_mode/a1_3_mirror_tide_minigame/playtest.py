# Minigame 8 — Mirror Tide: simple manual playtest runner

MENU = """=== Mirror Tide — Playtest ===
Choose a node:
  0) Reflection Shore
  1) Ripple Path
  2) Current Gate
  3) Stillness Depth
  q) Quit
> """.rstrip()

NODE_NAMES = {
    "0": "Reflection Shore",
    "1": "Ripple Path",
    "2": "Current Gate",
    "3": "Stillness Depth",
}

def node_loop(node_key: str):
    name = NODE_NAMES[node_key]
    print(f"\n-- {name} --", flush=True)
    print("Press l (left), r (right), or Enter (blank) to return to menu.\n", flush=True)
    while True:
        try:
            choice = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()  # newline
            return
        if choice == "":
            return
        elif choice == "l":
            print(f"[LEFT] Path through {name.lower()}.", flush=True)
        elif choice == "r":
            print(f"[RIGHT] Path through {name.lower()}.", flush=True)
        else:
            print("Try: l, r, or Enter to return.", flush=True)

def main():
    while True:
        try:
            sel = input(MENU + " ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.", flush=True)
            break
        if sel in ("q", "x"):
            print("Goodbye.", flush=True)
            break
        elif sel in ("0","1","2","3"):
            node_loop(sel)
        else:
            print("Pick 0,1,2,3 or q to quit.\n", flush=True)

if __name__ == "__main__":
    main()
