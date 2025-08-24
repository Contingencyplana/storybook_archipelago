import os

BASE = os.path.join("a0_0_sailing_mode", "a1_2_echoing_grotto_minigame")

def test_no_duplicate_indices_in_echoing_grotto():
    if not os.path.exists(BASE):
        return
    indices = {}
    for name in os.listdir(BASE):
        path = os.path.join(BASE, name)
        if not os.path.isdir(path):
            continue
        if name.startswith("a") and "_" in name:
            idx = "_".join(name.split("_")[:2])  # e.g. "a0_0"
            indices.setdefault(idx, []).append(name)
    offenders = {idx: names for idx, names in indices.items() if len(names) > 1}
    assert not offenders, f"Duplicate node folders found in Echoing Grotto: {offenders}"
