<!-- Path: C:\Users\Admin\storybook_archipelago\protocols\portals_protocol.md -->

# Portals Protocol v0.1

**Purpose:** Define how L/R (and optional numeric) choices link Cyberleaves safely and predictably.

---

## 1) Terminology & IDs

- **Leaf ID (canonical):** `namespace/island/leaf_name`
  - Pattern: `^[a-z0-9_-]+/[a-z0-9_-]+/[a-z0-9_-]+$`
  - Examples:
    - `archipelago/enchanted_isle/whispering_grove`
    - `primordial_pool/a0_0/entry`

---

## 2) Link Semantics

- **Primary choices:** `L`, `R`
- **Optional numeric choices:** `1..9` expressed as the **`numbers` array** in the registry.
  - Index rule: `numbers[0]` → option **1**, `numbers[1]` → option **2**, etc.
- **Where links are declared:**
  1. **Leaf-local**: `portalmap.md` (author intent per leaf)
  2. **Registry**: `registry/cybertree_registry.json` (source of truth for runtime)
  3. **Router**: default/fallback target (engine-wide)

**Resolution order at runtime:** _Registry_ → _Leaf-local_ → _Router fallback_
> The router reads the registry first; if absent, it consults `portalmap.md`; else it uses the default leaf.

---

## 3) Authoring: `portalmap.md` (per leaf)

Use this minimal template in each leaf:

```markdown
# Portal Map — <leaf_id>

- L → <leaf_id>
- R → <leaf_id>
- Numbers:
  - 1 → <leaf_id>   <!-- optional -->
  - 2 → <leaf_id>   <!-- optional -->

Notes:
- Brief intent for each link
- Temporary considerations (events, deprecations)
```

### Checklist (leaf-local)

- [ ] Targets exist (or have planned stubs)
- [ ] No accidental self-loop unless intended
- [ ] Numeric options (if any) match `story.py` numbering and count

---

## 4) Registry shape (runtime source of truth)

**Excerpt from** `registry/cybertree_registry.json`:

```json
{
  "portals": {
    "archipelago/enchanted_isle/whispering_grove": {
      "L": "archipelago/enchanted_isle/whispering_grove_left",
      "R": "archipelago/enchanted_isle/whispering_grove_right",
      "numbers": {
        "1": "archipelago/enchanted_isle/whispering_grove_1",
        "2": "archipelago/enchanted_isle/whispering_grove_2"
      }
    },
    "primordial_pool/a0_0/entry": {
      "L": "primordial_pool/a0_0/entry_left",
      "R": "primordial_pool/a0_0/entry_right",
      "numbers": {
        "1": "primordial_pool/a0_0/entry_1",
        "2": "primordial_pool/a0_0/entry_2"
      }
    }
  }
}
```

## 5) Fallbacks & Deprecations

- **Missing target** → route to **router default leaf** and show a friendly hint.
- **Deprecated target** → keep the old ID in the registry until callers are migrated; optionally point **L/R** to the replacement.
- **Invalid ID format** → treat as missing target (soft error; log, then fallback).

---

## 6) Testing Requirements

**Per leaf (Tier-1):**
- `lefttest.py` / `righttest.py` ensure **L/R** paths exist or intentionally return `next_leaf: null`.
- `storytest.py` verifies numeric option counts align with the `numbers` mapping (if used).

**Router/engine:**
- Unknown leaf → default leaf.
- Valid **L/R** transition → loads target leaf.
- Missing or malformed portal → soft error + fallback.
- Registry JSON passes schema validation in CI.

---

## 7) Versioning

- Changing portal **targets** is data-only and **does not** bump the engine version.
- Renaming a `leaf_id` is breaking for callers; maintain the old entry until all links are updated.

---

## 8) Operational Notes

- Prefer **registry-driven** changes for live updates; keep `portalmap.md` as design intent and documentation.
- Log soft errors for portal issues; crash only on router invariants.
