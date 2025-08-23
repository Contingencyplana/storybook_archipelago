# Input Mapping — CLI ↔ Storybook Client (Five Zones)

**Status:** Draft v0.1 • Purpose: Keep keyboard-based playtests aligned with the eventual click-based client UI.

This table maps our current CLI test inputs to the future Storybook “Five Interaction Zones”:

| CLI Input     | Client Action                           | Zone | Notes |
|---------------|-----------------------------------------|------|-------|
| **Enter**     | Click page (no numbered options present) | 1/3  | Defaults to a page turn: Left Page (Zone 1) or Right Page (Zone 3), depending on context in the client. In CLI tests, `Enter` is treated as a “continue/turn page” action. |
| **l**         | Click **Left Page**                      | 1    | Forces a Left Page interaction (e.g., turn-left or left-specific behavior). |
| **r**         | Click **Right Page**                     | 3    | Forces a Right Page interaction (e.g., turn-right or right-specific behavior). |
| **1 / 2 / 3** | Click numbered option on the page        | 1/3  | When the page presents a numbered list of choices; each digit selects its corresponding item. |
| **q**         | Click **Cover / Surround** → Main Menu   | 5    | Opens pause/quit/options in the diegetic cover area. |
| **Ctrl+C**    | Emergency exit                           | 5    | CLI-only hard exit; conceptually equivalent to clicking the cover/menu. |

> Zones reference: See **docs/ui_storybook_playbook.md** (“Five Interaction Zones”).
> - **Zone 1:** Left Page
> - **Zone 2:** Left Page Edge (Bookmarks / Echo Jump)
> - **Zone 3:** Right Page
> - **Zone 4:** Right Page Edge (Bookmarks / Echo Jump)
> - **Zone 5:** Cover / Surround (Main Menu)

## Notes & Conventions

- **Numbered lists take precedence**: If a page shows a numbered list, clicking that number (or pressing `1/2/3` in CLI) selects the option rather than turning the page.
- **Page edges (Zones 2 & 4)** are not represented in CLI mappings; they’ll be validated in client click‑zone playtests:
  - Bookmark click → direct jump.
  - Non‑bookmark click → **Echo Jump** (random vs patterned TBD).
- **Playtest docs**: `docs/testing_playtest_protocol.md` defines two tracks (CLI regression today, client click‑zone later).
- **Architecture**: The storybook spread is the primary UI metaphor (see **grand_plan.md**, “Architecture Decision: Storybook Spread UI”).


