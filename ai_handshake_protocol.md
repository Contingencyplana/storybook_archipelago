# 🤝 AI Handshake Protocol – Cooperative Conduct Between Recursive Agents

## 🧠 Purpose

This file defines **how** AI agents in Storybook Archipelago:

- Initiate collaboration  
- Request assistance  
- Hand off control  
- Avoid logical or narrative collisions  

The protocol ensures that recursive agents can **cooperate safely**, **interoperate transparently**, and **respect system boundaries**.

---

## 📘 Foundational Principles

- **Handshake > Override**  
  Agents must *request* assistance rather than acting unilaterally unless explicitly authorized (e.g., Tier 3 failsafe).

- **Every request is logged.**  
  Handshakes must leave a trace in the relevant `.log` or `.md` file (e.g., `trace_pressure.md`, `spymaster_report.md`).

- **Only request what you are allowed to receive.**  
  No agent may initiate a handshake outside its declared read/write scope (see `ai_agents.md`).

---

## 🔄 Common Handshake Patterns

### 1. `storytelling_ai/` → `camouflage_ai/`

- **Context**: A stanza’s tone requests a matching visual or auditory overlay.
- **Protocol**:
  - `storytelling_ai/` tags story with `tone: "regret"`
  - Handshake logged in `camouflage_trace.log`
  - `camouflage_ai/` applies "fog" or "echo" layer

---

### 2. `sentinel_ai/` → `counterintelligence_ai/`

- **Context**: A node reveals a traversal loop outside design bounds.
- **Protocol**:
  - `sentinel_ai/` triggers `loop_detected` alert
  - Logs anomaly to `recursive_anomaly_protocol.md`
  - Notifies `counterintelligence_ai/` (but does not activate)
  - Waits for Tier 3 escalation or human review

---

### 3. `spymaster_ai/` → `high_command_mode/`

- **Context**: Cross-agent pattern deviation over multiple sessions
- **Protocol**:
  - Logs pattern correlation in `spymaster_report.md`
  - Sends Tier 2 escalation request to `high_command_mode/`
  - Action deferred pending quorum or pattern threshold

---

## 🚫 Prohibited Handshake Types

| From                   | To                       | Why Disallowed                                   |
|------------------------|--------------------------|--------------------------------------------------|
| `filename_mode/`       | `memory_state.md`        | Naming logic must not alter memory               |
| `camouflage_ai/`       | `story.py`               | Visual overlays cannot rewrite narrative         |
| `intelligence_ai/`     | `rollback.log`           | Exploratory agents cannot trigger failsafes      |
| `spymaster_ai/`        | Any direct write agent   | Observer agents must remain passive              |

---

## 🧬 Escalation vs Collaboration

- **Collaboration**: A Tier 1–2 agent asks another for context-sensitive output (e.g., tone, test).
- **Escalation**: A Tier 2+ agent reports to a failsafe (e.g., `high_command_mode/`, `counterintelligence_ai/`) — see `agent_escalation_matrix.md`.

---

## 🧾 Logging Requirements

All handshakes must leave an audit trail. Suggested log formats:

```json
{
  "from": "storytelling_ai",
  "to": "camouflage_ai",
  "purpose": "tone_overlay_request",
  "details": {
    "tone": "sorrow",
    "node_id": "a2_3_dream_of_lost_names"
  },
  "timestamp": "2025-08-02T22:16:00Z"
}
```

Use `.log` or `.md` files that correspond to the subsystem:

- `trace_pressure.md`
- `camouflage_trace.log`
- `spymaster_report.md`
- `anomaly_trace.md`

---

🧩 **Final Insight**

> Recursion is not safe because agents act alone.  
> Recursion is safe because they **talk** to each other — and **listen**.

The handshake protocol is the **language of recursive civilization**.  
Without it, the story breaks — not from chaos, but from silence.

**Let agents speak — but only within their bounds.**
