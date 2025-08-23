# Storybook UI Playbook

Guidance for the L/R page‑turn UI used across modes/minigames. Keep strings stable for tests; presentation adds delight without breaking contracts.

## Inputs

- Primary: keyboard L/R arrows; secondary: A/D; tertiary: on‑screen buttons (Left/Right). Accept lowercase/uppercase 'l'/'r' for CLI tools.
- Remapping: allow optional key remap; persist per browser/device (localStorage), resettable.
- Redundancy: click/tap anywhere left/right third of the page triggers L/R; buttons remain for explicit affordance.
- Debounce: 250ms guard between turns; ignore repeated keydown while held.

- Behavior notes: Enter shows scene (look/recap). L/R are case‑insensitive. Ctrl+C exits in CLI tools only. Numeric keys are preview‑only in CLI; not actionable in web UI (click/tap list items instead).

## Layout (numbered choices)

- Single column if ≤5 items; two columns when >5 with balanced counts (left column favors one extra when odd).
- Maintain consistent item numbering across columns (1..N left-to-right, top-to-bottom).
- Reserve bottom‑center for L/R controls; ensure focus/aria order follows visual order.

## Accessibility

- Keyboard: all actionable controls reachable via Tab; Enter/Space activates focused control.
- Screen readers: announce current scene first, then choices; use aria-live="polite" for scene text updates.
- Focus management: move focus to scene heading on page‑turn; respect user’s prior focus when returning.
- Reduced motion: honor prefers-reduced-motion and fall back to cross‑fade (no slide) and zero parallax.
- Contrast: WCAG AA minimum; buttons 44x44 CSS px target size.

## Animation

- Default page‑turn: 250–300ms slide + slight opacity fade; easing: cubic-bezier(0.22, 0.61, 0.36, 1).
- Input feedback: brief (120ms) button press scale/ink; disable during transition to avoid double turns.
- Sound (optional): subtle rustle click; off by default; user-toggle remembered.

## Localization & RTL

- Use i18n keys for UI chrome; narrative strings come from content files unchanged.
- RTL: mirror layout and page‑turn direction; L remains logical "previous" and R "next" in controls and tests.
- Fonts: load locale‑appropriate fallback stack; avoid layout shift by preloading metrics where possible.

## Performance

- Prefetch next/prev node assets on idle using portalmap hints; cap to 2 parallel fetches.
- Defer non-critical animations until after first paint; avoid blocking fonts.
- Cache story text per node in-memory for quick back/forward.

## Testing hooks

- Rendering should hide internal markers but keep them present in DOM data attributes when needed:
  - Strip "[LEFT]"/"[RIGHT]" from visible text; expose data-left/right="true" on the choice elements.
  - Do not render "[PORTAL:" tags; use portalmap files to drive navigation.
- Add data-scene="true" on the scene container; data-choice-index="n" on each choice for deterministic E2E.

- Add data-page="left"/"right" on the page containers to mirror the explicit "[LEFT PAGE]"/"[RIGHT PAGE]" labels used in CLI previews.

See also:
- docs/ui_hooks_example.md for minimal JS/React and Python snippets.
- VS Code task: "Run: render choices demo" to print an annotated HTML list quickly.
- [Bare Bones Skeletal of Text](../bare_bones_skeletal_of_text.md) — for the philosophy and contract of text-first scaffolding that underpins this UI playbook.

## Five Interaction Zones (Top-Down Storybook UI)

The canonical client UI for Storybook Archipelago is a top-down view of an open storybook, with visible bookmarked page edges and a surrounding cover. This creates five consistent interaction zones:

### Zone One — Left Page
- **Default:** Clicking turns the left page.
- **If numbered list is present:** Clicking a list item chooses that option instead of turning.

### Zone Two — Left Page Edge (Bookmarks)
- A swatch of bookmarked page ends is visible left of the left page (~100 implied).
- **Click bookmark:** Jumps directly to that bookmarked screenshot.
- **Click elsewhere:** Jumps to one of 100 locations (acts as a memory echo).

### Zone Three — Right Page
- **Default:** Clicking turns the right page.
- **If numbered list is present:** Clicking a list item chooses that option instead of turning.

### Zone Four — Right Page Edge (Bookmarks)
- Same rules as Zone Two, but on the right side.
- **Bookmark click:** Direct jump.
- **Elsewhere:** Echo jump to one of 100 locations.

### Zone Five — Storybook Cover (Surround)
- The visible hard cover around the page spread.
- Clicking it opens the Main Menu (pause, quit, options, save/load).
- Can be styled as a closed book on a desk, with a parchment note of menu choices beside it.

---

### Notes
- **Diegetic UI:** All controls exist “in-world,” preserving immersion.
- **Consistency:** Identical rules left vs right.
- **Expandability:** Bookmarks double as save states, quick travel, or echo anchors.
- **Fail-safe:** The cover zone always offers a clean menu exit.

### CLI Mapping (temporary for playtesting)
- `Enter` → click page (no numbered list present).
- `l` → click left page.
- `r` → click right page.
- `1/2/3` → click numbered list options.
- `q` or `Ctrl+C` → click cover (menu).

⚖️ **Open Question:** For Zones 2 & 4 (“click elsewhere” on page edges), should jumps be:
- Truly random (dreamlike, chaotic), or
- Patterned/seeded by memory echoes (bounded but still surprising)?

Decision deferred until **end of RS2**.

## Out-of-scope (for this doc)

- Narrative authoring rules and portal contract details (see portals_and_four_part_paths.md and tests).
