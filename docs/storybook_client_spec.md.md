# Storybook Client Spec (Stub)

**Status:** Placeholder • Draft v0.1

This document will define the **client-side UI and interaction model** for the Storybook Archipelago video game.
It acts as the central reference for how the storybook is displayed, how players interact with it, and how click-zones map to game logic.

---

## Current Foundations

- The **Five Interaction Zones** (see [`ui_storybook_playbook.md`](./ui_storybook_playbook.md)) are the guiding metaphor:
  - Zone 1: Left Page
  - Zone 2: Left Page Edge (Bookmarks / Echo Jumps)
  - Zone 3: Right Page
  - Zone 4: Right Page Edge (Bookmarks / Echo Jumps)
  - Zone 5: Book Cover (Main Menu)

- **Input mapping**: see [`input_mapping.md`](./input_mapping.md) for the current CLI → Client key equivalences.
  (e.g., `l` = click left page, `r` = click right page, `Enter` = turn page, `1–3` = numbered option, `q/Ctrl+C` = menu/cover.)

---

## Pending Design Questions

- **Zone 2 & 4 “echo jumps”:**
  Should non-bookmark clicks be:
  - Truly random (dreamlike, chaotic), or
  - Patterned/randomized but bounded (seeded by memory, choices, or echoing mechanics)?

- **Main Menu styling (Zone 5):**
  Likely represented as a closed storybook on a desk, with a parchment note of menu choices beside it.

- **Bookmark presentation:**
  Currently assumed: ~100 slots per side, shown as a swatch of page ends.
  To be confirmed when save/load and quick travel are specified.

---

## Future Expansion

This spec will later cover:
- Visual resolution and asset requirements.
- Click-zone hitboxes and scaling across devices.
- Integration with sound, effects, and camouflage layers.
- Save/load flows tied to bookmarks.
- Accessibility notes (font scaling, colorblind safety, input remapping).

---

📌 **Note:** This file is a stub. It will expand into a full specification as the project moves toward **Alpha (multi-workspace)**.
