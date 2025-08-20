
# 🌌 Portal Map — Echoing Grotto Minigame

**Status:** Draft v0.2 • **Owner:** Mark R. Gillam • **Last updated:** 2025-08-19  
**Purpose:** Define L/R traversal routes between the Echoing Grotto’s nodes.  

---

## Node Index
- `a0_0_resonant_entry_node`
- `a0_1_chamber_of_reflections_node`
- `a0_2_whispering_arch_node` ← **new**
- `a0_3_tbd_node` (placeholder for final stanza slot)

---

## Portals

### `a0_0_resonant_entry_node`
- **L →** Chamber of Reflections (`a0_1_chamber_of_reflections_node`)  
- **R →** Whispering Arch (`a0_2_whispering_arch_node`)  

---

### `a0_1_chamber_of_reflections_node`
- **L →** Whispering Arch (`a0_2_whispering_arch_node`)  
- **R →** *TBD (connect once a0_3 is defined)*  

---


## Whispering Arch (a0_2)

- **L ** `TBD_next_node_left`  <!-- placeholder -->
- **R ** `TBD_next_node_right` <!-- placeholder -->

_These anchors are placeholders and will be bound once the next node (a0_3_...) is selected._

---

### `a0_3_tbd_node`
- **L →** *TBD*  
- **R →** *TBD*  

---

## Notes
- Whispering Arch is scaffolded with **L/R exits as placeholders**.  
- Once the fourth node (`a0_3`) is named, patch the connections so traversal closes the stanza loop.  
- Echo recursion theme: each node should offer one “forward echo” (progression) and one “return whisper” (loopback).  
