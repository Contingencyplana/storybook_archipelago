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

## 🧱 Planned Node Structure

This minigame will contain four gameplay nodes, built as one poetic stanza.  
They follow a gentle narrative arc from contact → contrast → reflection → exit.

| Node Folder                     | Working Title                     | Purpose |
|--------------------------------|-----------------------------------|---------|
| `a0_0_whispering_grove_node/`  | "The whisper that welcomes"       | Entry / initiation |
| `a0_1_drifting_glade_node/`    | "The grove that offers two paths" | Tone choice |
| `a0_2_reflecting_pool_node/`   | "The pool that remembers you"     | Memory echo |
| `a0_3_rippling_exit_node/`     | "The exit that forgets forward"   | Transition to next island |

Final node names may evolve slightly as camouflage layers emerge.

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
