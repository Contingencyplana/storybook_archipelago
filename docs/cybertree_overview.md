<!-- Path: C:\Users\Admin\storybook_archipelago\docs\cybertree_overview.md -->

# Cybertree Overview (CLAIMVIG ↔ Storybook Archipelago)

**Status:** Draft v0.1 • **Owner:** Mark R. Gillam • **Last updated:** 2025-08-18

## TL;DR
CLAIMVIG’s “Towering Cybertree” grows as **hundreds of small, interconnected multiplayer games (“Cyberbranches”)**.  
The **first four cyberbranches** are:
1) Storybook Archipelago (cybernurse)  
2) Primordial Pool (cyberdoc)  
3) Storybook (game maker)  
4) FUN Factory (its test)

Each leaf adheres to a **Leaf Contract** and registers in a central **Cybertree Registry**. A lightweight **Trunk Router** dispatches players to leaves and stitches L/R portals between them. **Echoes** persist player-world marks.

## Scope v0.1
- **In-scope:** Leaf contract, registry, portals, echoes, trunk router spec; Tier-1 16-file node layout.
- **Out-of-scope (for now):** Economy, mod marketplace, rich 3D, anti-cheat, cross-shard identity.

## Architecture at a Glance
- **Leaf Contract:** `contracts/leaf_contract_v0_1.md` (maps cleanly to Tier-1 16 files)
- **Registry:** `registry/cybertree_registry.json` (source-of-truth for leaf IDs/portals)
- **Registry:** `registry/cybertree_registry.md` (holds JSON source-of-truth)
- **Protocols:** `protocols/portals_protocol.md`, `protocols/echoes_protocol.md`
- **Router:** `engine/trunk_router_spec.md` (loads leaf by ID, passes input/state)
- **Tier-1 Node Layout:** 16-file structure for routing, story, tests, portals, orchestration

## Definitions
- **Cyberleaf:** A self-contained multiplayer minigame node conforming to the Leaf Contract.  
- **Echoes:** Persistent, privacy-safe world marks (lantern lit, tree restored, etc.).  
- **Portal:** A canonical L/R (or numeric) link from one leaf to another.

## Success Criteria (v0.1)
- [ ] First 4 leaves registered and portal-linked
- [ ] Contract tests passing in each leaf (`integtest`, `storytest`, L/R tests)
- [ ] Echoes read/write path validated end-to-end
- [ ] Router dispatch + fallback behaviors verified

## Next Actions
- [ ] Finalize Leaf Contract v0.1
- [ ] Seed Registry with inaugural leaves
- [ ] Implement minimal Trunk Router + harness tests
- [ ] Wire Echoes v0.1 into `orchestration.py`

## Changelog
- v0.1: Initial skeleton
