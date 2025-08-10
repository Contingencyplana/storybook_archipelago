<!-- Save to: storybook_archipelago/tier_3_minigame_node_structure.md -->

# 🟥 Tier 3 Minigame Node Structure

This file defines the **Tier 3 node** structure used in *Storybook Archipelago*.  
These nodes are intentionally minimal — poetic fragments, atmospheric events, narrative echoes.  
They are non-blocking, non-recursive, and self-contained.

Tier 3 nodes consist of **exactly 4 files**, and **must never hold memory or state**.

---

## 🧾 Overview

🟥 FINAL STRUCTURE — 4 Files, Minimal, Ephemeral, Poetic

Each Tier 3 node must include:

```plaintext
storybook_archipelago/
├── world_layer/
│   └── region_minigame/
│       └── poetic_fragment_node/
│           ├── __init__.py            # Python module marker
│           ├── README.md              # tier: 3, purpose, ephemeral: true (optional)
│           ├── story.py               # The entire visible experience
│           └── leftrightmain.py       # Handles both L and R routing
```

---

## 📖 Story File

- `story.py` is the entire node’s visible surface.
- It may present a stanza, dream fragment, ambient message, hallucination, or world echo.
- No logic is required beyond narrative delivery.
- Players must **never be stuck** in a Tier 3 node — all options must route out safely.

---

## 🔁 Logic File

- `leftrightmain.py` defines the outbound routes for both **Left (L)** and **Right (R)** inputs.
- Logic must be **self-contained**, **non-branching**, and **non-looping** — no recursion, memory, or state checks.
- This file should **not reference** orchestration, camouflage, or persistent state layers.
- Output paths may point to **Tier 2** or **Tier 1** nodes to create poetic contrast or reveal deeper recursion.
- If L and R are identical in outcome, this may be made explicit to reinforce dream-logic or hauntological tone.

> Tier 3 logic exists to **move the player gently onward** — not to trap, challenge, or confuse.

Handlers must return strings; do not emit JSON. Markers are optional in Tier 3.

---

## 📘 README File

Each Tier 3 node must contain:

- `tier` tag: `tier: 3`
- A brief one-sentence description
- An optional `ephemeral: true` flag (if it may be deleted post-usage)

**Example:**

```markdown
tier: 3  
ephemeral: true  
This node contains a dream fragment triggered after the player fails to remember something important.
```

## ⚠️ Tier 3 Limitations

| Feature          | Included? | Notes                                  |
|------------------|-----------|----------------------------------------|
| Memory support   | ❌        | No state or orchestration permitted    |
| Testing          | ❌        | Not required                           |
| Camouflage       | ❌        | No visual/mood overlays                |
| Recursion        | ❌        | May not gate or trigger recursion      |
| Blocking logic   | ❌        | Must always allow exit                 |

---

## 🔄 Evolution Rules

Tier 3 nodes may evolve **only under specific conditions**:

| Condition                            | Upgrade           |
|--------------------------------------|-------------------|
| Node becomes a traversal gate        | 🔺 Tier 1         |
| Node becomes narratively remembered  | 🔺 Tier 2         |
| Node becomes unused or vestigial     | 🔻 Delete/Archive |

Use AI tools like `psychiatrist_mode/` to monitor poetic drift and lifecycle status.

---

## 🧬 Design Philosophy

> A Tier 3 node **haunts**, but does not remain.  
> It says something, and then it fades.  
> It is not recursion — but the echo recursion left behind.

Tier 3 is your tool for **ghosts**, **glimpses**, **flickers**, and **forgotten threads**.  
It is gameplay without weight — **light enough to vanish**, **strong enough to be remembered**.
