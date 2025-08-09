<!-- Save to: storybook_archipelago/portals_and_four_part_paths.md -->

# 🌉 portals_and_four_part_paths.md
**Canonical Protocol – Recursive Portal Structure for Storybook Archipelago**

> _"A single step across modes is a thousand across structure. Let each be known."_

This document defines the **canonical format, enforcement rules, and safety requirements** for all **recursive portal paths** used in:
- `portalmap.md` files
- AI routing and orchestration
- Story-to-logic traversal systems

It governs:
1. How one node links to another  
2. How entire game modes and workspaces communicate across recursive depth  
3. How links remain portable across Visual Studio Code workspaces, virtual machines, and Azure resource containers  

---

## 🔁 Canonical Format — Four-Part Paths

**All** portal destinations **must** use this format:

```yaml
{workspace}/{game_mode}/{minigame}/{node}/
```

Each part is **required**, even for local links.

| Segment     | Description                                                     | Example                         |
|-------------|-----------------------------------------------------------------|---------------------------------|
| `workspace` | Full name of the VSC workspace; always begins with `storybook_` | `storybook_archipelago/`        |
| `game_mode` | Folder ending in `_mode/`                                       | `a0_0_sailing_mode/`            |
| `minigame`  | Folder ending in `_minigame/`                                   | `a0_0_enchanted_isle_minigame/` |
| `node`      | Folder ending in `_node/`                                       | `a0_1_drifting_glade_node/`     |

---

## ✅ Enforcement Rules
- All paths must be **fully qualified** (no relative paths).  
- All folders in the path must **end with the correct type suffix**: `_mode/`, `_minigame/`, `_node/`.  
- All workspaces must begin with: `storybook_`.  
- Paths must be **lowercase**, snake_case only.  
- When stored in variables: **no trailing slash**.  
- Lint/test tools must reject any link that violates the above.

These rules will be cross-checked against:
- `workspace_registry.md` — authoritative list of valid workspaces  
- `workflow.md` — how links are created, tested, and published  

---

## 🧠 Why This Matters

| Reason                   | Impact                                                                 |
|--------------------------|------------------------------------------------------------------------|
| **Disambiguation**       | Prevents collisions between identically named nodes in different modes |
| **Cross-Workspace Links**| Enables safe links between VS Code workspaces                          |
| **AI Routing Integrity** | Guarantees agents can trace a complete game path                       |
| **Camouflage Drift**     | Allows tonal shifts to be detected across traversals                   |
| **Export Safety**        | Ensures `.pak`, `.zip`, and Azure builds resolve cleanly                |

---

## 🗺️ Examples

| Use Case              | Valid Path                                                                                           |
|-----------------------|------------------------------------------------------------------------------------------------------|
| Local node jump       | `storybook_archipelago/a0_0_sailing_mode/a0_0_enchanted_isle_minigame/a0_1_drifting_glade_node/`     |
| Cross-mode transition | `storybook_archipelago/a0_5_shore_mode/a2_0_echo_ridge_minigame/a0_0_sand_gate_node/`                |
| Cross-workspace link  | `storybook_primordial_soup/a3_2_overseer_mode/a9_1_hidden_cycle_minigame/a0_2_the_gate_that_looped/` |

---

## 🚫 Deprecated Formats (Blocked in Lint/Test)
- `a0_1_drifting_glade_node/` ← ambiguous  
- `./a0_1_drifting_glade_node/` ← assumes filesystem-relative logic  
- `../a0_1_drifting_glade_node/` ← breaks portability between workspaces  
- Paths without `storybook_` prefix  

---

## 🤖 Router Requirements
Any routing logic (e.g., `integration.py`, `orchestration.py`, `high_command`) must:
- Accept only fully qualified four-part paths  
- Treat paths as **logical identifiers**, not OS file paths  
- Resolve targets across workspaces using `workspace_registry.md`  
- Fail fast on any invalid path before attempting traversal  

---

## 🌐 Multi-Workspace Strategy
For projects exceeding a single workspace:
- All VSC folders must begin with: `storybook_`  
- Cross-workspace access must never use hardcoded drive letters or absolute OS paths  
- `workspace_registry.md` defines the official mapping between workspace names and locations  

| Milestone             | Resulting Workspace Shift                     |
|-----------------------|-----------------------------------------------|
| ≥ 256 nodes           | Add: `storybook_graphics/` or `storybook_multiplayer/` |
| Multiplayer test loop | Launch: `storybook_netcode/`                  |
| Community UI phase    | Spin out: `storybook_loretools/`              |

---

## 🔧 Related / Companion Specs

| File                          | Purpose                                                       |
|-------------------------------|---------------------------------------------------------------|
| `workspace_registry.md`       | Maps all active `storybook_` workspaces                       |
| `recursive_linkage_policy.md` | Rules for allowed, mirrored, or escalated links               |
| `node_addressing_spec.md`     | Grammar and syntax for path declarations                      |
| `portal_fallback_protocol.md` | Behaviour when a link cannot be resolved                      |

---

## 🔚 Closing Thought
> _“A game world is not a line of code. It is a constellation of paths. Every link must know its sky.”_

This document governs the **structural integrity of traversal** throughout Storybook Archipelago — ensuring recursion, redirection, and reflection remain possible, testable, and safe.

All `portalmap.md` files must follow this format.  
All cross-workspace links must conform.  
This is recursive law.
