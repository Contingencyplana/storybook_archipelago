<!-- Save to: storybook_archipelago/tier_2_minigame_node_structure.md -->

# 🟨 Tier 2 Minigame Node Structure

This file defines the canonical structure of a **Tier 2 minigame node** in *Storybook Archipelago*.  
Tier 2 nodes are lightweight but fully playable — designed for fast traversal, modular generation, and recursive compatibility.

They balance simplicity and function: enough structure for story, logic, and testing, but without full orchestration or camouflage layering.

---

## 🧾 Overview

Tier 2 nodes contain **exactly 8 files**, arranged across a simplified recursive architecture:

```plaintext
storybook_archipelago/
├── some_mode/
│   └── some_minigame/
│       └── some_node/
│           ├── __init__.py            # Python module marker
│           ├── README.md              # 📘 Node description and tier
│           ├── integration.py         # 🧠 Coordinates routing
│           ├── camouflage.py          # 🎭 Basic tone overlays (optional)
│           ├── leftmain.py            # 🔁 Handles L-input logic
│           ├── rightmain.py           # 🔁 Handles R-input logic
│           ├── story.py               # 📖 Narrative content (can be short or symbolic)
│           └── testlogic.py           # ✅ Minimal test coverage
```

## 🧱 Purpose of Tier 2 Nodes

- Serve as fast traversal or side-room content  
- Support **partial recursion**, memory echoes, or list-triggered effects  
- Used for **AI-generated rooms**, **modular systems**, or **experimental logic patterns**

---

## 🧪 Test Requirements

Only **basic validation** is required:

- Confirm `leftmain.py` and `rightmain.py` route correctly  
- Confirm `story.py` options align with input logic  
- Validate that `integration.py` triggers correct transitions  
- Preferred tests: `lefttest.py` / `righttest.py` and, if present, `integtest.py` for the router.

Tier 2 nodes **must be testable**, but do **not** require full recursion edge-case coverage.

---

## 🎭 Camouflage Guidelines

`camouflage.py` may:

- Shift tone (e.g., from hopeful to eerie)  
- Control basic overlays (e.g., fog, silence, glitch)  

❌ No multi-layered or recursive camouflage needed.

---

## 🧠 Integration Logic

`integration.py` may:

- Trigger logic, state, or memory actions  
- Hand off to orchestration if nearby Tier 1 memory exists  
- Redirect output if conditions are met  

> The orchestration layer is **absent** here — so `integration.py` must handle fallback logic directly.

---

## 📘 Metadata Expectations

Every Tier 2 node must include:

- A **tier tag** in `README.md` (e.g., `tier: 2`)  
- A short **description of gameplay purpose**  
- An **AI compatibility note** (if auto-generated)

---

## 🔄 Upgrade / Downgrade Rules

| Direction       | Condition                                            |
|-----------------|------------------------------------------------------|
| Tier 2 → Tier 1 | Node is revisited, remembered, or gains recursion   |
| Tier 2 → Tier 3 | Node loses logic but retains poetic value           |
| Tier 2 → Delete | Node becomes unused and unreachable                 |

Tier 2 nodes are **flexible** — they evolve based on the player's journey.

---

## 🧬 Design Philosophy

> A Tier 2 node **thinks quickly**, **vanishes easily**, and **teaches subtly**.  
> It remembers enough to link logic, but not enough to demand memory.  
> It is the **flicker** between full recursion and poetic ephemera.
