# roadstanza_1.md — a0_0_sailing_mode

| Minigame Folder                 | Status        | Notes                                      |
|---------------------------------|---------------|--------------------------------------------|
| a1_0_tideline_market_minigame/  | Complete (T1) | Barter, shells, memory echoes              |
| a1_1_shell_bazaar_minigame/     | Complete (T1) | Spiral stalls, L/R traversal, recursive tone|
| a1_2_echoing_grotto_minigame/   | Incomplete    | Missing one node; not yet playtested       |
| a1_3_???_minigame/              | Pending       | Placeholder slot for fourth RS1 minigame   |


Policy alignment (see `node_type_rollout.md`).

## UI Mapping (Five Interaction Zones)

- **L / R** → left / right page turn.
- **Numbered options (1–3, etc.)** → in-page clickable choices.
- **Bookmarks (page edges)** → portalmap shortcuts or echoes.
- **Cover (surround)** → main menu (pause, quit, options, save/load).

Note: In CLI playtests, keys are placeholders for click zones:
Enter = click page (turn), L = left page, R = right page, 1/2/3 = numbered options, q/Ctrl+C = cover/menu.

## Notes

- RS1 is partially complete: first two minigames sealed, third incomplete, fourth pending.
- This file will be updated as Echoing Grotto and the fourth minigame progress.


## Gates to Introduce Next Type

Introduce a new Type only when all apply:

- Tests/guards are green for the prior stanza (L/R markers, portal guard).
- Portalmaps are activated and playtested without regressions.
- Clear player need for extra complexity (list on Left or Right).
- Matching tests exist:
  - Type 2: list assertions for Left paths

Policy alignment (see `node_type_rollout.md`).

---

## Notes

- RS1 is partially complete: first two minigames sealed, third incomplete, fourth pending.
- This file will be updated as Echoing Grotto and the fourth minigame progress.
