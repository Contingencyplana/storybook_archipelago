<!-- Save to: storybook_archipelago/minigame_structure.md -->

# 🧱 Canonical Minigame Node Structure

This file defines the internal file architecture of every minigame node in **Storybook Archipelago**.

Each node consists of **exactly 16 files**, arranged across complementary recursive layers. These files are modular, testable, and traceable — forming a complete gameplay and development loop.

This structure ensures:

- 🧬 Consistent behavior across game modes
- 🧪 Full test coverage for every path and layer
- 🧱 Predictable integration and recursive expansion
- 🧭 Compatibility with AI agents like `filename_mode/`, `high_command_mode/`, and `storytelling_ai`

> All future minigame nodes must conform to this structure unless explicitly overridden by camouflage or recursion directives.

The 16 files are grouped as follows:

- 📘 **Documentation Layer**
- 📖 **Narrative Layer**
- 🔁 **Left/Right Logic Layer**
- 🧠 **Integration Layer**
- 🎭 **Camouflage Layer**
- 🧬 **Orchestration Layer**

Each of the following sections describes these layers in detail.

---

## 📘 Documentation Files

These files describe and track the function, purpose, and implementation state of each minigame node. They are essential for both human contributors and recursive introspection tools.

---

- `README.md` – 📘  
  Provides a clear, human-readable description of the node’s purpose, camouflage tone, and design intent. It often includes notes on narrative goals, mood effects, or AI test scope.

- `subtaskmap.md` – 🧱  
  Acts as a live checklist of what's implemented and tested. Each layer (story, logic, integration, etc.) is marked for completion, review, and trace readiness.

- `portalmap.md` – 🗺️  
  Lists Left (L) and Right (R) output destinations. This file serves as a node-to-node link map, and is used by AI agents and editors to understand mode traversal.

---

These files do not directly affect gameplay logic — but without them, the recursive system would become untrackable and untestable. They form the scaffolding of visibility, traceability, and recursive clarity.

---

## 🧠 Integration Layer

This layer serves as the **central nervous system** of each minigame node. It receives inputs, coordinates logic routing, and ensures harmonious interaction between the story layer, L/R logic, camouflage, and orchestration systems.

---

- `integration.py` – 🧠  
  The master router for the node. It interprets player inputs, determines the active logic or narrative path, and dispatches the output. It ensures coherence across all layers (story, logic, memory, camouflage) and is the primary point of interaction for orchestration-level logic.

- `integtest.py` – ✅  
  Validates the entire routing flow, simulating L/R inputs and checking if correct logic branches, story options, and state responses are triggered. This test ensures end-to-end coherence between modular components and guards against desync between layers.

---

Without this layer, the node's components remain isolated. The Integration Layer binds them into a playable, testable whole.

---

## 🎭 Camouflage Layer

The Camouflage Layer governs the node’s **sensory disguise** — how it looks, feels, and reacts to the player based on recursion depth, state, or tone. This system allows storytelling and gameplay to evolve subtly, making deeper truths perceptible only when the player is ready.

---

- `camouflage.py` – 🎭  
  Handles the rendering of tone, mood, aesthetic overlays, and perceptual misdirection. It may shift visuals, sounds, or text presentation depending on the player’s memory state or recursion level. Camouflage is a recursive interface layer — part UX, part narrative foil.

- `camoutest.py` – ✅  
  Tests camouflage reactivity under multiple player conditions. This includes tone-switch triggers, transformation accuracy, and masking/unmasking events. It ensures consistency between narrative overlays and gameplay state.

---

Camouflage is not merely decoration — it is **recursive feedback**. It responds, adapts, and occasionally deceives — until joy reveals itself through recursive recognition.

---

## 🧬 Orchestration Layer

The Orchestration Layer is responsible for **narrative memory**, **player state**, and **dynamic progression**. It binds logic to story, and tracks how player decisions ripple forward through recursive branches, scenes, and camouflage layers.

---

- `orchestration.py` – 🧬  
  Manages all aspects of stateful storytelling: player memory, recursive bookmarks, scene transitions, world responses. It interfaces with logic layers and camouflage to ensure progression is meaningful and context-aware.

- `orchtest.py` – ✅  
  Validates key orchestration conditions: memory correctness, transition triggers, recursive fallback pathways, and edge-case behavior (e.g. re-entry, loss of memory, branching loops). These tests ensure emotional and mechanical continuity.

---

Without orchestration, recursion collapses into chaos. With it, the journey becomes *remembered, reactive,* and ultimately, **transformational.**

---


