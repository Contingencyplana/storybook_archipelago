# Contributing to Storybook Archipelago

Thanks for supporting the archipelago. Keep changes tiny, testable, and aligned with the recursive 7‑step workflow.

## Prerequisites

- Python 3.12+
- pip
- ripgrep (`rg`) for the portal guard
- Git and VS Code (recommended)

## Setup

```pwsh
# From repo root
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -U pip
pip install -r requirements.txt
```

## Running tests and guards

Preferred via VS Code tasks:

- Test: repo root (pytest)
- Lint: disallow closed‑bracket portal tags (uses ripgrep). Use only the open form of the portal hint (the version without a closing bracket).
- Lint: disallow non-string returns (handlers/story)

CLI equivalents:

```pwsh
pytest -q
# For guards, prefer the provided VS Code tasks (they wrap platform‑specific details).
```

## Authoring workflow (7 tiny steps)

Follow `workflow.md`. Build one file at a time; pair each logic file with its test.

1) Planning → capture node intent and contracts.
2) Integration → `integration.py` routes "L"/"R"/other.
3) Camouflage → visual/mood overlay; no logic changes.
4) Orchestration → memory/state management.
5) Left → implement `leftmain.py` and `lefttest.py`.
6) Right → implement `rightmain.py` and `righttest.py`.
7) Story → implement `story.py` and `storytest.py`.

Minimum Tier‑1 slice before linking:

- Router handles L/R and default to story
- ≥1 side test passes
- `portalmap.md` uses four‑part paths

## Contracts and rules (must‑follow)

- Return‑value contract: see `docs/return_value_contract_v1.md`.
- Four‑part portal paths: see `portals_and_four_part_paths.md`.
- Story text must include "grove" and must not contain any portal tag.
- Left returns include token "[LEFT]"; Right returns include token "[RIGHT]".
- Portal tags: use only the open form of the portal hint (no closing bracket). The closed‑bracket form is forbidden and enforced by lint.

## Packaging

- Local: use the VS Code packaging task if provided, or `git archive --worktree-attributes`.
- CI: tag a commit (e.g., `v0.1.0`) to produce a clean ZIP artifact.

## Style and formatting

- `.editorconfig` defines whitespace and indentation. Do not fight it.
- Keep diffs focused; avoid mass reformatting unrelated files.

## Pull requests

- Keep PRs small and descriptive.
- Ensure tests and guards pass.
- Reference relevant nodes using four‑part paths when discussing portals.
