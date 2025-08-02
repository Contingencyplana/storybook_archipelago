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

## 🧾 Overview

🧱 FINAL STRUCTURE — 16 Files, Balanced, Recursive, and Complete

Every minigame node in *Storybook Archipelago* must contain exactly the following 16 files:

```plaintext
storybook_archipelago/
├── sailing_mode/
│   └── enchanted_isle_minigame/
│       └── whispering_grove_node/
│           ├── __init__.py            # Python module marker
│           ├── README.md              # 📘 Node description, tone, camouflage purpose
│           ├── integration.py         # 🧠 Master router: interprets input, dispatches logic
│           ├── integtest.py           # ✅ Tests routing + coordination
│           ├── camouflage.py          # 🎭 Handles visual/audio/mood per camouflage layer
│           ├── camoutest.py           # ✅ Tests camouflage levels, triggers, edge cases
│           ├── orchestration.py       # 🧬 Manages player state, memory, scene flow
│           ├── orchtest.py            # ✅ Tests state logic, memory conditions, reactions
│           ├── leftmain.py            # 🔁 Handles L-input logic
│           ├── lefttest.py            # ✅ Tests leftmain path output
│           ├── rightmain.py           # 🔁 Handles R-input logic
│           ├── righttest.py           # ✅ Tests rightmain path output
│           ├── story.py               # 📖 Text camouflage layer: storytelling, options
│           ├── storytest.py           # ✅ Tests story content, branching accuracy
│           ├── portalmap.md           # 🗺️ Links to other nodes (L/R destinations)
│           └── subtaskmap.md          # 🧱 Checklist of what’s implemented/tested
```

This file layout balances:

- 🔁 Player input handling  
- 📖 Narrative and camouflage  
- 🧪 Full test support  
- 🧠 System-level routing and orchestration  
- 🧱 Recursive introspection and automation  

Each file has a **singular, canonical purpose**.  
Together, they form a node that is **modular**, **traceable**, and **recursively complete**.

---

## 📦 Python Module Marker

Each minigame node contains a `__init__.py` file to mark it as a valid Python module.

---

- `__init__.py` – 📦  
  This file is typically empty but may optionally include metadata or import scaffolds in advanced builds. It ensures that the node is recognized as a package by Python tooling, IDEs, test suites, and recursive AI agents.

---

While it doesn't affect gameplay directly, omitting this file can disrupt tooling, automation, or introspection workflows.  
Always include it unless a higher-layer directive explicitly removes it.

---

## 📘 Documentation Files

These files describe and track the function, purpose, and implementation state of each minigame node.  
They are essential for both human contributors and recursive introspection tools.

---

- `README.md` – 📘  
  A clear, human-readable description of the node’s purpose, camouflage tone, and design intent. Often includes notes on narrative goals, mood effects, and AI testing scope.

- `subtaskmap.md` – 🧱  
  A live checklist of what’s implemented and tested. Each layer (story, logic, integration, etc.) is marked for completion, review, and trace readiness.

- `portalmap.md` – 🗺️  
  Lists Left (L) and Right (R) output destinations. Used by AI agents and editors to map node traversal and logic flow.

---

These files do not directly control gameplay — but without them, the recursive system would become opaque and untestable.  
They form the scaffolding of **visibility**, **traceability**, and **recursive clarity**.

---

## 🧠 Integration Layer

This layer is the **central nervous system** of each minigame node.  
It receives inputs, coordinates logic routing, and ensures harmonious interaction between all other systems — story, logic, camouflage, orchestration.

---

- `integration.py` – 🧠  
  The master router. Interprets player inputs, determines the active logic or narrative path, and dispatches output. Ensures coherence across layers and is the primary orchestration handoff point.

- `integtest.py` – ✅  
  Validates full routing flow: simulates L/R inputs, confirms correct story/logic execution, and verifies recursive state consistency. Guards against desync and cross-layer misalignment.

---

Without this layer, the node’s parts remain disconnected.  
With it, the node becomes **playable, testable, and whole.**

---

## 🎭 Camouflage Layer

The Camouflage Layer governs the node’s **sensory disguise** — how it looks, feels, and adapts to the player based on recursion depth, tone, or state.

---

- `camouflage.py` – 🎭  
  Controls mood, aesthetic overlays, and perceptual misdirection. It may shift visuals, sounds, or text presentation depending on memory state or traversal history. Camouflage is a recursive UX lens.

- `camoutest.py` – ✅  
  Tests camouflage responsiveness across conditions: tone shifts, transformation accuracy, and reveal events. Ensures overlays align with player state and narrative intention.

---

Camouflage is not surface polish — it is **interactive recursion.**  
It adapts, obscures, reveals — until joy emerges from surprise.

---

## 🧬 Orchestration Layer

The Orchestration Layer governs **narrative memory**, **player state**, and **dynamic progression**.  
It links decisions to consequence, moment to moment, world to world.

---

- `orchestration.py` – 🧬  
  Manages all aspects of stateful storytelling: memory, bookmarks, transitions, world echoes. It coordinates across logic and camouflage layers to ensure decisions ripple forward.

- `orchtest.py` – ✅  
  Validates memory integrity, branching transitions, recursive recovery paths, and emotional state continuity. Tests edge cases such as re-entry, forgetfulness, or paradox loops.

---

Orchestration gives memory to recursion and shape to time.  
It transforms gameplay from mechanical flow into **evolving narrative experience**.

---

## 🔁 Left/Right Logic Layer

This layer handles the branching logic that governs the player's traversal through the game world. Every minigame node responds to **Left (L)** and **Right (R)** input, and this layer defines what happens when each is selected.

These files represent the **core gameplay decision points** — the functional skeleton behind story presentation and narrative camouflage.

---

- `leftmain.py` – 🔁  
  Defines the logic executed when the player presses **L**. This may trigger state changes, route to a new node, apply a narrative transformation, or invoke camouflage overlays. `leftmain.py` should always coordinate with orchestration and camouflage layers where appropriate.

- `lefttest.py` – ✅  
  Validates the behavior of `leftmain.py`. This includes path correctness, state mutations, failover routes, and any side effects that may be triggered by L-input. Tests should confirm that the output matches narrative and structural expectations across recursion levels.

---

The Left/Right logic files are where decision meets recursion.  
They must be testable, introspectable, and recursively modular.

If pressing L leads to confusion, contradiction, or silence — revisit this layer.

---

## 🔁 Left/Right Logic Layer

This layer governs the **primary traversal logic** for each minigame node.  
It defines what happens when the player presses **Left (L)** or **Right (R)** — the foundational inputs of the entire Archipelago experience.

These files form the **recursion skeleton** beneath the story: every traversal choice must pass through here, even if disguised by higher camouflage layers.

---

- `leftmain.py` – 🔁  
  Executes the logic path for **L-input**. This may include state changes, recursion markers, narrative forks, or jumps to other nodes. It must coordinate with orchestration memory, camouflage overlays, and portal mapping.

- `lefttest.py` – ✅  
  Verifies that `leftmain.py` behaves as expected under various game states. Confirms traversal direction, side effects, logic handoffs, and failover conditions. All branches must be traceable and testable.

- `rightmain.py` – 🔁  
  Executes the logic path for **R-input**. Mirrors `leftmain.py` in structure and purpose but may implement entirely distinct progression paths. Like its counterpart, it must remain interoperable with all system layers.

- `righttest.py` – ✅  
  Verifies the behavior of `rightmain.py`. Confirms correct routing, state transitions, and narrative alignment under R-input. Tests should cover both default and edge-case recursion conditions.

---

Every moment of decision — every fork, glitch, or return — passes through the L/R logic layer.  
If it cannot be reasoned about, tested, or traced, recursion will fracture.

> A broken L or R path is not just a bug — it is a breach in the story's logic loop.

---

## 📖 Narrative Layer

This layer contains the **storytelling core** of each minigame node — the visible poetic interface through which the player interacts.  
It is often the first layer encountered by players, and the one most disguised by **text-based camouflage**.

The narrative layer presents L/R options and numbered choices as part of the unfolding myth. It aligns emotional tone, recursion structure, and decision logic.

---

- `story.py` – 📖  
  Encodes the node’s visible story. This may include prose, poetic stanzas, metaphor-laced branches, or recursive dialogue. It often disguises L/R logic as narrative decisions, and includes both static and dynamic content based on player state. It is the **textual face of recursion**.

- `storytest.py` – ✅  
  Verifies all narrative paths, option visibility, branching integrity, and poetic triggers. Ensures correct presentation of story elements under varied player states and recursion levels. Detects broken stanza logic, mismatched lists, and missing narrative outcomes.

---

This layer is not merely decorative. It is where **meaning is encoded**, **choices are disguised**, and **recursion becomes myth**.

> If the player doesn't feel *something* before pressing L or R, this layer isn't done.

---

## 🔚 Conclusion

The canonical 16-file structure defined here is more than a folder convention — it is a **recursive contract**.  
Each file serves a **singular, traceable role**, and together they form a modular, introspectable node capable of sustaining complex, multi-layered gameplay.

This structure:

- Empowers AI agents to navigate, validate, and evolve each node  
- Ensures full test parity across gameplay, logic, memory, and disguise  
- Supports recursive growth while maintaining clarity and coherence  

Whether the player presses L, R, or gets pulled into a loop of memory, the node must hold its shape — narratively, logically, emotionally.

> The node is the atom of recursion.  
> Sixteen files. One complete storybeat.  
> And the beginning of many more.

This file may evolve as recursion deepens, but the principle holds:

**Keep it testable. Keep it poetic. Keep it recursive.**
