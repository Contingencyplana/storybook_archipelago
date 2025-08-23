# Bare Bones Skeletal of Text

## Philosophy

Storybook Archipelago is built from the inside out, starting with a minimal, text-first scaffold for every node and scene. This "bare bones" approach ensures that all logic, story, and player interaction is fully playable and testable from the start—while making it easy to add graphics, sound, and richer UI later, without rewriting core logic.

## Why This Matters

- **Future-Proof:** By labeling and structuring output (e.g., with [LEFT PAGE], [RIGHT PAGE], numbered lists, and illustration cues), we make it trivial to swap in visuals, audio, or new input modes later.
- **Testable:** All features are accessible and testable via text, supporting rapid iteration and robust CI.
- **Accessible:** The game is always playable in a terminal or basic UI, ensuring accessibility and broad compatibility.
- **Collaborative:** Writers, designers, and developers can work in parallel, knowing the text scaffold is the single source of truth.


## UI Alignment: Writing for Five Interaction Zones

When writing for Storybook Archipelago, keep these UI-driven authoring points in mind:

- Numbered lists = clickable options; keep between 3–6 items, one line each.
- Default click = page turn; when no numbered list is present, clicking the page should advance naturally.
- Paragraphs should be scannable; keep prose short and visually clean for readability in screenshot/storybook format.
- CLI keys (Enter, l, r, 1–3) are temporary stand-ins for these interactions during playtesting.

## Practical Guidelines

- Use explicit labels like `[LEFT PAGE]`, `[RIGHT PAGE]`, and content cues ("Illustration:", "Numbered list:") in all story and logic outputs.
- Keep prompts and help text minimal and consistent.
- Avoid hard-coding graphics or sound; instead, leave clear placeholders in the output.
- Structure all node files (integration, story, leftmain, rightmain, etc.) to support overlays and future enhancements.

## See Also
- Grand Plan (grand_plan.md)
- Template Minigame (a0_0_sailing_mode/template_minigame/README.md)
- Node Tiers (node_tiers.md)
- Storybook UI Playbook (docs/ui_storybook_playbook.md) — for detailed UI/UX, accessibility, and implementation guidance building on this text scaffold.

This approach is core to the project's doctrine and should be followed for all new nodes, minigames, and workspaces.
