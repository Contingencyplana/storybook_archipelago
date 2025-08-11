<!-- Save to: storybook_archipelago/workflow.md -->

---
id: workflow
title: Canonical Build and Recursion Workflow
version: 1.0.0
status: stable
owners: [ "Storybook Archipelago Core" ]
last_updated: 2025-08-09
depends_on:
  - portals_and_four_part_paths.md   # Gate A
  - workspace_registry.md            # Gate A
links:
  - test_strategy.md
  - worldmap.md
  - planning_spaces.md
  - camouflage_layers.md
  - recursive_anomaly_protocol.md
---

# 🧱 workflow.md
**Canonical Build and Recursion Workflow – Storybook Archipelago**

> _“To build is to recurse with care. To recurse is to build with order.”_

This file defines the **step‑by‑step process** for creating game modes, minigames, and nodes in Storybook Archipelago using **test‑first**, **four‑part paths**, and **camouflage‑compliant** methods.

## 0) 🧭 Execution Modes (humans + VSC GPT-5)

We use two ways to build nodes:

- **Standard (7-step)** — follow the detailed sequence below. Use for new mechanics or anything cross-cutting.
- **Fast-path (automation)** — when the node is simple Tier-3, we compress into **2–3 passes**:

  1) Planning shell (`README.md`, `portalmap.md`, `subtaskmap.md`)
  2) One-shot build + tests + guard sweeps (integration, camouflage, orchestration, left/right, story)
  3) Activate portals + log milestones

**Fast-path criteria:** tiny, idempotent edits; tests run from repo root; guards clean (disallow the closed-bracket portal tag variant; use “[PORTAL:” only), and handlers/story return **strings only**.

**Definition of done (any mode):**

- Pytest green for the node and repo
- Guard sweeps clean
- `README.md`/`portalmap.md`/`subtaskmap.md` updated
- Milestones logged (node + root when relevant)
- Portals flipped to **Active** only when the downstream target exists and tests are green

---

## 1) 🗺️ Layered Build Order — Game World Structure

Storybook Archipelago unfolds recursively in **three tiers**:

| Tier | Folder Suffix | Description                              |
|-----:|----------------|------------------------------------------|
| 1    | `_mode/`       | Game modes / world zones                 |
| 2    | `_minigame/`   | Thematic gameplay clusters (stanzic)     |
| 3    | `_node/`       | Individual interactive L/R nodes         |

- Each **mode** contains **minigames**.  
- Each **minigame** contains **nodes**.  
- Each **node** contains **logic**, **camouflage**, **state**, and **story** layers.

> **Pathing rule:** All links in any `portalmap.md` **must** use the four‑part path format from `portals_and_four_part_paths.md`.

---

## 2) 🌀 Seven‑Step Minigame Node Workflow

Create a functional Tier‑3 node using this **7‑step** sequence:

### **Step 1 — Planning Shell**

- `README.md` — Node purpose, camouflage intent, tone
- `portalmap.md` — L/R links using **four‑part paths** (placeholders allowed initially)
- `subtaskmap.md` — Checklist of implementation progress

### **Step 2 — Input Router**

- `integration.py` — Routes input to L, R, or story
- `integtest.py` — Validates dispatch logic

### **Step 3 — Camouflage Layer**

- `camouflage.py` — Mood, glitch, silence, recursion mask
- `camoutest.py` — Verifies trigger conditions, fallbacks

### **Step 4 — Orchestration Layer**

- `orchestration.py` — Memory state, transitions, conditionals
- `orchtest.py` — Validates memory flow and decision reactions

### **Step 5 — Left Path**

- `leftmain.py` — L‑button logic
- `lefttest.py` — Validates left path responses

### **Step 6 — Right Path**

- `rightmain.py` — R‑button logic
- `righttest.py` — Validates right path responses

### **Step 7 — Story Layer**

- `story.py` — Player-facing narrative and L/R poetic options
- `storytest.py` — Tests text branching and options display

> **Consistency note:** All storytelling content lives in `story.py`. Logic lives in `*main.py` files (incl. `storytelling_ai` orchestration when used).

Follow the **Return value contract (handlers & story) — v1** for string markers.

---

## 3) 🧪 Testing Protocol (per `test_strategy.md`)

- Every Python logic file (`*.py`) must have a matching `*test.py`.
- Scaffolding may start with partial tests, but **minimum test coverage** defined in `test_strategy.md` must be met **before a node is link‑enabled**.
- Tier‑3 nodes must pass **integration**, **camouflage**, and **orchestration** tests before being referenced in any upstream `portalmap.md`.
- CI must **fail** on:
  - Non‑canonical paths (relative, wrong suffix, missing `storybook_`)
  - Missing/duplicate test files for required modules
  - Lint violations specified in `test_strategy.md`

- Tests should use **absolute package imports** so `pytest -q` runs from the repo root (e.g., `from a0_0_sailing_mode.a0_0_enchanted_isle_minigame... import …`).
- `pytest.ini` sets `python_files = *test.py` for discovery.
- Nodes are Python packages (`__init__.py` present) so absolute imports resolve.

---

## 4) 📁 Planning Folders

| Planning Folder     | Purpose                                                      |
|---------------------|--------------------------------------------------------------|
| `taskmaps/`         | Stanza/task planning within a minigame                       |
| `roadmaps/`         | Mode‑level planning of minigame sequence and themes         |
| `mirror_decisions/` | Activated only on anomaly; holds containment/rollback docs  |

All planning folders must include the canonical files listed in `planning_spaces.md`.

---

## 5) 🔁 Recursive Safety & Automation

- Minigame generation may be **manual** or **automated**. Prefer the **7‑step** pattern; a compressed **fast-path** is allowed for simple Tier‑3 nodes when criteria in **Execution Modes** are met (idempotent changes, tests + guards green, milestones updated).
- Any skipped step must be marked in `subtaskmap.md` with ☐ and a short rationale.
- Automation stanzas (e.g., compiler/validators) may compress steps, but only under **`high_command`** oversight and with tests updated accordingly.

---

## 6) 🧬 Fallbacks & Anomaly Handling

- If a node fails tests or introduces branching drift, flag it in `subtaskmap.md` and block it from `portalmap.md` until fixed.
- If a minigame collapses recursion or corrupts traversal, escalate to `mirror_decisions/` and follow `recursive_anomaly_protocol.md`.
- All anomalies must record:
  - Trigger conditions
  - Containment actions
  - Re‑entry criteria (tests required to restore links)

---

## 7) ⚙️ Tooling Hooks (recommended)

- **Pre‑commit**: path linter (four‑part), filename suffix linter, Markdown lint
- **CI jobs**:
  - `validate-paths` (four‑part + registry cross‑check)
  - `run-tests` (per `test_strategy.md`)
  - `build-worldmap` (verifies `worldmap.md` references resolve)
- **VS Code tasks**:
  - `Validate Docs` → linters + schema checks
  - `Audit Gate A–E` → targeted checks per acceptance gate

- CI: doc guard — disallow the closed-bracket portal tag variant; use “[PORTAL:” only.
- CI: code guard — disallow non-string returns in handlers/story.
- CI (optional): run tests on push/PR (install deps → `pytest -q`).

---

## 8) ✅ Acceptance & Gates

- **Node acceptance (Tier‑3 minimal viable slice):**
  - `integration.py` routes L/R/INVALID
  - `leftmain.py`/`rightmain.py` return structured results
  - `portalmap.md` uses **four‑part paths** only
  - Tests: `integtest.py` + at least one of `lefttest.py` or `righttest.py` pass

- **Gate mapping:**
  - **Gate A** (Step 1): Four‑part paths + registry validated repo‑wide
  - **Gate B** (Step 2): README/conventions/glossary stabilized
  - **Gate C** (Step 3): CI green; world map resolvable
  - **Gate D** (Step 4): Planning and design principles standardized
  - **Gate E** (Step 5): AI safety/escalation/tiers codified

---

## 🔚 Conclusion

This workflow governs **all gameplay creation** in Storybook Archipelago.  
It ensures recursion grows safely, nodes are testable, and gameplay remains **camouflaged, poetic, and traceable**.

> _“If the game is not TONS‑of‑FUN, the recursion isn’t done.”_  
> _(See `camouflage_layers.md`, Section 13)_
