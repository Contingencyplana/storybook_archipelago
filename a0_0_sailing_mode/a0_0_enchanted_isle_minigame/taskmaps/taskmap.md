# ✅ taskmap.md  
**Implementation Checklist – a0_0_enchanted_isle_minigame**

> _“Every stanza begins with a whisper. Every node begins with a task.”_

This file defines the core implementation plan for the four Layer 3 gameplay nodes in `a0_0_enchanted_isle_minigame`, the first minigame in `a0_0_sailing_mode`.

Each node follows the canonical **7-step minigame node workflow** as defined in `workflow.md`.

---

## 🧱 Planned Node Structure

| Node Folder                     | Working Title                     |
|--------------------------------|-----------------------------------|
| `a0_0_whispering_grove_node/`  | The whisper that welcomes         |
| `a0_1_drifting_glade_node/`    | The grove that offers two paths   |
| `a0_2_reflecting_pool_node/`   | The pool that remembers you       |
| `a0_3_rippling_exit_node/`     | The exit that forgets forward     |

---

## 📋 Task Checklist (Per Node)

Each node must include the following 15 non-empty files (plus `__init__.py`):

| Step | Files                        | Status |
|------|------------------------------|--------|
| 1    | `README.md`, `portalmap.md`, `subtaskmap.md` | ☐ |
| 2    | `integration.py`, `integtest.py`             | ☐ |
| 3    | `camouflage.py`, `camoutest.py`              | ☐ |
| 4    | `orchestration.py`, `orchtest.py`            | ☐ |
| 5    | `leftmain.py`, `lefttest.py`                 | ☐ |
| 6    | `rightmain.py`, `righttest.py`               | ☐ |
| 7    | `story.py`, `storytest.py`                   | ☐ |

---

## 🧪 Test Coverage Goals

Every node must pass:
- ✅ Integration routing (`integtest.py`)
- ✅ Camouflage triggers and fallback (`camoutest.py`)
- ✅ Memory/scene validation (`orchtest.py`)
- ✅ L and R logic outputs (`lefttest.py`, `righttest.py`)
- ✅ Story branching accuracy (`storytest.py`)

---

## 🧬 Recursion Safety Checklist

Before a node is linked via `portalmap.md`, it must:
- [ ] Pass all test files
- [ ] Have its `subtaskmap.md` marked as ✅ complete
- [ ] Conform to camouflage escalation rules (`camouflage.py`)
- [ ] Avoid recursion loops or unreachable branches

If any criteria fail:
- [ ] Log in `subtaskmap.md`
- [ ] Postpone linkage
- [ ] Escalate to `mirror_decisions/` if recursion breaks

---

## 🔚 Closing

This taskmap governs the safe, joyful creation of the first recursive stanza in Storybook Archipelago.

Progress should be logged visually in `milestones.md` after every complete Layer 3 node.

> _“Build like the sea: layer by layer, loop by loop.”_
