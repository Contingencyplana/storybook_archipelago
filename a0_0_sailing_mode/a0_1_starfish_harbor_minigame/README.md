# a0_1_starfish_harbor_minigame

A four-node stanza in sailing mode. Tier‑1 nodes with L/R traversal and narrative tied to the grove motif.

Nodes:

- a0_0_tide_grove_node (hub)
- a0_1_coral_quay_node
- a0_2_anchor_lane_node
- a0_3_beacon_jetty_node

Topology:

- tide_grove → L: coral_quay, R: anchor_lane
- coral_quay L → beacon_jetty
- anchor_lane R → beacon_jetty

Status: 51/51 tests passing.
