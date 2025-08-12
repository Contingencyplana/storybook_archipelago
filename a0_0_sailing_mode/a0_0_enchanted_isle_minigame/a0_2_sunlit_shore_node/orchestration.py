# Orchestration layer — memory/state transitions (minimal Tier-1)

def update_memory(memory: dict, key: str, value) -> dict:
    memory = dict(memory or {})
    memory[key] = value
    return memory
