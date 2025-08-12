<!-- Save to: storybook_archipelago/conventions.md -->

# 📏 conventions.md  

Canonical Naming and Structural Conventions – Storybook Archipelago

> _“Consistency is camouflage for complexity.”_  
> This file defines all required naming and structural conventions for the Storybook Archipelago project.  
> These conventions ensure recursive safety, tooling compatibility, contributor clarity, and poetic cohesion across all gameplay layers.
> See also: `names_have_power.md` for the poetic and recursive role of naming in gameplay, memory, and AI.

---

## 1. 🧭 Folder Naming Conventions

### 🟦 Game Mode Folders (Tier 1)

All game modes must end in `_mode/`.

**Examples:**

- `a0_0_sailing_mode/`
- `a2_1_funhouse_mode/`
- `a3_3_testing_mode/`

### 🟩 Minigame Folders (Tier 2)

All minigame folders must end in `_minigame/`.

**Examples:**

- `enchanted_isle_minigame/`
- `crumbling_castle_minigame/`

### 🟨 Minigame Node Folders (Tier 3)

All nodes must end in `_node/`.

**Examples:**

- `whispering_grove_node/`
- `echoing_cave_node/`

---

## 2. 📁 Planning Folder Names

| Folder Type        | Required Name         |
|--------------------|------------------------|
| Minigame planning  | `taskmaps/`            |
| Game mode planning | `roadmaps/`            |
| Anomaly handling   | `mirror_decisions/`    |
| AI subsystem plans | Named after AI domain  |

All planning folders must contain the required files defined in `planning_spaces.md`.

---

## 3. 🧠 File Suffix Conventions

| Suffix      | Meaning                             | Example                     |
|-------------|-------------------------------------|-----------------------------|
| `.py`       | Logic, orchestration, or test file  | `leftmain.py`, `camouflage.py` |
| `.md`       | Planning, mapping, narrative intent | `roadmap.md`, `nodestanza_0.md` |
| `main.py`   | Always handles L or R logic         | `leftmain.py`, `rightmain.py` |
| `test.py`   | Must mirror the file it tests       | `camoutest.py`, `orchtest.py` |

Storytelling logic must reside in `story.py` and `storytest.py`.

---

## 4. 🧾 Planning File Naming

| Folder        | Required Files                                              |
|---------------|-------------------------------------------------------------|
| `taskmaps/`   | `__init__.py`, `milestones.md`, `README.md`, `nodestanza_0.md`, `taskmap.md` |
| `roadmaps/`   | `__init__.py`, `milestones.md`, `README.md`, `roadstanza_0.md`, `roadmap.md` |
| `mirror_decisions/` | `__init__.py`, `mirror_decision.md`, `fallbackmap.md`, `README.md`, `milestones.md` |

All planning folders must be Python modules (include `__init__.py`).

---

## 5. 🧬 Recursive Tier Structure

| Tier | Folder Ends In   | Contents                                     |
|------|------------------|----------------------------------------------|
| 1    | `_mode/`         | Roadmaps, Layer 1 orchestration              |
| 2    | `_minigame/`     | Taskmaps, Layer 2 stanza-driven gameplay     |
| 3    | `_node/`         | Actual interactive gameplay logic (L/R/story) |

All folder paths must follow this recursive descent:
`*_mode/` → `*_minigame/` → `*_node/`

---

## 6. 🎼 Stanza Numbering (Groups of Four)

Storybook Archipelago organizes content into rhythmic groups of four called **stanzas** at each layer. Use these canonical terms:

- Mirrorstanza: 4 game modes (workspace/world level)
- Roadstanza: 4 minigames (mode level)
- Nodestanza: 4 nodes (minigame level)

Numbering uses the pattern `aS_I` where `S` is the stanza index starting at 0, and `I` is the item within the stanza (0..3). Examples for a minigame with:

- One stanza:
	- `a0_0...`, `a0_1...`, `a0_2...`, `a0_3...`

- Two stanzas:
	- `a0_0...`, `a0_1...`, `a0_2...`, `a0_3...`
	- `a1_0...`, `a1_1...`, `a1_2...`, `a1_3...`

- Six stanzas:
	- `a0_0...` → `a0_3...`
	- `a1_0...` → `a1_3...`
	- `a2_0...` → `a2_3...`
	- `a3_0...` → `a3_3...`
	- `a4_0...` → `a4_3...`
	- `a5_0...` → `a5_3...`

This pattern applies at workspace, mode, and minigame levels. It aligns with our L/R traversal and keeps planning predictable. See also `workflow.md` and `roadmaps/` for mode stanza planning (roadstanza), and `taskmaps/` for minigame stanza planning (nodestanza).

---

## 7. 📖 Story and Camouflage Files (Tier 3)

Each Tier 3 `*_node/` must include:

- `story.py` — defines poetic logic and options
- `camouflage.py` — mood and recursion-layer control
- `orchestration.py` — memory, state, and path flow
- `integration.py` — master router between L/R/story

See: `minigame_template/` for full node file list.

---

## 🔚 Conclusion

Conventions are recursive safeguards.  
They allow AI tools, contributors, and test frameworks to:

- Predict file and folder locations
- Avoid naming collisions
- Traverse recursive paths correctly
- Maintain player immersion through structural camouflage

If a file or folder does not follow these conventions, it is considered invisible to the recursive system.
