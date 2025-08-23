# Testing & Playtest Protocol — Storybook Archipelago

**Status:** Draft v0.1 • Owner: Vision Holder • Last updated: 2025‑08‑23
**Purpose:** Define how we validate gameplay at two levels: fast CLI regression and later client click‑zone playtests.

---

## 1) CLI Regression Track (today)

**Goal:** Catch breakages fast; keep nodes/minigames stable during development.
**Tools:** `pytest`, node `integration.py`, minigame `playtest.py` (CLI harness).
**When to run:** On every node change; before commits; before tagging a minigame “playtest‑ready”.

### What to run (minimum)
- **Unit tests:** `pytest -q` (per node: `lefttest.py`, `righttest.py`, `storytest.py`, etc.)
- **Integration tests:** per node `integration.py` (manual prompt run acceptable)
- **Minigame harness:** `python playtest.py` at the minigame root to route across nodes

### Input mapping (CLI → intended client)
- `Enter` → click page (no numbered options present)
- `l` → click **Left Page** (Zone 1)
- `r` → click **Right Page** (Zone 3)
- `1/2/3` → click numbered options on the page
- `q` / `Ctrl+C` → click **Cover / Surround** (Zone 5 → Main Menu)

> See `docs/input_mapping.md` for the canonical table.

### Pass/Fail gates
- All node tests green (no skips)
- `integration.py` accepts `Enter`, `l`, `r` (and numbers if applicable) without errors
- Minigame `playtest.py` can route to each canonical node and return to menu cleanly

---

## 2) Client Click‑Zone Playtests (later)

**Goal:** Validate feel, usability, and pacing in the **storybook spread** UI.
**When:** After RS2 decision on Zones 2 & 4 jump behavior (random vs patterned).
**Who:** Vision Holder first; external playtesters later.

### Scope
- **Five Interaction Zones** (see `docs/ui_storybook_playbook.md`):
  1. Left Page (turn page unless numbered list)
  2. Left Page Edge — Bookmarks & Echo Jump
  3. Right Page (turn page unless numbered list)
  4. Right Page Edge — Bookmarks & Echo Jump
  5. Cover / Surround — Main Menu (pause/quit/options)

### Test checklist (per minigame)
- Bookmarks jump to correct destinations (per `portalmap.md`)
- Echo jump behavior matches mode (random vs patterned) and is documented
- Numbered list hit boxes trigger the intended routes
- Page clicks (no lists) always turn pages correctly
- Cover is always clickable to open Main Menu

---

## Documentation & Conventions

- **Portalmaps:** See `docs/portalmap_conventions.md` for bookmark & echo jump tagging.
- **Authoring guidance:** See `bare_bones_skeletal_of_text.md` (numbered options, scannable text).
- **UI metaphor:** See `grand_plan.md` (“Architecture Decision: Storybook Spread UI”).
- **Input mapping:** See `docs/input_mapping.md`.

---

## Reporting / Playtest Notes

- Each minigame keeps a `playtest.md` at its root with:
  - Date, build hash, tester, environment
  - Steps taken (inputs / clicks)
  - Observations (flow, confusion points, delight)
  - Issues with repro steps
  - Suggested tweaks to portalmap/bookmarks/echo seeds

---

## Exit Criteria (per minigame)

- CLI track: all tests green, harness navigable, no regressions
- Client track (when available): all five zones behave per spec; no dead‑ends; cover always accessible
- Playtest.md has at least one completed pass with actionable notes (or “no issues”)



Keep it light—stub level is fine.
