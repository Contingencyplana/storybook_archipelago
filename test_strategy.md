<!-- Save to: storybook_archipelago/test_strategy.md -->

# 🧪 Canonical Testing Doctrine – test_strategy.md

This file defines the **testing philosophy, requirements, and structure** for all nodes in *Storybook Archipelago*, across all three tiers (Tier 1–3).

Testing in this game is **not a technical afterthought** — it is a **recursive necessity**.  
It verifies that recursion is stable, paths are playable, memories are valid, and player experience is **joyfully predictable**.

Without testing, recursion fractures.  
With testing, recursion blooms.

---

## 🧭 Testing by Node Tier

| Tier | Required Tests | Notes |
|------|----------------|-------|
| Tier 1 | ✅ Full coverage | All logic, integration, memory, and narrative must be tested |
| Tier 2 | 🟡 Minimal coverage | Key L/R path and integration tests required |
| Tier 3 | ❌ Optional | No test files required, but logic must still be safe and non-blocking |

---

## 🧪 Tier 1 – Full Test Coverage

Tier 1 nodes must be **completely testable**. This includes:

- Logic behavior (`lefttest.py`, `righttest.py`)
- Narrative consistency (`storytest.py`)
- Routing coordination (`integtest.py`)
- Camouflage conditions (`camoutest.py`)
- State integrity (`orchtest.py`)

### 📦 Expected Test Files (Tier 1)

```plaintext
├── lefttest.py         # Tests all L-input logic, branches, failovers
├── righttest.py        # Tests all R-input logic, branches, failovers
├── storytest.py        # Verifies option visibility, stanza structure, list accuracy
├── integtest.py        # Ensures correct routing across system layers
├── camoutest.py        # Tests tone triggers, disguise changes, overlay effects
├── orchtest.py         # Validates memory state changes, loops, recovery
```

✅ All tests must pass before a Tier 1 node is considered trace-complete.

---

## 🟡 Tier 2 – Minimal Test Coverage

Tier 2 nodes are playable but lightweight. Their testing must ensure:

- **L and R choices do not crash**
- `integration.py` produces expected output
- `story.py` aligns with logic intent

### 🧪 Required Tests (Tier 2)

You may include:

```plaintext
├── lefttest.py         # Optional but recommended
├── righttest.py        # Optional but recommended
```

Integration logic should be self-tested using lightweight methods (e.g., assertions, print-checks) unless promoted to Tier 1.

Tier 2 nodes must be safe, but may be shallow.

---

## ❌ Tier 3 – Test Exempt

Tier 3 nodes do **not** require standalone test files. However:

- `leftrightmain.py` must **not** contain branching logic  
- Logic must **always** resolve to a valid destination  
- Player must **never** get stuck  

> Use quick dev-side assertions or safe-routing wrappers as needed.

---

## 📂 Layer-Specific Test Notes

| File              | Test File         | Required Tier  | Notes                               |
|-------------------|-------------------|----------------|-------------------------------------|
| `leftmain.py`     | `lefttest.py`     | Tier 1         | Optional Tier 2                     |
| `rightmain.py`    | `righttest.py`    | Tier 1         | Optional Tier 2                     |
| `story.py`        | `storytest.py`    | Tier 1         | ❌ Not required for Tiers 2–3       |
| `integration.py`  | `integtest.py`    | Tier 1         | ❌ Not required for Tiers 2–3       |
| `camouflage.py`   | `camoutest.py`    | Tier 1         | ❌ Not required for Tiers 2–3       |
| `orchestration.py`| `orchtest.py`     | Tier 1         | ❌ Not required for Tiers 2–3       |

---

## 🔁 L/R Path Test Expectations

All test files should validate:

- ✅ Correct routing destination (`portalmap.md` alignment)
- ✅ Proper failover (e.g., if a target node is missing or memory is invalid)
- ✅ Recursive sanity (e.g., no infinite logic loops)
- ✅ Poetic correctness (e.g., story and logic do not conflict)

> Every time the player presses **L** or **R**, that decision must be **predictable**, **testable**, and **narratively sound**.

---

## L/R Path Test Expectations (Additional Rules)
 

- Left path MUST include the token `[LEFT]` somewhere in the returned string.
- Right path MUST include the token `[RIGHT]`.
- `story.describe_scene(memory)` MUST include the word “grove” (case-insensitive) and MUST NOT include any `[PORTAL:` tag.

Suggested pytest assertions:

```python
assert "[LEFT]" in left_output
assert "[RIGHT]" in right_output
assert "grove" in story_output.lower()
assert "[PORTAL:" not in story_output
```

## 🧪 Recursive Edge-Case Testing

For advanced Tier 1 nodes, also test:

- What happens if memory is corrupted  
- Re-entry to the same node from multiple angles  
- Camouflage triggers under atypical player states  
- “Story echoes” (same node revisited with altered mood/memory)

---

## 🧠 AI-Compatible Structure

Test files must follow **predictable naming conventions** so AI agents can:

- Parse which logic files are tested  
- Auto-generate or repair missing tests  
- Confirm test readiness before enabling player traversal

---

## 🔚 Final Principle

Testing is not bureaucracy.  
Testing is **recursive trust made visible**.

A tested node is:

- ✅ Knowable  
- ✅ Replayable  
- ✅ Evolvable  
- ✅ Safe

> **No recursion without reflection.  
> No reflection without tests.**
