# Grand Plan — Build-from-Inside Strategy

Purpose: Codify how we progressively build Storybook Archipelago from within the game while phasing AI assistance down over time.

## Core stance

- Build the game increasingly from inside the game. External AI (agent) scaffolds early; player-facing tools and nodes take over.
- Keep changes tiny and testable (Tier‑1 first). Promote complexity only when playtests demand it.

## Workspace model (camouflage layers)

- Ten camouflage layers map to ten workspaces over time, plus one client (frontend) workspace players download (≈ 11 total).
- Optional later: integration/high_command workspaces if coordination pressure appears.
- Each camouflage workspace both (a) forges the next layer and (b) updates the client.

## Staging and gates

Spin up a new workspace only when all gates pass:

1) Tier‑1 slice green in the current workspace (routing, L/R, story, camouflage, orchestration tests).
2) Cross‑workspace policies in place:
   - Four‑part paths only; target workspace listed in `workspace_registry.md`.
   - Portals that leave a minigame remain Pending until the destination exists and passes tests.
3) CI guards active: portal‑marker guard and non‑string‑return guard.
4) Packaging path exists (e.g., clean ZIP on tag) for reproducible handoffs.

## Build‑from‑inside mechanics

- Provide in‑game builder nodes/tools (start simple):
  - Node routers, tiny editors, and test triggers exposed as scenes.
  - Memory/state via orchestration to carry intent across steps.
- Keep contracts human‑readable strings; avoid binary/stateful surprises.

## Risks and mitigations

- Fragmentation across workspaces → Mitigate with a single registry, four‑part paths, and a worldmap.
- Version skew between layers and client → Package on tag; treat client as an artifact of the current stable layer.
- Scope creep → Enforce Tier‑1 discipline and staged subtype rollout; defer Tier‑2/3 until needed.

## Near‑term plan

1) Ship the first minigame with one nodestanza (4 nodes) in `storybook_archipelago/`.
2) Playtest; fix tone/flow. Add a second nodestanza only if needed.
3) Define readiness criteria to spawn Camouflage Layer 1 workspace; update `workspace_registry.md` accordingly.
4) Keep portals that cross workspaces Pending until destinations are real and green.

References: `camouflage_layers.md`, `return_value_contract_v1.md`, `portals_and_four_part_paths.md`, `node_tiers.md`, `tier_1_minigame_node_structure.md`, `node_type_rollout.md`.

---

## Success criteria

- Definition of Ready (per layer): Tier‑1 slice green; external portals Pending; clean ZIP on tag.
- Definition of Done (per stanza): first nodestanza playtested; README/docs updated; worldmap entry added.

## Release and versioning

- Tag format: `vA.B.C` (A = mode wave, B = stanza, C = fix).
- Artifact name: `<repo>-<tag>.zip` (emitted by the package‑on‑tag workflow).

## Playtest loop

- Cadence: per node (1–2 min), per stanza smoke (5–8 min).
- Signals: scene includes "grove"; `[LEFT]`/`[RIGHT]` markers present; no `[PORTAL:` in story; tone notes captured.

See: `testplayers.md` for who/when to invite and readiness gates.

## Builder scope

- Now: route creation, edit `story.py` text, trigger tests, mark portals Pending, page previews ("[LEFT PAGE]"/"[RIGHT PAGE]"), and numbered lists as preview content only.
- Later: numeric selection (post‑Tier‑1), scaffold new nodes, cross‑workspace promotions.

## Tier‑1 page UX policy (Type‑1..4)

- Inputs: Enter shows the scene via `story.describe_scene` (look/recap). L triggers Left, R triggers Right. Numeric keys (1–9) are preview‑only; they do not select. Hint: "Numbers preview only; use L/R or Enter."
- Page previews: Always label pages explicitly as "[LEFT PAGE]" and "[RIGHT PAGE]" for accessibility.
  - Type‑1: illustrations/text on both sides (no lists).
  - Type‑2: numbered list on Left above text; Right shows illustration/text. Detect list items permissively: `1)`, `1.`, or `1-`. Keep lists small (≈3–6 items).
  - Type‑3: mirror of Type‑2 (numbered list on Right).
  - Type‑4: numbered lists on both sides (use sparingly at Tier‑1).
- Error handling: On unknown input, print a compact one‑time help line per session.
- Telemetry: In the playtester, track frequency of numeric presses and Enter vs L/R to inform if/when numeric selection should be enabled later.
- Pause/Save: Reserve Esc/P for future Pause/Save UI; do not bind to Enter at Tier‑1.

## Rollback and anomalies

- On failure: revert to last tag; quarantine broken node; log in `milestones.md`; see `recursive_anomaly_protocol.md`.

## Workspace lifecycle

- Add to `workspace_registry.md` when created.
- Activate cross‑workspace portals only after the destination exists and passes tests.

## Metrics (lightweight)

- Fun/flow: avg loops to boredom; percent of choices reread.
- Technical: test pass rate; time‑to‑green after edit; artifact size.

## Non‑goals (now)

- No secret/network calls from in‑game builder.
- No Tier‑2/3 capabilities until Tier‑1 Subtypes 1–2 are stable.
