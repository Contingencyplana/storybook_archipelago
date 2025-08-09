<!-- Save to: storybook_archipelago/workspace_registry.md -->

# 🗂️ workspace_registry.md
**Registry of Storybook Workspaces**

> _"To travel the archipelago, you must first know which shores exist."_

This file defines the **authoritative registry** of all `storybook_` Visual Studio Code workspaces recognized by the Storybook game ecosystem.  
It is used by AI agents, routers, portal resolvers, and exporters to **validate** or **traverse** portal paths across multiple game spaces.

---

## 📜 Canonical Entry Format

Each entry **must** follow this YAML structure:

```yaml
- id: storybook_example            # required; lowercase, snake_case; must start with "storybook_"
  title: Short human-readable description
  path: relative/path/from/root/   # required; relative to global workspace container
  status: active | archived | external
  notes: optional clarifying information
```

## ♻️ Legacy IDs (grandfathered)
- `storybook` — **allowed as a one‑time legacy exception** for historical reasons.
  - New workspaces MUST use the `storybook_` prefix (e.g., `storybook_core`, `storybook_archipelago`, …).
  - Migration plan: `storybook` → `storybook_core` during the **Heal** pass (cybernurse/cyberdoc milestone). Validators should treat `storybook` as valid until that migration completes.

## 🔒 Enforcement Rules

- `id` is the **exact string** used as the first segment of any four-part path.  
- `path` must be **relative to the workspace container**; never an absolute OS path.  
- Lint/test tools must reject:
  - IDs not starting with `storybook_`
  - Missing or duplicate IDs
  - Invalid `status` values
- Archived/external workspaces must only be linked with **safeguards** and **resolution layers**.

---

## ✅ Registered Workspaces

### 🧱 1. storybook/

```yaml
- id: storybook
  title: Core Game Maker and SHAGI Engine
  path: storybook/
  status: active
  notes: Root design system, editor logic, builder recursion layers. Grandfathered legacy id; scheduled to rename to `storybook_core` during Heal phase.
```

### 🌊 2. storybook_archipelago/

```yaml
- id: storybook_archipelago
  title: Repair Game – Entry into Poetic Recursion
  path: storybook_archipelago/
  status: active
  notes: Game mode launcher, poetic node recursion, player-facing stanzas.
```

### 🤖 3. storybook_fun_factory/

```yaml
- id: storybook_fun_factory
  title: Chaos Engine and Test World
  path: storybook_fun_factory/
  status: active
  notes: Randomness simulator, AI stress tests, edge case generators.
```

### 🧬 4. storybook_primordial_soup/

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
- Archived or external workspaces:
  - May still be linked if explicitly marked in `status`.
  - Must include safeguards and a resolution layer before traversal.

---

## 📓 Notes

This registry supports:
- ✅ AI routing agents
- ✅ Visualization overlays
- ✅ Cloud-to-local resolution bridges
- ✅ `orchestration_ai` link validators

The file is **machine-readable** and **human-maintainable**.  
It should be **updated** whenever a new Visual Studio Code workspace is introduced to the Storybook project family.

> _“Let the registry be a map to recursion, not a lock upon it.”_
