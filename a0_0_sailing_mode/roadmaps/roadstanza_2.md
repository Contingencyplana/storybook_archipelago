# roadstanza_2.md — a0_0_sailing_mode

Roadstanza 2 (RS2) planning stub.

| Minigame Folder                 | Status        | Notes                             |
|---------------------------------|---------------|-----------------------------------|

## Recommended Staging

- Roadstanza 2 (RS3 – minigames 9–12): Type 1–3 (introduce Type 3: Right list) sparingly

### Suggested ratios (guideline)

- RS2: ~60% Type 1, ~25% Type 2, ~15% Type 3

## Gates to Introduce Next Type

Introduce a new Type only when all apply:

- Tests/guards are green for the prior stanza (L/R markers, portal guard).
- Portalmaps are activated and playtested without regressions.
- Clear player need for extra complexity (list on Left or Right).
- Matching tests exist:
  - Type 2: list assertions for Left paths
  - Type 3: list assertions for Right paths

Policy alignment (see `node_type_rollout.md`)

Checklist (to be expanded when RS3 starts):

- [ ] Select minigame 5 theme
- [ ] Scaffold Tier‑1 nodes (Type 1 baseline)
- [ ] Introduce Type‑2 asymmetry on Left for selected nodes
- [ ] Add tests asserting numbered list cue (e.g., "1) on Right paths
- [ ] Keep portals Pending until tests green; then activate
