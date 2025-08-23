# Portalmap Conventions — Storybook Archipelago

**Status:** Draft v0.1 • Owner: Vision Holder • Last updated: 2025-08-23
**Purpose:** Define canonical conventions for portalmaps across nodes and minigames.

---

## 🎴 Core Elements

- **Bookmarks (Zones 2 & 4):**
  - Represented as entries in `portalmap.md`.
  - Each bookmark has a label (short, 1–2 words) and a destination reference.
  - Bookmarks double as "save states" and quick navigation anchors.

- **Echo Jumps (Zones 2 & 4 non-bookmark clicks):**
  - Represented with the tag `echo_jump:`
  - Two options:
    - `random` → completely unbounded, dreamlike jump.
    - `patterned` → bounded/randomized jump, seeded by player memory, prior choices, or recursion weights.
  - Must specify seeding/weighting notes if `patterned`.

- **Page Turns (Zones 1 & 3):**
  - Default action unless numbered options override.
  - L = left page turn, R = right page turn.

- **Cover (Zone 5):**
  - Always available fallback → links to Main Menu.

---

## 📝 Authoring Notes

- Keep portalmap entries consistent across nodes in a minigame.
- Mark whether a jump is `bookmark`, `echo_jump: random`, or `echo_jump: patterned`.
- For playtest clarity, CLI placeholders (`Enter`, `L/R`, `1–3`, `q`) map to these zones until the client UI is active.

---

## 📌 Example Portalmap Entry

```yaml
- label: "Crystal Vault"
  destination: a0_3_crystal_vault_node
  type: bookmark

- label: "Whisper Echo"
  destination: random
  type: echo_jump: patterned
  seed: "memory_path"
```

Keep the file lightweight (stub style, but specific enough to guide current node authors).
