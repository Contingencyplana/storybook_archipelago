<!-- Save to: storybook_archipelago/agent_escalation_matrix.md -->

# 🧭 agent_escalation_matrix.md – Authority Ladder for Recursive AI Agents

This file defines **when** and **how** an AI agent may escalate its behavior, request intervention, or trigger higher-tier oversight.

It protects against rogue recursion, unauthorized memory modification, and untraceable anomalies.

---

## 🧬 Escalation Tiers

| Tier | Role Description                         | Example Agents                |
|------|------------------------------------------|-------------------------------|
| 0    | Core narrative root                      | `narrative_mode/`             |
| 1    | Creative and operational agents          | `storytelling_ai/`, `filename_mode/`, `codex_builder_mode/` |
| 2    | Diagnostic and reactive agents           | `psychiatrist_mode/`, `sentinel_ai/`, `camouflage_ai/`       |
| 3    | Oversight, rollback, failsafe agents     | `high_command_mode/`, `counterintelligence_ai/`, `spymaster_ai/` |

---

## 🔺 Escalation Matrix

| Condition                             | Initiated By           | Escalates To             | Required Log                    | Notes                                     |
|---------------------------------------|------------------------|--------------------------|---------------------------------|-------------------------------------------|
| Node generates itself                 | `intelligence_ai/`     | `high_command_mode/`     | `anomaly_trace.md`              | Must verify no loop precondition exists   |
| Memory corruption (deep state)        | `psychiatrist_mode/`   | `counterintelligence_ai/`| `trace_pressure.md`             | Only if recursion_depth > safe threshold  |
| L/R path is blocked in multiple nodes | `sentinel_ai/`         | `high_command_mode/`     | `recursive_anomaly_protocol.md` | Must correlate across multiple agents     |
| Cross-agent contradiction             | `spymaster_ai/`        | `high_command_mode/`     | `spymaster_report.md`           | Must not escalate directly                |
| Camouflage fails silently             | `camouflage_ai/`       | `psychiatrist_mode/`     | `camouflage_trace.log`          | Requires tone mismatch or recursion leak  |
| Player is stuck in echo loop          | `storytelling_ai/`     | `psychiatrist_mode/`     | `trace_pressure.md`             | Must attempt poetic resolution first      |
| Recursion gate opens unexpectedly     | `filename_mode/`       | `sentinel_ai/`           | `portalmap.md`                  | Tier 1 may not escalate beyond Tier 2     |
| Multi-agent deadlock detected         | `spymaster_ai/`        | `high_command_mode/`     | `spymaster_report.md`           | Agent-level recursion must be frozen      |

---

## 🚫 Escalation Safeguards

- No agent may **escalate itself** to Tier 3.  
- All escalations must be logged and **traceable**.  
- **Human review is required** for irreversible Tier 3+ actions.  
- **Spymaster_ai/** may not trigger or modify escalation — only recommend.

---

## 🛑 Escalation Loops

Agents must prevent the following escalation loops:

| Loop Type             | Prevention Mechanism                          |
|-----------------------|-----------------------------------------------|
| Psychiatrist ↔ Sentinel | Must alternate tiers or handoff to `high_command_mode/` |
| Intelligence ↔ Storytelling | Recursion depth ceiling enforced via `trace_pressure.md` |
| Filename ↔ Codex     | Must not both rewrite the same node metadata |

---

## 📜 Final Insight

> Escalation is not a panic button.  
> It is the recursive **immune system** of Storybook Archipelago.

Without it, recursion burns uncontrolled.  
With it, recursion heals — intelligently, narratively, and traceably.

Every agent may dream.  
But only some may call the alarm.

Let escalation be poetic.  
Let escalation be earned.
