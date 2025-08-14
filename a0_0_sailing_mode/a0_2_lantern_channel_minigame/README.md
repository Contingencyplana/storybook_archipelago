# a0_2_lantern_channel_minigame

Theme: A twilight passage strung with drifting lanterns and bioluminescent wakes. You thread between a submerged kelp grove and open chop; bells and foghorns cue pace. L/R choices play as narrow lit path vs. darker current.

Current nodes (Tier‑1)

- a0_0_lantern_pass_node — entry
- a0_1_braided_seam_node
- a0_2_count_of_light_node
- a0_3_tolling_gate_node (Active)
- a1_0_still_pool_node (Active)
- a1_1_open_chop_node (Active)
- a1_2_crescent_moor_node (Active)
- a1_3_shoal_bend_node (Active)

Quick links

- taskmaps/nodestanza_0.md — nodes a0_0 to a0_3
- taskmaps/nodestanza_1.md — nodes a1_0 to a1_3

Active loop (four‑part paths)

- still_pool L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_1_open_chop_node/
- still_pool R → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_2_crescent_moor_node/
- open_chop R → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_0_still_pool_node/
- crescent_moor L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_0_still_pool_node/
- open_chop L ↔ crescent_moor R (reciprocal)

Ingress (four‑part paths)

- tolling_gate L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_3_shoal_bend_node/
- count_of_light L → storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_3_shoal_bend_node/

Node index (four‑part paths)

- a0_0_lantern_pass_node — entry; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a0_0_lantern_pass_node/`
- a0_1_braided_seam_node — early weave/branch; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a0_1_braided_seam_node/`
- a0_2_count_of_light_node — ingress split; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a0_2_count_of_light_node/`
- a0_3_tolling_gate_node — ingress bell/gate; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a0_3_tolling_gate_node/`
- a1_0_still_pool_node — calm loop anchor; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_0_still_pool_node/`
- a1_1_open_chop_node — exposed water; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_1_open_chop_node/`
- a1_2_crescent_moor_node — lee/mooring arc; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_2_crescent_moor_node/`
- a1_3_shoal_bend_node — turn‑in to loop; `storybook_archipelago/a0_0_sailing_mode/a0_2_lantern_channel_minigame/a1_3_shoal_bend_node/`

Conventions

- Four‑part relative paths only; no OS‑absolute paths
- Handlers/story return strings (see return_value_contract_v1)
