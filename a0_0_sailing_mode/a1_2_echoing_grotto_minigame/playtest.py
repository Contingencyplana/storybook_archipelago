
# Playtest script for Echoing Grotto Minigame (manual node chaining)
from a0_0_gate_of_echoes_node import integration as gate
from a0_1_whisper_chorus_node import integration as whisper
from a0_2_resonance_pool_node import integration as resonance
from a0_3_crystal_vault_node import integration as vault

def run_playtest():
    nodes = [
        ("Gate of Echoes", gate),
        ("Whisper Chorus", whisper),
        ("Resonance Pool", resonance),
        ("Crystal Vault", vault),
    ]
    print("\nEchoing Grotto Minigame Playtest")
    print("---------------------------------")
    while True:
        print("\nChoose a node to play:")
        for i, (name, _) in enumerate(nodes, 1):
            print(f"  {i}. {name}")
        print("  q. Quit")
        choice = input("Select 1-4 or q: ").strip().lower()
        if choice == "q":
            print("Exiting playtest.")
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(nodes):
                print(f"\n--- {nodes[idx][0]} ---")
                # Each node's integration.py has a __main__ loop; simulate that here
                memory = {}
                try:
                    while True:
                        user_input = input("Press L, R, Enter, or (if available) 1/2/3: ")
                        output = nodes[idx][1].route_input(user_input, memory)
                        print(output)
                except (KeyboardInterrupt, EOFError):
                    print("\nReturning to node menu.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    try:
        run_playtest()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting playtest.")
