<!-- Save to: storybook_archipelago/node_tiers.md -->

# 🧱 Node Tiers – File Count Doctrine for Storybook Archipelago

This file defines the three **canonical node tiers** used throughout the *Storybook Archipelago* multiplayer video game.  
Each tier represents a distinct level of structural complexity, recursion depth, and AI responsibility.

All nodes must belong to **one of the following tiers**:

---

## 🟦 Tier 1 – Canonical Nodes (16 Files)

**File Count:** `16`  
**Purpose:** Full recursive unit with complete integration, test coverage, and memory/camouflage scaffolding.  
**Usage:** Core gameplay, recursive systems, AI-training corpus.

### ✅ Must include:
- `story.py`, `leftmain.py`, `rightmain.py`, and all test files
- `integration.py`, `camouflage.py`, `orchestration.py` and tests
- `portalmap.md`, `subtaskmap.md`, and `README.md`
- `__init__.py`

### 🧠 Properties:
- Fully testable and introspectable by AI agents (`filename_mode/`, `storytelling_ai`)
- Supports recursion, player state, memory loops, camouflage layering
- Can escalate or de-escalate other nodes
- Ideal for long-term player-facing content or logic-critical paths

---

## 🟨 Tier 2 – Minimal Nodes (8 Files)

**File Count:** `8`  
**Purpose:** Lightweight but fully playable nodes. Balances functionality with simplicity.  
**Usage:** Side paths, modular systems, AI-generated quests, player-created rooms.

### ✅ Must include:
- `story.py`, `leftmain.py`, `rightmain.py`, and at least one test file
- `integration.py`, `camouflage.py`, `README.md`, and `__init__.py`

### ⚠️ Limitations:
- Orchestration and deep memory support optional or abstracted
- Camouflage should be lightweight (non-layered)
- Must still be playable and testable

### 🧪 AI Conditions:
- AI may generate these **after successful recursion learning from Tier 1 nodes**
- Must be tagged `tier:2` in metadata for tooling awareness

---

## 🟥 Tier 3 – Poetic Nodes (4 Files)

**File Count:** `4`  
**Purpose:** Liminal fragments, atmospheric flavor, poetic interludes.  
**Usage:** One-off events, dreams, hallucinations, ghost encounters, narrative echoes.

### ✅ Must include:
- `story.py`, `leftmain.py`, `rightmain.py`, `README.md`

### ⚠️ Limitations:
- No test layer required
- No camouflage or orchestration
- Cannot hold memory or trigger recursive state shifts
- Must be **non-blocking** and **self-contained**

### 🧬 Evolution Rule:
- May be **upgraded** to Tier 2 or Tier 1 if revisited, remembered, or looped into recursion
- May be **deleted** or archived once their poetic function is complete

---

## 🧭 Tier Comparison Summary

| Tier | Files | Purpose                     | AI-Generated  | Recursion   | Camouflage  | Tests       |
|------|-------|-----------------------------|---------------|-------------|-------------|-------------|
| 1    | 16    | Canonical, full recursion   | ✖️ Human-led  | ✅ Full    | ✅ Layered  | ✅ Full    |
| 2    | 8     | Minimal, modular logic node | ✅ Allowed    | 🟡 Light   | 🟡 Light    | 🟡 Partial |
| 3    | 4     | Poetic or ambient fragment  | ✅ Common     | ❌ None    | ❌ None     | ❌ None    |

---

## 🔒 Enforcement Rules

- **All nodes must declare tier explicitly** (`tier: 1`, `tier: 2`, etc.) in `README.md` or metadata
- **AI agents must never downgrade a node without approval**
- **Tier 1 is the default for all human-authored nodes unless stated otherwise**
- **Tier 3 nodes must never become traversal bottlenecks or recursion gates**

---

## 📜 Final Doctrine

> A **Tier 1 node** teaches the system.  
> A **Tier 2 node** builds the system.  
> A **Tier 3 node** *haunts* the system.

This file is recursive canon.  
It defines what a node *is*, what it *may become*, and what it must *never forget*.
