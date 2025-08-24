# tests/guard_echoing_grotto_duplicates.py
"""
Guardrail: Ensure Echoing Grotto stanza has only one node per index.
This prevents ghost/duplicate folders like:
  a0_0_gate_of_echoes_node
  a0_0_resonant_chamber_node
coexisting in the same stanza.
"""

import os
import re

TARGET_PREFIX = os.path.join("a0_0_sailing_mode", "a1_2_echoing_grotto_minigame")

def test_no_duplicate_node_indices_in_echoing_grotto():
    if not os.path.isdir(TARGET_PREFIX):
        return  # Nothing to check if the minigame doesn't exist

    dirs = [
        d for d in os.listdir(TARGET_PREFIX)
        if os.path.isdir(os.path.join(TARGET_PREFIX, d))
    ]

    # Group by stanza prefix (e.g. a0_0, a0_1, a0_2, a0_3)
    groups = {}
    for d in dirs:
        m = re.match(r"^(a\d+_\d+)_", d)
        if not m:
            continue
        prefix = m.group(1)
        groups.setdefault(prefix, []).append(d)

    offenders = {k: v for k, v in groups.items() if len(v) > 1}

    assert not offenders, (
        "Duplicate node indices detected in Echoing Grotto:\n" +
        "\n".join(f"  {k}: {', '.join(v)}" for k, v in offenders.items())
    )
