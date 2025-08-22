# 🗺️ roadmap.md

## Strategic Mode Plan – a0_0_sailing_mode

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

| Minigame Folder                       | Theme                                  |
|---------------------------------------|----------------------------------------|
| `a0_0_enchanted_isle_minigame/`       | Magic, stillness, poetic first contact |
| `a0_1_starfish_harbor_minigame/`      | Harbor cadence, ropes and bells        |
| `a0_2_lantern_channel_minigame/`      | Twilight passage, drifting lanterns    |
| `a0_3_fogbound_sound_minigame/`       | Low-visibility navigation by sound     |

### 🧱 Stanza 1 – Market and Bazaar

| Minigame Folder                        | Theme                                     |
|----------------------------------------|-------------------------------------------|
| `a1_0_tideline_market_minigame/`       | Shoreline market, shells, barter, memory  |
| `a1_1_shell_bazaar_minigame/`          | Spiral stalls, trade, recursion, shimmer  |
| `a1_2_echoing_grotto_minigame/`        | Echoes, grotto passages, incomplete node  |

Planned stanza updates will follow this template in `roadstanza_2.md`, etc.

---

## 🔀 Traversal Rules

- Each minigame ends in a **Left (l)** or **Right (r)** choice that determines which minigame island comes next
- Traversal may be **non-linear**, **loopable**, or **memory-modulated**
- All node-to-node links are documented in each node's `portalmap.md`

---

## 🎭 Camouflage and Mood Progression

Camouflage layers are expected to escalate subtly across this mode.
Anticipated emotional layering:

| Minigame                              | Camouflage Layer                  |
|---------------------------------------|-----------------------------------|
| `a0_0_enchanted_isle_minigame/`       | Fog, stillness, childlike awe     |
| `a0_1_starfish_harbor_minigame/`      | Echo, harbor rhythm               |
| `a0_2_lantern_channel_minigame/`      | Twilight tint, bell/foghorn cues  |
| `a0_3_fogbound_sound_minigame/`       | Silence, echo-location, horn cues |
| `a1_0_tideline_market_minigame/`      | Bustle, shifting sands, barter    |
| `a1_1_shell_bazaar_minigame/`         | Spiral shimmer, recursive calls   |
| `a1_2_echoing_grotto_minigame/`       | Hollow resonance, unfinished tone |

---

## 🧠 Testing Notes

All minigames in this mode must:

- Pass l, r, and Story test coverage (lowercase inputs normalized)
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
