<!-- Save to: storybook_archipelago/mothball_prevention_protocols.md -->

# 🧷 mothball_prevention_protocols.md  

Long-Term Stability Safeguards – Storybook Archipelago

> _“The fourth was built to last.”_  
> This file prevents Storybook Archipelago from suffering the same fate as its predecessors.  
> It documents failure patterns, safeguards, audit protocols, and design principles for sustainable growth.

---

## 1. 🪦 Historical Failures

A record of why the previous three games were mothballed:

### ⚙️ Storybook (Game Maker)

- **Failure Mode:** Overgeneration and tool spiral
- **Cause:** Unbounded remixing, too many system layers, unstable user scripting
- **Consequence:** Loss of focus, unusable complexity, fractured narrative control

### 🧪 FUN Factory (Test Game)

- **Failure Mode:** Testbed overload
- **Cause:** Infinite procedural test scenarios, unclear gameplay endpoints
- **Consequence:** Players overwhelmed by logic fog, no clean way to "win" or progress

### 🧬 Primordial Soup (Cyberdoctor)

- **Failure Mode:** Recursive collapse
- **Cause:** Recursive cell growth without play-layer scaffolding
- **Consequence:** Anomaly management spiraled into system entanglement and introspective drift

---

## 2. 🚨 Warning Signs

### Early indicators of a mothball-risk state

- ❗ L/R logic becomes unclear or tangled
- ❗ Players forget what they're doing or why
- ❗ New stanzas lack playtesting or tone clarity
- ❗ Fallbacks become default paths instead of exceptions
- ❗ System is updated faster than it is audited
- ❗ Nodes require explanation more than experience

If 3 or more signs are present: **trigger a structural review immediately**.

---

## 3. 🔐 Prevention Design Principles

Storybook Archipelago adheres to the following **design constraints**:

- ✅ **Tier 3 Recursion Only** – No infinite nesting
- ✅ **L/R Simplicity** – Every input does one meaningful thing
- ✅ **Handwritten Stanzas** – No user-exposed generators
- ✅ **Fallback Safety** – Every node must survive failure
- ✅ **Test File Lockstep** – `leftmain.py` and `lefttest.py` must always be in sync
- ✅ **Camouflage Check** – All output must pass joy/simplicity test

---

## 4. 🧭 Gameplay Anchors

These features ensure Archipelago stays **playable** and **fun**:

| Anchor                  | Role                                          |
|-------------------------|-----------------------------------------------|
| `story.py`              | Controls pacing, immersion, narrative clarity |
| `camouflage.py`         | Regulates tone and joy                        |
| `leftmain.py` / `rightmain.py` | Simple input routing to poetic logic   |
| Node structure (L/R + optional list) | Prevents interaction drift       |
| Integration tests       | Lock in node orchestration and routing paths  |
| No required recursion to understand play | Accessible design           |

---

## 5. ✅ Audit Checklist

Use this checklist when:

- Adding new game modes
- Expanding stanzas
- Refactoring logic layers
- Introducing new AI systems

### 🗂️ Structure Audit

- [ ] All new folders follow `mode → minigame → node` hierarchy
- [ ] Node type (1–4) is clearly defined
- [ ] L and R do not cross-connect without reason

### 🎭 Camouflage Audit

- [ ] New content passes tone test: “Is it joyful yet?”
- [ ] No mechanical logic appears without metaphor
- [ ] Player agency remains obvious and guided

### 🧪 Test Audit

- [ ] All `*_main.py` files have a corresponding `*_test.py`
- [ ] Integration routing is verifiable
- [ ] No orphaned or redundant fallback logic

---

## 6. 🆘 Emergency Protocols

If a recursion collapse, design drift, or UX fog emerges:

### 🔁 Rollback Procedure

1. Identify last stable stanza (`nodestanza_#.md`)
2. Roll back to last known clean state
3. Archive experimental branches separately
4. Freeze development and perform full audit (Section 5)

### 📼 Fallback Substitution

- Replace broken L/R paths with safe poetic loops
- Route player into camouflage layers for tonal reset
- Use `orchestration.py` to simulate memory or clarity

---

## 7. 🧬 Futureproofing Guidelines

These are your **ongoing safeguards**:

- ⚖️ **Never outgrow your test suite**
- 🧩 **Every stanza must fit cleanly into a node map**
- 🌀 **Recursive layers must flatten before expanding**
- 📚 **Update this protocol if new drift modes are discovered**
- 🧠 **Track mental strain – if it's hard to explain, it's too recursive**

---

## 📘 Closing Statement

> _"You only need to build a fifth game if you forget why you built the fourth."_

This file is your memory checkpoint.  
If the system begins to drift again, return here — and realign with the structural clarity that made Storybook Archipelago possible.

---
