<!-- Path: C:\Users\Admin\storybook_archipelago\contracts\leaf_contract_v0_1.md -->

# Leaf Contract v0.1

**Engine compatibility:** ≥ 0.1.0  
**Contract goal:** Make every Cyberleaf **loadable, testable, and portal-safe** across the Cybertree.

## Interface Summary

### 1) Routing
- **Module:** `integration.py`
- **Entrypoint:** `route(input_event: dict, state: dict) -> dict`
- **Input (example):**

```jsonc
{ "key": "L" /* or "R" or 1..4 */, "meta": { "device": "kb" } }

{
  "screen": "string",
  "options": { "L": ["string"], "R": ["string"], "numbers": ["string"] },
  "effects": [ { "type": "echo" /* or "fx" */, "payload": {} } ],
  "next_leaf": null, // or "string"
  "state": {} // JSON-serializable
}
```

## 2) Story Layer

- **Module:** `story.py`
- **Exports:**
  - `DESCRIPTION: str`
  - `OPTIONS_L: list[str]`
  - `OPTIONS_R: list[str]`

---

## 3) Portals

- **Doc:** `portalmap.md`
- **Requirement:** Declare canonical **L/R** (and optional **numeric**) targets by `leaf_id`.

---

## 4) Echoes (World Marks)

- **Module:** `orchestration.py`
- **Functions:**
  - `emit_echo(kind: str, payload: dict, state: dict) -> dict`
  - `read_echoes(filters: dict) -> list[dict]`

---

## 5) Camouflage (Optional, Pure)

- **Module:** `camouflage.py`
- **Constraint:** Pure functions only (no global I/O).

---

## Required Tests (per Tier-1 leaf)

- `integtest.py::test_contract_route_signature`
- `storytest.py::test_options_sync_with_route`
- `lefttest.py::test_left_paths_exist`
- `righttest.py::test_right_paths_exist`
- `camoutest.py::test_camouflage_hooks_pure`

---

## Tier-1 16-File Compliance Checklist

- [ ] `__init__.py`
- [ ] `README.md`
- [ ] `integration.py` / `integtest.py`
- [ ] `camouflage.py` / `camoutest.py`
- [ ] `orchestration.py` / `orchtest.py`
- [ ] `leftmain.py` / `lefttest.py`
- [ ] `rightmain.py` / `righttest.py`
- [ ] `story.py` / `storytest.py`
- [ ] `portalmap.md`
- [ ] `subtaskmap.md`

---

## Error Handling

- On invalid key: return frame with `"next_leaf": null`, include a friendly `"screen"` hint.
- On missing portal: fallback to router default leaf; log a soft error.

---

## Versioning

- Contract increments (0.1 → 0.2) must include a migration note and a compatibility table.

---

## Notes

- State must be JSON-serializable.
- Leave PII out of Echo payloads (see **Echoes Protocol**).
