<!-- Path: C:\Users\Admin\storybook_archipelago\protocols\echoes_protocol.md -->

# Echoes Protocol v0.1 (World Marks)

**Purpose:** Persist lightweight, privacy-safe **marks** left by players (e.g., lantern lit, tree restored) so leaves can reflect shared history.  
**Status:** Draft v0.1 • **Owner:** Mark R. Gillam • **Last updated:** 2025-08-18

---

## 1) Scope

- **In-scope:** API (emit/read), record schema, idempotency & dedupe, retention/TTL, privacy, validation, tests.
- **Out-of-scope (v0.1):** Federation across shards, moderation tooling, analytics, economy hooks.

---

## 2) Glossary

- **Echo:** A small, append-only record describing a persistent world mark.
- **Leaf:** A minigame node identified by canonical `leaf_id`.
- **Actor:** The pseudonymous player identity; stored as a non-reversible hash.

---

## 3) Leaf-side API

- **Module:** `orchestration.py`
- **Functions (pure relative to outside world; mutate only `state`):**
  - `emit_echo(kind: str, payload: dict, state: dict) -> dict`
    - Writes an echo (or no-ops if duplicate via idempotency).
  - `read_echoes(filters: dict) -> list[dict]`
    - Retrieves echoes by criteria (leaf_id, kind, time window, actor scope).

### 3.1 Input/Output Contracts (JSONC examples)

```jsonc
// emit_echo input (conceptual)
{
  "kind": "lantern_lit",
  "payload": { "x": 12, "y": 4, "idempotency_key": "wg-12-4" },
  "state": { /* game state; JSON-serializable */ }
}

// read_echoes filters (conceptual)
{
  "leaf_id": "archipelago/enchanted_isle/whispering_grove",
  "kind": "lantern_lit",
  "since_ts": "2025-08-01T00:00:00Z",
  "actor_scope": "self" // or "any"
}
```

## 4) Echo Record Schema

### 4.1 Canonical Echo (stored form)

```jsonc
{
  "echo_id": "f2b6d8b8-8f7d-4f34-9a81-02c7e1a3e0e6",   // uuid
  "ts": "2025-08-18T04:05:06Z",                       // ISO-8601
  "leaf_id": "archipelago/enchanted_isle/whispering_grove",
  "kind": "lantern_lit",
  "payload": { "x": 12, "y": 4, "idempotency_key": "wg-12-4" },
  "actor_hash": "0a5c...sha256hex...b9f3",            // pseudonymous hash; no PII
  "ttl_s": 1209600                                    // 14 days (default)
}
```

### 4.2 JSON Schema (lite)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:cybertree:echo:0.1",
  "title": "Echo v0.1",
  "type": "object",
  "required": ["echo_id", "ts", "leaf_id", "kind", "payload", "actor_hash", "ttl_s"],
  "additionalProperties": false,
  "properties": {
    "echo_id": { "type": "string", "format": "uuid" },
    "ts": { "type": "string", "format": "date-time" },
    "leaf_id": { "type": "string", "pattern": "^[a-z0-9_-]+/[a-z0-9_-]+/[a-z0-9_-]+$" },
    "kind": { "type": "string", "minLength": 1 },
    "payload": { "type": "object", "additionalProperties": true },
    "actor_hash": { "type": "string", "pattern": "^[A-Fa-f0-9]{64}$" },
    "ttl_s": { "type": "integer", "minimum": 0 }
  }
}
```

---

## 5) Idempotency & Dedupe

- Use `payload.idempotency_key` (caller-chosen) to avoid duplicates for the same logical event.
- If a prior echo exists with the same `leaf_id`, `kind`, and `idempotency_key`, `emit_echo` **MUST no-op**.
- If absent, create a new echo with a fresh `echo_id` and `ts`.

---

## 6) Retention & Expiry

- Default **TTL = 14 days** (`ttl_s = 1209600`).
- Leaf authors may set a different TTL per echo by writing `ttl_s`.
- Expiry policy: expired echoes **MAY** be omitted by `read_echoes`; compaction runs can hard-delete expired rows.

---

## 7) Privacy & Safety

- **Never** include PII in `payload`.
- `actor_hash` must be a stable, salted **SHA-256** (server-side salt) to prevent cross-context correlation.
- Echoes are **append-only**. Redaction requires an explicit, audited admin path.

---

## 8) Storage Adapters (v0.1)

- Start with **in-process store** (per session) for local tests.
- Provide a thin adapter interface when promoting to shared storage:

```python
class EchoStore:
    def write(self, echo: dict) -> None: ...
    def query(self, filters: dict) -> list[dict]: ...
    def exists(self, leaf_id: str, kind: str, idem_key: str) -> bool: ...
```

## 9) Errors & Fallbacks

- Invalid schema → return error frame or raise `ValueError` in dev; soft-log + drop in prod (configurable).
- Unknown `leaf_id` → treat as local leaf or reject (engine policy).
- Oversized `payload` (> 4 KB suggested limit) → truncate or reject per config.

---

## 10) Validation & Tests

**Leaf tests (Tier-1):**
- `orchtest.py::test_emit_echo_idempotent`
- `orchtest.py::test_read_echoes_filters`
- `camoutest.py::test_camouflage_hooks_pure` _(unchanged; ensures echo effects don’t break purity)_
- JSON Schema validation for a sample echo passes.

**Engine/router tests:**
- Echo `effects` in frames are **passed through unchanged**.
- State roundtrip remains **JSON-serializable**.

---

## 11) Examples

// Example: emit → effect included in a frame
{
  "effects": [
    { "type": "echo", "payload": { "kind": "lantern_lit", "idempotency_key": "wg-12-4" } }
  ]
}

// Example: read result
[
  {
    "echo_id": "f2b6d8b8-8f7d-4f34-9a81-02c7e1a3e0e6",
    "ts": "2025-08-18T04:05:06Z",
    "leaf_id": "archipelago/enchanted_isle/whispering_grove",
    "kind": "lantern_lit",
    "payload": { "x": 12, "y": 4, "idempotency_key": "wg-12-4" },
    "actor_hash": "0a5c...b9f3",
    "ttl_s": 1209600
  }
]

---

## 12) Versioning & Migration

- Backward-compatible field additions (new optional keys) are allowed within **v0.x**.
- Breaking changes require a new `$id` (e.g., `urn:cybertree:echo:0.2`) and a migration note.
