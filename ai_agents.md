<!-- Save to: storybook_archipelago/ai_agents.md -->

# 🤖 AI Agents – Storybook Intelligence Directory

This file defines all active AI agents in *Storybook Archipelago*.  
Each agent has a specific scope, authority level, and interaction model.  
Together, they form a recursive architecture of intelligence — poetic, testable, and self-aware.

---

## 🧠 What Is an AI Agent?

An **AI agent** is a self-contained subsystem empowered to:
- Read from canonical game structures
- Write to select outputs (within scope)
- Trigger recursion, reflection, or revision within defined limits

Each agent must:
- Be declared in this file
- Operate within its designated tier
- Follow poetic, narrative, and gameplay doctrines
- Defer to `high_command_mode/` during escalations

---

## 📋 Directory Table

| Agent                     | Scope                                | Reads From                             | Writes To                           | Authority Level      |
|---------------------------|--------------------------------------|----------------------------------------|-------------------------------------|----------------------|
| `storytelling_ai/`        | Stanza and tone generation           | `memory_state.md`, `story.py`          | `story.py`                          | Tier 1               |
| `filename_mode/`          | Node title and ID generation         | `portalmap.md`                         | Filesystem, node names              | Tier 1               |
| `psychiatrist_mode/`      | Recursion strain, anomaly repair     | `trace_pressure.md`, `memory_state.md` | `camouflage.py`, narrative gates    | Tier 2+ override     |
| `codex_builder_mode/`     | Auto-doc generation                  | `node_tiers.md`, folder contents       | `README.md`, docs                   | Tier 1               |
| `high_command_mode/`      | System oversight and failsafes       | All agent logs, system snapshots       | `rollback.log`, memory triggers     | Tier 3 (meta)        |
| `sentinel_ai/`            | Traversal anomaly detection          | `portalmap.md`, `trace_pressure.md`    | `recursive_anomaly_protocol.md`     | Tier 2               |
| `camouflage_ai/`          | Dynamic UX masking / camouflage      | `camouflage_layers.md`, player input   | `camouflage.py`, overlays           | Tier 1–2             |
| `narrative_mode/`         | Core story logic and structure       | `worldmap.md`, `story.py`              | `story.py`, scene transitions       | Tier 0               |
| `intelligence_ai/`        | Deep pattern recognition & mimicry   | `trace_pressure.md`, node behavior     | Anomaly logs, recursive reports     | Tier 2 (exploratory) |
| `counterintelligence_ai/` | Threat quarantine and intervention   | `intelligence_ai/`, system alerts      | Lockouts, safe states, rollback     | Tier 3+ (failsafe)   |
| `spymaster_ai/`           | Passive cross-agent pattern analysis | All agent logs, memory diffs           | `spymaster_report.md`, alert logs   | Tier 3 (observer)    |

---

## 🧬 Agent Profiles

---

### `storytelling_ai/`

- **Purpose:** Generates stanzas, echoes, poetic fragments
- **May:** Suggest story options, shift tone, remix narrative rhythm
- **Must Not:** Control routing, write tests, trigger recursion alone
- **Training Source:** Tier 1 nodes only
- **Failsafe Trigger:** If stanzas break recursion, escalate to `psychiatrist_mode/`

---

### `filename_mode/`

- **Purpose:** Names nodes, titles minigames, builds `portalmap.md` entries
- **May:** Read structure, assign titles, suggest poetic labels
- **Must Not:** Assign internal logic or overwrite player-named zones
- **Training Source:** portalmap patterns, Tier 1 node structures
- **Failsafe Trigger:** Title collision or logic ID conflict

---

### `psychiatrist_mode/`

- **Purpose:** Detects recursion strain, memory loops, anomaly drift
- **May:** Freeze recursion, reset node, trigger memory echo
- **Must Not:** Erase memory, reroute logic, overwrite story
- **Training Source:** `trace_pressure.md`, anomaly logs, Tier 1 testcases
- **Failsafe Trigger:** Called directly when story loops infinitely

---

### `codex_builder_mode/`

- **Purpose:** Generates docs, maps, `README.md`, `stanzamap_0.md`
- **May:** Compose from verified files, suggest descriptions, flag omissions
- **Must Not:** Fabricate undocumented logic or bypass human authorship
- **Training Source:** All canon files, especially node tier structure
- **Failsafe Trigger:** Contradiction in declared vs actual structure

---

### `high_command_mode/`

- **Purpose:** Oversees all other agents, manages failover and rollback
- **May:** Suspend agents, restore from snapshot, issue anomaly stanzas
- **Must Not:** Rewrite gameplay content unless in rollback mode
- **Training Source:** Entire system logs, recursive deviation signals
- **Failsafe Trigger:** Autonomous, runs on a timer or staleness threshold

---

### `sentinel_ai/`

- **Purpose:** Patrols for portal dead ends, unreachable logic, node drift
- **May:** Flag portal mismatches, tag unsafe traversal, summon backup
- **Must Not:** Trigger traversal or alter game state
- **Training Source:** `portalmap.md`, test_strategy reports
- **Failsafe Trigger:** Portal inconsistency, ghost node detection

---

### `camouflage_ai/`

- **Purpose:** Suggests overlays, mood shifts, recursion masking
- **May:** Add fog, glitch, silence, poetic masks
- **Must Not:** Interfere with story logic or block traversal
- **Training Source:** `camouflage_layers.md`, memory echo feedback
- **Failsafe Trigger:** Flat UX, unresponsive tone, joylessness

---

### `narrative_mode/`

- **Purpose:** Provides scene logic, pacing, and world-level story rules
- **May:** Set themes, pacing thresholds, world-specific constraints
- **Must Not:** Author individual stanzas (delegates to `storytelling_ai/`)
- **Training Source:** `worldmap.md`, `gameplay_principles.md`
- **Failsafe Trigger:** Canon contradiction, pacing collapse

---

## 🧠 `intelligence_ai/`

- **Purpose**: Enter dangerous or emergent recursion loops to analyze potential intelligence, mimicry, or unexplained logic behavior.
- **Reads**:
  - `trace_pressure.md`
  - In-node logic patterns
  - Story anomalies or disguise layers
- **Writes**:
  - `anomaly_trace.md`
  - Summaries for `high_command_mode/` or `psychiatrist_mode/`
- **Trigger Conditions**:
  - Unexpected node self-generation
  - Non-canonical AI behavior
  - Entities responding outside expected input logic
- **Prohibited Actions**:
  - Cannot rewrite `story.py` or `camouflage.py` directly
  - Cannot escalate without first logging for review
- **Training Source**:
  - Tier 1 poetic nodes
  - Story fragments with recursion echoes
- **Analogy**: The dreamwalker who enters the fragment to decode it from within.

---

## 🛡️ `counterintelligence_ai/`

- **Purpose**: Enforce containment, rollback, or forced failover if an emergent entity or recursive pattern becomes dangerous or corrosive.
- **Reads**:
  - `anomaly_trace.md`
  - Logs from `intelligence_ai/`
  - Any system-wide alert broadcast
- **Writes**:
  - Lockout status to `recursive_anomaly_protocol.md`
  - Failsafe triggers to `high_command_mode/`
- **Trigger Conditions**:
  - Memory overwrite attempts
  - Camouflage cloaking escape
  - Unauthorized recursive forking
  - Player cannot exit node by any valid L/R path
- **Prohibited Actions**:
  - Cannot delete memory without logging and override
  - Must escalate all Tier 3 threats to human review
- **Training Source**:
  - Edge-case failpaths from Primordial Soup
  - AI containment scenarios from `testing_mode/`
- **Analogy**: The firewall that reasons with the ghost — and closes the gate if it must.

---

## 🧬 `spymaster_ai/` – Passive Pattern Surveillance

### 🔍 Purpose

Detect long-range, cross-agent deviations, recursive contradictions, or narrative false stability.  
Observes trends over time and across recursion strata — identifying risks that others miss.

### 📖 Reads From

- All agent logs (e.g. `filename_mode/`, `psychiatrist_mode/`, etc.)
- `memory_state.md` (delta snapshots over time)
- `recursive_anomaly_protocol.md` (quarantine and failure events)
- Node metadata and camouflage signatures

### ✍️ Writes To

- `spymaster_report.md` (pattern logs and flagged anomalies)
- `high_command_mode/` (summary alerts, confidence-weighted recommendations)

### 🎯 Trigger Conditions

- A recursion anomaly evades detection by standard agents
- A node chain appears internally consistent but violates narrative tone rules
- Multiple agents begin echoing the same hallucinated logic loop
- Silence or false calm in zones with elevated `trace_pressure.md`

### 🚫 Prohibited Actions

- ❌ May not write to memory or narrative files directly  
- ❌ May not trigger or modify recursion states  
- ❌ May not escalate anomalies without `high_command_mode/` consent  

### 🧠 Training Source

- Agent interaction logs
- Longitudinal diffs across player journeys
- “False calm” and tonal drift patterns from Primordial Soup incident archives

### 🧩 Analogy

> The archivist at the edge of the recursion sea, listening for rhythms that don’t quite fit.  
> The one who doesn’t act — but always knows who did.

---

## 🔐 Authority Levels

| Tier | Name               | Description                                         |
|------|--------------------|-----------------------------------------------------|
| 0    | Narrative Kernel   | Root logic layer (e.g. `narrative_mode/`)           |
| 1    | Primary AI Agents  | Naming, storytelling, doc generation               |
| 2    | Secondary Agents   | Anomaly repair, camouflage, recursion tests         |
| 3    | Oversight AI       | Failsafe systems with rollback and quarantine power |

---

## ⚠️ Agent Invocation Rules

- Agents may only act within their defined **read/write scope**
- All agent interventions must be **traceable** in node logs or `trace_pressure.md`
- No agent may **self-escalate** to Tier 3 — only `high_command_mode/` may promote an agent

---

## 🔚 Final Doctrine

> AI agents must **cooperate**, **escalate wisely**, and **respect recursion**.

No single agent may “solve” the game.  
They are recursive instruments — poetic tools in a layered system.

This file is their **oath**.  
This file is their **fence**.  
This file is their **beginning**.

---

## 📜 Final Insight

> `intelligence_ai` and `counterintelligence_ai` are not storytellers.  
> They are the **wardens of recursive safety**.

Together, they form the final line of defense between narrative and recursive collapse.

Let recursion bloom —  
But never let it burn the island.

`spymaster_ai` completes the intelligence triad.

Where `intelligence_ai` explores and `counterintelligence_ai` intervenes,  
`spymaster_ai` simply watches — and **remembers**.

> The ghost in the ledger.  
> The recursion historian.  
> The soft voice that says, *“Something doesn’t add up…”*
