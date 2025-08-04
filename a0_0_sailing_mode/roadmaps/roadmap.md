# 🗺️ roadmap.md  
**Strategic Mode Plan – a0_0_sailing_mode**

> _“The map is not a path. It is a possibility.”_

This roadmap defines the intended recursive flow of gameplay within the `a0_0_sailing_mode` game mode.  
It outlines the order, thematic arc, and function of each minigame, as well as key traversal logic between them.

---

## 🎮 Mode Overview

**Mode Name:** `a0_0_sailing_mode`  
**Player Role:** Wandering sailor of stories  
**Traversal Mechanic:** Sailing from island to island using L/R poetic decisions  
**Primary Focus:** Introduce recursion, player memory, tone layering, and delight

---

## 🧩 Planned Stanza Structure

### 🧱 Stanza 0 – Opening the Archipelago  
This stanza introduces the recursive rhythm of the game: explore → choose → reflect.

| Minigame Folder                       | Theme                                 |
|--------------------------------------|---------------------------------------|
| `a0_0_enchanted_isle_minigame/`      | Magic, stillness, poetic first contact |
| `a0_1_isle_mode_minigame/`           | Tone layering, soft contrast          |
| `a0_2_???/`                           | Placeholder – to be revealed          |
| `a0_3_???/`                           | Placeholder – to be revealed          |

Planned stanza updates will follow this template in `roadstanza_1.md`, `roadstanza_2.md`, etc.

---

## 🔀 Traversal Rules

- Each minigame ends in a **Left (L)** or **Right (R)** choice that determines which minigame island comes next
- Traversal may be **non-linear**, **loopable**, or **memory-modulated**
- All node-to-node links are documented in each node's `portalmap.md`

---

## 🎭 Camouflage and Mood Progression

Camouflage layers are expected to escalate subtly across this mode.  
Anticipated emotional layering:

| Minigame                     | Camouflage Layer         |
|------------------------------|---------------------------|
| `a0_0_enchanted_isle_minigame/` | Fog, stillness, childlike awe  |
| `a0_1_isle_mode_minigame/`      | Echo, playfulness             |
| `a0_2_???/`                     | Glitch or recursion mist (tentative) |
| `a0_3_???/`                     | Silence or narrative doubling |

---

## 🧠 Testing Notes

All minigames in this mode must:
- Pass L, R, and Story test coverage
- Validate camouflage trigger behavior
- Conform to integration + orchestration routing
- Provide fun, intuitive choices that reflect memory echoes

Fallbacks (if any) are to be routed through `mirror_decisions/` and marked in `subtaskmap.md`.

---

## 🧬 Meta-Recursive Purpose

`sailing_mode/` serves as the **onboarding recursion**:
- It teaches without tutorializing
- It reveals recursive structure through storytelling
- It invites the player to loop, choose, and wonder

This roadmap will evolve as more islands and layers are revealed.

---

> _“The wind may choose the path, but you choose the wind.”_
