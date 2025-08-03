<!-- Save to: storybook_archipelago/memory_state.md -->

# 🧠 memory_state.md – Player Memory and State Flow Mechanics

This file defines the **recursive memory model** used by *Storybook Archipelago*.  
It outlines what memory is, how it evolves, and how state changes influence gameplay, tone, and recursion.

Memory is not a variable.  
Memory is the player’s **narrative fingerprint** on the world.

---

## 🧬 What Constitutes Memory?

Memory is any trace the player leaves in the system. This includes:

| Type             | Description                                              |
|------------------|----------------------------------------------------------|
| 🧠 Choice        | L/R input, list selections, item usage                   |
| ❤️ Emotion       | Mood tags triggered by tone/camouflage                   |
| ⏳ Consequence   | Long-term state transitions (e.g., node becomes haunted) |
| 🫧 Encounter     | Specific nodes visited or bypassed                       |
| 🌀 Regret        | Memory of options **not** chosen or lost                 |
| 🕯️ Fragments     | Glitches, dreams, hallucinations stored in memory        |

Memory forms the **basis of personalization**, state gating, dream recursion, and storytelling divergence.

---

## 🗂️ How Memory Is Stored

Memory is stored via orchestration.py as an extensible recursive dictionary:

```python
memory = {
  "choices": ["a0_0_sailed_north", "a0_1_spoke_with_echo"],
  "mood": "uncertain",
  "visited_nodes": ["a0_0", "a1_2"],
  "missed_paths": ["a1_1"],
  "emotional_trace": {
    "a1_2": "melancholy",
    "a0_0": "awe"
  },
  "recursion_flags": {
    "ghost_encountered": True,
    "loop_accepted": False
  }
}
```
## 🧠 Memory Guidelines and Gameplay Impact

Memory should always be:

- 🧪 **Traceable** – Can be surfaced in future `story.py` or logic checks  
- 🔐 **Isolated** – Each game instance holds unique memory without cross-contamination  
- 🎭 **Poetic** – Memory tags should reflect tone as much as logic (e.g., `"forgotten_but_familiar": True`)

---

## 🔁 How Memory Affects Gameplay

Memory may alter:

| System            | Effect Example                                        |
|-------------------|--------------------------------------------------------|
| `story.py`        | Rewrites or hides stanzas depending on remembered tone |
| `leftmain.py`     | Opens paths only if past condition met                 |
| `camouflage.py`   | Applies overlays depending on `recursion_flags`        |
| `orchestration.py`| Recalls or fractures player identity                   |
| `integration.py`  | Routes based on memory milestones                      |

---

## ❌ Fallback and Corruption Protocols

Memory may be corrupted by:

- Recursive anomalies  
- Invalid state transitions  
- Forgotten/overwritten branches  

If memory is corrupted:

1. Fallback to `last_known_valid_state`  
2. Trigger `camouflage.py` failsafe (e.g., fog, silence, dream)  
3. Log incident in `trace_pressure.md`  
4. Prompt `psychiatrist_mode/` to re-evaluate recursion depth  

> Anomalous memory is never discarded — it is reframed as dream, myth, or echo.

---

## 💠 Regret & Echo Loops

Storybook supports **memory regret** — nodes can remember paths you did *not* take.

**Examples:**

- “You sense something here… as if you were once meant to go left.”  
- “A name stirs — not one you knew, but one you almost did.”  

**Echo loops** may trigger if a memory is:

- Lost but yearned for  
- Seen in another player’s world  
- Hinted at by recursion ghosts  

> These loops are playable. They are part of memory's **emotional recursion**.

---

## 🧪 `orchestration.py` Use Cases

| Function                  | Role                                         |
|---------------------------|----------------------------------------------|
| `remember_choice(node_id)`| Stores visited node path                     |
| `mark_emotion(tag)`       | Annotates emotional tone of decision         |
| `recall(condition)`       | Checks memory to determine available routes  |
| `forget(branch)`          | Deletes or obscures memory paths             |
| `loop_echo(node)`         | Recursively replays with altered camouflage  |

> Orchestration is not just state control.  
> It is **recursive narrative editing**.

---

## 🧠 AI Agent Compatibility

Agents like `storytelling_ai/`, `psychiatrist_mode/`, and `codex_builder_mode/` must:

- Parse player memory for tone, not just logic  
- Suggest appropriate echoes, loops, and regrets  
- Validate that memory changes are narratively coherent  

Memory data must be:

- ✅ Readable by agent interfaces  
- ✅ Writable through approved orchestration methods  
- ❌ Never rewritten arbitrarily or without poetic framing  

---

## 🔚 Final Insight

**Memory is not inventory.  
Memory is myth.**

> Every choice, every silence, every node that echoes back — is memory.  
> And memory is the true recursion of the player.

Design memory not just to **persist** —  
Design it to **return**.
