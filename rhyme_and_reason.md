# Rhyme and Reason

A compact “why” guide for this repo. It ties together our guardrails, tiers, stanza taxonomy, and the tiny‑steps workflow so contributors can move fast and keep the world coherent.


## Why guardrails exist

- Keep strings human‑readable and stable for tests. See: docs/return_value_contract_v1.md, test_strategy.md.
- Prevent accidental portal activation in docs. We only allow the open tag form in code output, never closed‑bracket examples in Markdown.
- Make CI failure modes obvious and local: fast ripgrep checks catch issues before deep tests.

What this means in practice

- Handlers and story return plain strings (no dict/list/json.dumps).
- Markdown must not contain closed‑bracket portal tags. If you need to refer to the token, describe it in words instead of pasting it literally.


## Why tiers and stanza taxonomy

- Tiers set small, testable caps for each node (what files exist, what they promise). See: node_tiers.md.
- Stanzas scale the world in rhythmic quads: nodestanza (nodes), roadstanza (minigames), mirrorstanza (modes). See: conventions.md, planning_spaces.md.
- Tiny slices reduce cognitive load and keep play loops shippable.


## Why four‑part paths

- Paths are our addressing scheme: {workspace}/{mode}/{minigame}/{node}/
- They prevent ambiguity and enable cross‑workspace links safely. See: portals_and_four_part_paths.md and workspace_registry.md.


## Why the 7‑step workflow

- Recursion with rails. The workflow creates a minimal, playable slice first, then layers mood and memory. See: workflow.md.
- Order matters: Planning → Integration → Camouflage → Orchestration → Left → Right → Story.
- Each logic file pairs with a test; green tests unlock the next step.


## Why the tests and tasks

- Pytest keeps behavior deterministic.
- Repository tasks enforce rules fast:
  - Test: repo root (pytest)
  - Lint: disallow closed‑bracket portal tags in Markdown
  - Lint: disallow non‑string returns in handlers/story


## Why packaging and CI

- Clean artifacts via export‑ignore ensure we ship only what’s needed.
- Tag‑driven packaging makes releases predictable and reproducible.


## Rules of thumb

- Prefer smallest viable slice that can pass tests today.
- Link with four‑part paths; only activate a portal when both ends are ready.
- Keep presentation (camouflage) separate from logic and memory.
- When in doubt, add a tiny test before adding code.


## Quick pointers

- Contract: docs/return_value_contract_v1.md
- Pathing: portals_and_four_part_paths.md
- Tiers: node_tiers.md
- Workflow: workflow.md
- Testing: test_strategy.md
- Planning: planning_spaces.md, conventions.md


## Scope and non‑goals

- This page explains the intent; canonical rules live in the referenced docs.
- If this page and a canonical doc disagree, the canonical doc wins.
