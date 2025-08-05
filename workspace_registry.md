# 🗂️ workspace_registry.md
**Registry of Storybook Workspaces**

> _"To travel the archipelago, you must first know which shores exist."_  

This file defines the official registry of all `storybook_` Visual Studio Code workspaces recognized by the Storybook game ecosystem.  
It is used by AI agents, routers, portal resolvers, and exporters to validate or traverse portal paths across multiple game spaces.

---

## 📜 Canonical Format

Each entry must follow this structure:

```yaml
- id: storybook_example
  title: Short human-readable description
  path: /relative/path/from/global/root/
  status: active | archived | external
  notes: optional clarifying information
```

✅ Registered Workspaces
🧱 1. storybook/

```yaml
- id: storybook
  title: Core Game Maker and SHAGI Engine
  path: storybook/
  status: active
  notes: Root design system, editor logic, builder recursion layers.
```

🌊 2. storybook_archipelago/

```yaml
- id: storybook_archipelago
  title: Repair Game – Entry into Poetic Recursion
  path: storybook_archipelago/
  status: active
  notes: Game mode launcher, poetic node recursion, player-facing stanzas.
```

🤖 3. storybook_fun_factory/

```yaml
- id: storybook_fun_factory
  title: Chaos Engine and Test World
  path: storybook_fun_factory/
  status: active
  notes: Randomness simulator, AI stress tests, edge case generators.
```

🧬 4. storybook_primordial_soup/

```yaml
- id: storybook_primordial_soup
  title: Recursive Multiplayer Cellworld
  path: storybook_primordial_soup/
  status: active
  notes: Cybercell growth, AI memory loops, multiplayer recursion.
```

## 🔁 Workspace Usage Guidelines

- All `portalmap.md` files must use the `id` value from this file as the **first path segment**.
- Any workspace not listed here is **non-canonical** and must not be referenced in routing.
- Archived or external workspaces may still be linked, but only with **safeguards** and **resolution layers** in place.

---

## 📓 Notes

- This registry is intended to support future tools such as:
  - ✅ AI routing agents
  - ✅ Visualization overlays
  - ✅ Cloud-to-local resolution bridges
  - ✅ `orchestration_ai` link validators
- The file is **machine-readable** and **human-maintainable**.
- It should be **updated** whenever a new Visual Studio Code workspace is introduced to the Storybook project family.

> _“Let the registry be a map to recursion, not a lock upon it.”_
