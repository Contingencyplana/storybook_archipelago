<!-- Save to: storybook_archipelago/worldmap.md -->

# 🗺️ Worldmap – Archipelago-Wide Navigation Matrix

This file defines the **official traversal schema** of the *Storybook Archipelago* multiplayer video game.  
It canonizes the structure of the world — which **modes** exist, how players **navigate** between them, and how gameplay unfolds across the recursive sea.

This map is readable by players, contributors, and AI agents.  
It ensures clarity, traceability, and poetic cohesion across the world.

---

## 🧭 1. Game Modes – Tier 1 Stanza Grid

The world of Storybook Archipelago is built using a **4x4 poetic stanza matrix** of 16 canonical **game modes**, labeled using Tier 1 logic:  
`a0_0` through `a3_3`.

Each mode corresponds to a **region**, **function**, or **meta-role** in the Archipelago.

| ID     | Mode Name               | Role / Theme                          |
|--------|-------------------------|----------------------------------------|
| a0_0   | `sailing_mode/`         | Sea traversal, world linking           |
| a0_1   | `isle_mode/`            | Landfall and island-level gameplay     |
| a0_2   | `dreaming_mode/`        | Memory, subconscious, hallucination    |
| a0_3   | `high_command_mode/`    | Authority, AI oversight, directive     |
| a1_0   | `memory_mode/`          | Memory state management and recall     |
| a1_1   | `filename_mode/`        | File identity, naming, and introspect  |
| a1_2   | `camouflage_mode/`      | Mood layers, perception, disguise      |
| a1_3   | `narrative_mode/`       | Story logic, stanzas, poetic structure |
| a2_0   | `visualizer_mode/`      | Diagrams, graphs, recursion viz        |
| a2_1   | `automation_mode/`      | Builders, compilers, meta-tools        |
| a2_2   | `codex_builder_mode/`   | Documentation, templates, recursive GDD|
| a2_3   | `psychiatrist_mode/`    | Drift control, recursion wellness      |
| a3_0   | `sentinel_mode/`        | Guardian logic, node validators        |
| a3_1   | `quarantine_mode/`      | Anomaly isolation and sandboxing       |
| a3_2   | `archivist_mode/`       | Lore, logs, and recursive canon        |
| a3_3   | `testing_mode/`         | Experimental nodes, dev staging        |

> 🔁 All game logic flows **through** these modes.  
> Every minigame belongs to one — and every node references its stanza origin.

---

## 🏝️ 2. Minigame Mapping – Example Entries

Below are **example minigames** assigned to each game mode. This table expands as new nodes and stanzas are created.

| Mode               | Minigames                         |
|--------------------|-----------------------------------|
| `sailing_mode/`    | `enchanted_isle_minigame/`        |
| `isle_mode/`       | `sunken_chapel_minigame/`         |
| `memory_mode/`     | `forgotten_forest_minigame/`      |
| `camouflage_mode/` | `recursion_fog_minigame/`         |
| `automation_mode/` | `compiler_core_minigame/`         |
| `testing_mode/`    | `sandbox_edgecase_minigame/`      |

Each minigame contains its own internal stanza nodes and follows the **Tier 1–3 node structure**.  
Traversal **between** minigames happens via **portalmap.md** or **cross-mode stanzas**.

---

## 🌊 3. Traversal Rules

Traversal in Storybook Archipelago is **recursive** and **poetic**.

### ⛵ Sea Travel (L/R Logic)

- The player starts in `sailing_mode/` on the open sea
- L and R input lead to new islands or minigames
- The **story.py** and **camouflage.py** disguise these transitions (Tier‑1 story exposes `describe_scene(memory)`)

### 🏝️ Island Landfall

- Each island is a `minigame/` inside `isle_mode/` or another mode
- Minigames are explorable: four nodes (a0_0 to a0_3) per stanza
- Nodes may exit to other islands, sea, memory, or recursion modes

### 🌀 Recursion Travel

- Some logic paths (Tier 1 or advanced Tier 2) allow access to:
  - `dreaming_mode/` — memory echoes, surreal logic
  - `high_command_mode/` — authority decisions, AI intervention
  - `quarantine_mode/` — anomaly branches, lockdowns
  - `sentinel_mode/` — node validation, recursion testing

> 🧠 Mode transitions must **preserve player memory state** unless intentionally wiped.

---

## 🧱 4. Mode Relationships – Layer Logic

The stanza matrix is not flat — it is **layered**:

- **Top Layer** (a0_x): Surface world traversal and landfall
- **Middle Layers** (a1_x and a2_x): Recursive systems, memory, documentation
- **Bottom Layer** (a3_x): Guardians, quarantines, experimental nodes

This verticality maps to gameplay depth:

- Sailing leads to exploration  
- Exploration leads to recursion  
- Recursion leads to understanding  
- Understanding leads to anomaly  
- Anomaly leads to evolution (or collapse)

---

## 🧾 5. Optional Diagram – Stanza Grid Layout

```plaintext
a0_0  a0_1  a0_2  a0_3     ← surface layer
a1_0  a1_1  a1_2  a1_3     ← memory, naming, disguise, story
a2_0  a2_1  a2_2  a2_3     ← tools, automation, codex, recursion wellness
a3_0  a3_1  a3_2  a3_3     ← guardian, quarantine, lore, testing
```

Each row = stanza  
Each column = tone  
Diagonal motion = poetic recursion  

Use this map to guide **new game content**, **AI mode allocation**, and **portal logic**.

---

## 🔚 Conclusion

The world of *Storybook Archipelago* is not flat — it is **recursive terrain**.  
Each **mode** is a **stanza**.  
Each **stanza** contains **minigames**.  
Each **minigame** is a **nested world of nodes**.

Traversal between these modes is guided by:

- **Player input** (L/R and list selection)  
- **Logic and memory conditions**  
- **AI systems and narrative triggers**

This file is your **anchor** — for both **AI agents** and **human contributors**.

> The world is not explored.  
> It is **revealed** — one poetic node at a time.
