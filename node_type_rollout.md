# Node Type Rollout (Tier‑1 Subtypes)

Purpose: outline a safe, test-first rollout of Tier‑1 subtypes (Type 1–4) across the first four roadstanzas. This guides pacing without changing canon.

Key: This doc concerns Tier‑1 subtypes only. Tier 2–3 nodes are AI‑generated per `node_tiers.md` and are not part of this rollout.

---

## Recommended Staging

- Roadstanza 0 (RS0 – minigames 1–4): Type 1 only (no lists)
- Roadstanza 1 (RS1 – minigames 5–8): Type 1 + limited Type 2 (Left list)
- Roadstanza 2 (RS2 – minigames 9–12): Type 1–3 (introduce Type 3: Right list) sparingly
- Roadstanza 3 (RS3 – minigames 13–16): Type 1–4; Type 4 rare, only after strong telemetry

### Suggested ratios (guideline)

- RS0: 100% Type 1
- RS1: ~70–80% Type 1, ~20–30% Type 2
- RS2: ~60% Type 1, ~25% Type 2, ~15% Type 3
- RS3: ~50% Type 1, ~30% Type 2, ~15% Type 3, ~5% Type 4

---

## Gates to Introduce Next Type

Introduce a new Type only when all apply:

- Tests/guards are green for the prior stanza (L/R markers, portal guard).
- Portalmaps are activated and playtested without regressions.
- Clear player need for extra complexity (list on Left or Right).
- Matching tests exist:
  - Type 2: list assertions for Left paths
  - Type 3: list assertions for Right paths
  - Type 4: list assertions for both sides

---

## Notes

- Keep Type 4 uncommon. Use it for deliberate spikes in agency/complexity.
- Do not embed closed‑bracket portal tags in Markdown; hint only in runtime strings.
- Align node subtype labeling in `subtaskmap.md` (e.g., `subtype: type_1`).
- Current status: Fogbound Sound (minigame 4, RS1) remains `subtype: type_1` across all nodes.
- If telemetry shows confusion or churn, shift back toward Type 1.

---

References: `tier_1_minigame_node_structure.md`, `node_tiers.md`, `workflow.md`, `test_strategy.md`, `rhyme_and_reason.md`.
