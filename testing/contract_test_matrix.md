<!-- Path: C:\Users\Admin\storybook_archipelago\testing\contract_test_matrix.md -->

# Contract Test Matrix (Tier-1 Leaves)

**Status:** Draft v0.1 • **Owner:** Mark R. Gillam • **Last updated:** 2025-08-18  
**Purpose:** Define the **must-pass** tests for every Tier-1 leaf so behavior stays consistent across the Cybertree as content scales.

---

## 1) Scope

- **Applies to:** All Tier-1 leaves using the 16-file layout and `leaf_contract_v0_1.md`.
- **Guarantees:** Frame shape, portal integrity, option alignment, echo behavior, and purity constraints.
- **Enforced by CI:** Build fails if any required test is **missing** or **failing**.

---

## 2) Must-Pass Test List (by interface)

| Interface | Test name (pytest::node) | Why it exists |
|---|---|---|
| **Routing / Contract** | `integtest.py::test_contract_route_signature` | `integration.route(input_event, state)` exists & callable with dicts. |
| **Frame shape** | `integtest.py::test_frame_contract_shape` | Returned object matches Frame Contract keys/types. |
| **Story alignment** | `storytest.py::test_options_sync_with_route` | `OPTIONS_L/OPTIONS_R` align with `frame.options`. |
| **Left path** | `lefttest.py::test_left_paths_exist` | L-side options resolve to valid branches/leaf transitions. |
| **Right path** | `righttest.py::test_right_paths_exist` | R-side options resolve to valid branches/leaf transitions. |
| **Portals** | `integtest.py::test_portals_exist_in_registry` | Any `next_leaf` or portal target exists in registry. |
| **Echoes** | `orchtest.py::test_emit_echo_idempotent` | Duplicate `idempotency_key` does not create duplicates. |
| **Echoes filters** | `orchtest.py::test_read_echoes_filters` | Filters by kind/leaf/time behave as expected. |
| **Camouflage purity** | `camoutest.py::test_camouflage_hooks_pure` | `camouflage.py` functions are pure (no global I/O). |
| **State roundtrip** | `integtest.py::test_state_is_json_serializable` | `state` remains JSON-serializable through dispatch. |

> **Note:** You may add more tests per leaf, but these names must exist and pass.

---

## 3) File-to-Test Coverage Map (Tier-1: 16-file layout)

| File(s) | Covered primarily by |
|---|---|
| `integration.py` | route signature • frame shape • portals existence • state roundtrip |
| `story.py` | options sync with route |
| `leftmain.py` | left paths exist |
| `rightmain.py` | right paths exist |
| `orchestration.py` | echo idempotency • echo filters |
| `camouflage.py` | camouflage purity |
| `portalmap.md` | portals exist in registry (advisory vs. runtime registry) |
| `README.md`, `subtaskmap.md`, tests themselves | out of scope for contract; lint/docs checks optional |

---

## 4) Minimal Assertions (what each test must prove)

- **Route signature:** callable, accepts `{ "key": ..., "meta": ... }`, returns a dict.
- **Frame contract:** has keys `screen`, `options{L,R,numbers}`, `effects[]`, `next_leaf (str|null)`, `state (dict)`.
- **Options sync:** `story.OPTIONS_L/OPTIONS_R` length and labels align with `frame.options`.
- **Portals valid:** Any `next_leaf` or registry portal target resolves to a known `leaf_id`.
- **Echoes:** Duplicate `idempotency_key` → no new record; filters respect `kind/leaf_id/since_ts`.
- **Purity:** Camouflage hooks don’t touch filesystem, network, globals.
- **State:** JSON-serializable after dispatch.

---

## 5) Naming & Markers

- **Test names:** keep **exact** names from §2 (CI checks them literally).
- Optional marker for contract tests:
~~~python
# conftest.py
import pytest
def pytest_configure(config):
    config.addinivalue_line("markers", "contract: required contract tests")

# example
@pytest.mark.contract
def test_frame_contract_shape(): ...
~~~

---

## 6) CI Gate (hard requirements)

- Fail build if:
  - Any required test **node name** is missing.
  - Any required test **fails**.
  - Registry JSON fails schema validation (see `registry/cybertree_registry.md`).

- Suggested command:
~~~powershell
# From repo root
python -m pytest -q --maxfail=1
~~~

---

## 7) Example Scaffolds (copy into each leaf test file)

~~~python
# integtest.py
from typing import Dict, Any
import json

def test_contract_route_signature():
    import integration
    assert hasattr(integration, "route")
    frame = integration.route({"key": "L", "meta": {}}, {})
    assert isinstance(frame, dict)

def test_frame_contract_shape():
    import integration
    frame = integration.route({"key": "L", "meta": {}}, {})
    for k in ["screen", "options", "effects", "next_leaf", "state"]:
        assert k in frame
    assert isinstance(frame["options"], dict)
    assert all(k in frame["options"] for k in ["L","R","numbers"])
    # JSON-serializable state
    json.dumps(frame["state"])

def test_portals_exist_in_registry():
    # Pseudocode: validate next_leaf or registry links exist.
    pass

def test_state_is_json_serializable():
    import integration, json as _json
    frame = integration.route({"key": "R", "meta": {}}, {})
    _json.dumps(frame["state"])
~~~

~~~python
# storytest.py
import story, integration

def test_options_sync_with_route():
    frame = integration.route({"key": "L", "meta": {}}, {})
    assert isinstance(story.OPTIONS_L, list)
    assert isinstance(story.OPTIONS_R, list)
    assert len(frame["options"]["L"]) == len(story.OPTIONS_L)
    assert len(frame["options"]["R"]) == len(story.OPTIONS_R)
~~~

~~~python
# lefttest.py
import integration
def test_left_paths_exist():
    frame = integration.route({"key": "L", "meta": {}}, {})
    assert "L" in frame["options"]
    # Additional assertions per leaf specifics
~~~

~~~python
# righttest.py
import integration
def test_right_paths_exist():
    frame = integration.route({"key": "R", "meta": {}}, {})
    assert "R" in frame["options"]
~~~

~~~python
# orchtest.py
def test_emit_echo_idempotent():
    # Arrange → emit once, emit again with same idempotency_key → count unchanged.
    pass

def test_read_echoes_filters():
    # Arrange → write few echoes → query with filters → results match.
    pass
~~~

~~~python
# camoutest.py
def test_camouflage_hooks_pure():
    # Call camouflage hooks and assert no global side effects.
    pass
~~~

---

## 8) Versioning the Matrix

- **v0.1:** Names above are frozen.  
- New required tests will bump this file to **v0.2** and include a migration note.

---

## 9) Migration Note (placeholder)

- _None yet._ When adding tests, document the reason, impact, and how to update leaves.

---

## Changelog
- v0.1 — Initial matrix aligned to `leaf_contract_v0_1.md` & `trunk_router_spec.md`.
