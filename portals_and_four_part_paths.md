<!-- Save to: storybook_archipelago/portals_and_four_part_paths.md -->

# 🌉 portals_and_four_part_paths.md
**Canonical Protocol – Recursive Portal Structure for Storybook Archipelago**

> _"A single step across modes is a thousand across structure. Let each be known."_  

This file defines the canonical format, purpose, and safety requirements for **recursive portal paths** used in `portalmap.md`, AI routing, and all story-to-logic traversal systems within the Storybook Archipelago game project.

It governs not only how one node links to another, but also how entire game modes and workspaces communicate across recursive depth, virtual machines, and Azure resource containers.

---

## 🔁 Canonical Format – Four-Part Paths

All portal destinations must follow this format:

```yaml
{workspace}/{game_mode}/{minigame}/{node}/
```


Each part is **required**, even for local links.

### 📌 Component Breakdown

| Segment         | Description                                | Example                                      |
|------------------|--------------------------------------------|----------------------------------------------|
| `workspace`     | Full name of the VSC workspace, always begins with `storybook_` | `storybook_archipelago/` |
| `game_mode`     | Folder ending in `_mode/`                   | `a0_0_sailing_mode/`                         |
| `minigame`      | Folder ending in `_minigame/`               | `a0_0_enchanted_isle_minigame/`             |
| `node`          | Folder ending in `_node/`                   | `a0_1_drifting_glade_node/`                 |

---

## 🧠 Rationale

| Justification                | Why It Matters                                                |
|-----------------------------|---------------------------------------------------------------|
| ✅ **Disambiguation**        | Prevents confusion from duplicate node names across modes     |
| ✅ **Cross-Workspace Links** | Enables safe links between Visual Studio Code workspaces      |
| ✅ **AI Routing Integrity**  | Allows agents like `orchestration_ai` to trace full game paths|
| ✅ **Camouflage Drift**      | Helps memory systems detect tonal shifts across traversal      |
| ✅ **Export Safety**         | Supports `.pak`, `.zip`, and Azure deployments unambiguously  |

---

## 🗺️ Examples

| Use Case                     | Valid Path                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| 🔁 Local node jump           | `storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/` |
| 🌉 Cross-mode transition     | `storybook_archipelago/a0_5_shore_mode/a2_0_echo_ridge_minigame/a0_0_sand_gate_node/`             |
| 🌐 Cross-workspace linkage   | `storybook_primordial_soup/a3_2_overseer_mode/a9_1_hidden_cycle_minigame/a0_2_the_gate_that_looped/` |

---

## 🚫 Deprecated Path Formats

Avoid the following patterns:

- ❌ `a0_1_drifting_glade_node/` ← ambiguous
- ❌ `./a0_1_drifting_glade_node/` ← assumes filesystem-relative logic
- ❌ `../a0_1_drifting_glade_node/` ← breaks portability between workspaces
- ❌ paths without `storybook_` prefix

---

## 🤖 Router Expectations

Agents and routers (e.g., `integration.py`, `orchestration.py`, `high_command`) must:

- Accept only **fully qualified 4-part paths**
- Treat paths as **logical identifiers**, not OS filesystem paths
- Be prepared to resolve targets **across workspace boundaries** using future `workspace_registry.md`

---

## 🌐 Multi-Workspace Strategy

To support expansion beyond a single VSC instance:

- All VSC folders must begin with: `storybook_`
- Workspaces will be tracked in `workspace_registry.md` (see below)
- Cross-workspace node access must **never** use hardcoded drive paths

| Milestone                 | Resulting Workspace Shift                  |
|---------------------------|--------------------------------------------|
| ≥ 256 nodes               | Initiate workspace: `storybook_graphics/` or `storybook_multiplayer/` |
| Multiplayer test loop     | Launch: `storybook_netcode/`               |
| Community UI scaffolding  | Spin out: `storybook_loretools/`           |

---

## 📁 Storage & Naming Conventions

- ✅ All folders in a path must **end in a type suffix**:
  - `_mode/`, `_minigame/`, `_node/`
- ✅ All workspaces must begin with: `storybook_`
- ✅ Paths are always **lowercase**, snake_case only
- ✅ No trailing slashes when used in variables (only in `portalmap.md`)

---

## 🔧 Future Companion Files

| File                          | Purpose                                                          |
|-------------------------------|------------------------------------------------------------------|
| `workspace_registry.md`       | Declares and maps all active `storybook_` workspaces             |
| `recursive_linkage_policy.md` | Defines when links are allowed, mirrored, or escalated          |
| `node_addressing_spec.md`     | Governs grammar and syntax of path declarations                 |
| `portal_fallback_protocol.md` | Describes what happens when a link cannot be resolved           |

---

## 🔚 Closing Thought

> _“A game world is not a line of code. It is a constellation of paths. Every link must know its sky.”_

This document governs the **structural integrity of traversal** throughout Storybook Archipelago — and ensures that recursion, redirection, and reflection remain possible, testable, and safe.

All `portalmap.md` files must follow this format.  
All cross-workspace links must conform.  
This is recursive law.
