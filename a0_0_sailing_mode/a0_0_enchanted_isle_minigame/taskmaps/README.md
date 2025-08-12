# 🧭 README.md  
**Minigame Overview – a0_0_enchanted_isle_minigame**

> _“An island that speaks only when the player listens.”_

This file defines the narrative purpose, recursive structure, and gameplay tone of the `a0_0_enchanted_isle_minigame`.  
It is the first minigame within `a0_0_sailing_mode`, and serves as the player’s initial experience of recursion, poetic options, and memory-based navigation.

---

## 🧩 Minigame Identity

**Name:** `a0_0_enchanted_isle_minigame`  
**Stanza Role:** Stanza 0 of `a0_0_sailing_mode`  
**Theme:** Stillness, invitation, quiet wonder  
**Function:** Introduce recursion through soft logic and poetic masking  
**Recursion Type:** Shallow loops, player memory activation, tone ripple

---

## 🧱 Node Structure (Nodestanza 0)

This minigame’s first nodestanza contains four nodes (see `nodestanza_0.md` for canonical paths):

| Node Folder                       | Title                         | Status   |
|-----------------------------------|-------------------------------|----------|
| `a0_0_whispering_grove_node/`     | Whispering Grove              | Complete |
| `a0_1_drifting_glade_node/`       | Drifting Glade                | Complete |
| `a0_2_sunlit_shore_node/`         | Sunlit Shore                  | Complete |
| `a0_3_wavesong_pier_node/`        | Wavesong Pier                 | Complete |

---

## 🎭 Camouflage Layers to Explore

- **Fog** – gentle recursion masking
- **Silence** – sound used to imply presence
- **Mirror** – player memory subtly reflected back
- **Rhythm** – poetic L/R choices with no immediate payoff

---

## 🧪 Testing and Build Flow

This minigame will be built using the 7-step minigame node workflow (see `workflow.md`), with one node completed and tested at a time.

Test coverage must include:

- Integration routing
- Camouflage triggers
- Memory state validation
- L/R logic
- Story presentation and branching

---

## 🔁 Escalation Notes

If recursion fails during node construction (e.g., a logic loop, camouflage breakdown, or test gap):

- Log the event in `subtaskmap.md` of the affected node
- Escalate to `mirror_decisions/` if unrecoverable
- Postpone linking in `portalmap.md` until node passes `orchtest.py`, `camoutest.py`, and `storytest.py`

---

## 🔚 Closing Thought

`a0_0_enchanted_isle_minigame` is the first island.  
It does not explain recursion. It lets the player feel it.  
It is not meant to surprise, but to **invite**.

> _“Every first recursion is a kindness.”_
