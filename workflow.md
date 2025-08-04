# 🧱 workflow.md  
**Canonical Build and Recursion Workflow – Storybook Archipelago**

> _“To build is to recurse with care. To recurse is to build with order.”_  
> This file defines the step-by-step process for creating game modes, minigames, and nodes in Storybook Archipelago using recursive, test-first, and camouflage-compliant methodology.

---

## 1. 🗺️ Layered Build Order – Game World Structure

Storybook Archipelago unfolds recursively in **three tiers**:

| Tier | Folder Ends In     | Description                          |
|------|--------------------|--------------------------------------|
| 1    | `_mode/`           | Game modes / world zones             |
| 2    | `_minigame/`       | Thematic gameplay clusters (stanzic) |
| 3    | `_node/`           | Individual interactive L/R nodes     |

Each game mode contains minigames.  
Each minigame contains nodes.  
Each node contains logic, camouflage, state, and story layers.

---

## 2. 🌀 Seven-Step Minigame Node Workflow

To create a functional gameplay node, follow this 7-step process:

### **Step 1 – Planning Shell**
- `README.md` – Node purpose, camouflage intent, tone
- `portalmap.md` – L/R links to other nodes (can be placeholders)
- `subtaskmap.md` – Checklist of implementation progress

### **Step 2 – Input Router**
- `integration.py` – Routes input to L, R, or story
- `integtest.py` – Validates dispatch logic

### **Step 3 – Camouflage Layer**
- `camouflage.py` – Mood, glitch, silence, recursion mask
- `camoutest.py` – Verifies trigger conditions, fallback

### **Step 4 – Orchestration Layer**
- `orchestration.py` – Memory state, transitions, conditionals
- `orchtest.py` – Validates memory flow and decision reactions

### **Step 5 – Left Path**
- `leftmain.py` – L-button logic
- `lefttest.py` – Validates left path responses

### **Step 6 – Right Path**
- `rightmain.py` – R-button logic
- `righttest.py` – Validates right path responses

### **Step 7 – Story Layer**
- `story.py` – Player-facing narrative and L/R poetic options
- `storytest.py` – Tests text branching and options display

---

## 3. 🧪 Testing Protocol (Per `test_strategy.md`)

- Every `.py` logic file must have a matching `test.py`
- Testing may be partial during early scaffolding but must reach **minimum coverage before gameplay activation**
- Tier 3 nodes must pass `camouflage`, `integration`, and `orchestration` tests before being linked in `portalmap.md`

---

## 4. 📁 Planning Folder Use

| Planning Folder     | Use Case |
|---------------------|----------|
| `taskmaps/`         | Used inside each minigame for stanza planning and execution |
| `roadmaps/`         | Used inside each game mode to plan minigame sequence and theme |
| `mirror_decisions/` | Dormant until triggered by recursive anomaly (used for containment, rollback, and diagnostics) |

All planning folders must contain the canonical files listed in `planning_spaces.md`.

---

## 5. 🔁 Recursive Safety and Automation

- All minigame generation may be **manual or automated**, but must follow the 7-step build pattern
- Any skipped step must be marked in `subtaskmap.md` with ☐
- Automation stanzas (e.g. `compiler_ai/`) may override this flow, but only if supervised by `high_command`

---

## 6. 🧬 Fallbacks and Anomaly Handling

- If a node fails tests or introduces branching drift, it must be flagged in its `subtaskmap.md`
- If a minigame collapses recursion or logic, escalate to `mirror_decisions/`
- Anomaly triggers are routed through `recursive_anomaly_protocol.md`

---

## 🔚 Conclusion

This workflow governs **all gameplay creation** in Storybook Archipelago.  
It ensures recursion grows safely, nodes are testable, and gameplay remains camouflaged, poetic, and traceable.

> _“If the game is not TONS-of-FUN, the recursion isn’t done.”_  
> _(See: `camouflage_layers.md → Section 13`)_
