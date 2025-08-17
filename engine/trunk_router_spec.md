<!-- Path: C:\Users\Admin\storybook_archipelago\engine\trunk_router_spec.md -->

# Trunk Router Spec v0.1

**Purpose:** Load a leaf by ID, forward input/state, return a **frame**; enforce fallbacks and contract checks.  
**Status:** Draft v0.1 • **Owner:** Mark R. Gillam • **Last updated:** 2025-08-18

---

## 1) Public API (Python)

~~~python
def load_leaf(leaf_id: str):
    """
    Import/resolve the leaf module(s) for `leaf_id`.
    Validate required entrypoints and cache handles for dispatch.
    Raises ImportError/ValueError on hard violations in dev.
    """

def dispatch(leaf_id: str, input_event: dict, state: dict) -> dict:
    """
    Route an input event to a leaf’s integration entrypoint.
    Returns a frame dict (see Frame Contract).
    Applies registry overrides, portal resolution, and fallbacks.
    """

def default_leaf_id() -> str:
    """
    Returns the engine-wide default leaf_id for fallback routing.
    """
~~~

---

## 2) Frame Contract (returned by `dispatch`)

~~~jsonc
{
  "screen": "string",
  "options": { "L": ["string"], "R": ["string"], "numbers": ["string"] },
  "effects": [ { "type": "echo" /* or "fx" */, "payload": {} } ],
  "next_leaf": null, // or "string"
  "state": {} // JSON-serializable
}
~~~

- `screen` is human-readable.
- `options` must align with `story.py` exports and portal mappings.
- `effects` are pass-through; the router does not mutate effect payloads.
- `next_leaf` (if provided) must be a valid `leaf_id` or will trigger fallback.

---

## 3) Behavior

1. **Load & Verify**
   - `load_leaf` imports the leaf, asserts the integration entrypoint:
     - `integration.route(input_event: dict, state: dict) -> dict`
   - Optional checks: presence of `story.py` exports and `portalmap.md` (advisory).

2. **Dispatch**
   - Call `integration.route(...)` with the provided `input_event` and `state`.
   - Validate that the returned object satisfies the **Frame Contract** (shape only).

3. **Portal Resolution**
   - If `frame.next_leaf` is set:
     - Verify against `registry/cybertree_registry.json`.
     - If missing/invalid: soft-log and replace with `default_leaf_id()`.

4. **Error Handling**
   - Contract violations in dev: raise with clear message.
   - In prod: return an **error frame** and route to `default_leaf_id()`.

---

## 4) Error Frame (engine-generated)

~~~jsonc
{
  "screen": "An error occurred. Returning to a safe harbor.",
  "options": { "L": [], "R": [], "numbers": [] },
  "effects": [],
  "next_leaf": "<default-leaf-id>",
  "state": {}
}
~~~

---

## 5) Minimal Test Matrix

- [ ] Unknown leaf → **routes to** `default_leaf_id()`.
- [ ] Valid L/R transition → **loads** target leaf (per registry).
- [ ] Contract violation (bad frame shape) → **error frame** + fallback.
- [ ] State roundtrip remains **JSON-serializable**.
- [ ] Echo `effects` are **passed through unchanged**.

---

## 6) Integration with Registry & Protocols

- Source of truth for portals: `registry/cybertree_registry.json` (validated in CI).
- Local author intent: `portalmap.md` (documentation; may be overridden by registry).
- Echo handling per: `protocols/echoes_protocol.md`.

---

## 7) Operational Notes

- **Dev hot-reload:** Allow module reload on change; clear router cache.
- **Prod stability:** Use a static import map and pinned registry snapshot.
- **Logging:** Soft errors for portal resolution; hard errors only for router invariants.
- **Metrics (optional):** per-leaf loads, dispatch latency, error counts.

---

## 8) Roadmap (post-v0.1)

- Pluggable stores for Echoes/Identity.
- Sandboxed leaf execution hooks.
- Session/origin metadata passthrough.
- Structured diagnostics frames for UI-rich error reporting.
