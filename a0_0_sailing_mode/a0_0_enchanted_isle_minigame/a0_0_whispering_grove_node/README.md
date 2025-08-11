# 🌿 README.md
**Node Overview – a0_0_whispering_grove_node**

> _“The whisper that welcomes.”_

This file defines the identity, purpose, camouflage intent, and narrative tone of the first node in `a0_0_enchanted_isle_minigame`.

---

## 🧩 Node Identity

- **Name:** `a0_0_whispering_grove_node`
- **Working Title:** The whisper that welcomes
- **Subtype:** Type 1 – Basic L and R, no list logic
- **Role:** First interaction point for the player
- **Purpose:** Gently introduce recursion, tone, and poetic branching

---

## 🌀 Narrative Tone

- **Mood:** Hushed, ambient, expectant
- **Imagery:** Trees that lean in, fog that responds, silence that feels aware
- **Style:** Short L/R poetic options with equal weight, no list involved

---

## 🎭 Camouflage Theme

- **Primary:** Fog (visual recursion mask)
- **Secondary:** Silence (auditory suggestion of presence)
- **Trigger:** Camouflage may shift slightly after repeated loops or waiting

---

## 🔁 Memory Behavior

- First entry sets a seed for memory reflection in `a0_2_reflecting_pool_node`
- Memory may store whether the player hesitated, pressed L/R, or looped

---

## 🚪 Output

- Both `L` and `R` lead to `a0_1_drifting_glade_node`
- Tone, state, or camouflage layer may shift subtly based on direction

---

## 🧩 Implementation Notes

- Narrative surface lives in `story.py` as `describe_scene(memory) -> str`.
- Handlers return strings: `leftmain.handle_left(memory)` includes `[LEFT]`; `rightmain.handle_right(memory)` includes `[RIGHT]`.
- See [`docs/return_value_contract_v1.md`](../../../docs/return_value_contract_v1.md).
- `describe_scene(memory)` must include “grove” and must **not** contain `[PORTAL:`.

---

## ⛑️ Safety Notes

- This node should **not** include numbered list logic
- No deep recursion or redirects
- No state dependencies from previous nodes

> _“You are not being tested. You are being heard.”_
