# integration.py — Crystal Vault Node
from .leftmain import handle_left
from .rightmain import handle_right
def touch_crystal(memory):
    return "You touch a crystal. It hums faintly."

def listen_echo(memory):
    return "You listen to an echo. It repeats, slightly changed."

def break_shard(memory):
    return "You break a shard. The vault shivers."

# integration.py — Crystal Vault Node

def route_input(user_input, memory):
    # TODO: Route L/R/numbered input to handlers
    return "[Crystal Vault integration stub]"
from .leftmain import handle_left
from .rightmain import handle_right

def touch_crystal(memory):
    return "You touch a crystal. It hums faintly."

def listen_echo(memory):
    return "You listen to an echo. It repeats, slightly changed."

def break_shard(memory):
    return "You break a shard. The vault shivers."

def route_input(user_input, memory):
    if isinstance(user_input, str):
        u = user_input.strip().lower()
        if u == "l":
            return handle_left(memory)
        elif u == "r":
            return handle_right(memory)
        elif u == "1":
            return touch_crystal(memory)
        elif u == "2":
            return listen_echo(memory)
        elif u == "3":
            return break_shard(memory)
    return "[Crystal Vault integration: unknown input]"
