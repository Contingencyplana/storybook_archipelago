# Storybook Archipelago — Production Checklist (with Dependencies)

## How to Use
- **Status keys:** ☐ Not started · 🟡 In progress · ✅ Done
- **Owners:** fill as you assign; leave “—” if unassigned
- **Dependencies:** all listed items must be ✅ before starting
- **DAG rule:** Prefer completing each “Step n.x” top-to-bottom before moving to the next step unless marked “parallelizable”

---

## Step 1 — Critical Pathing & Linking (BLOCKERS — do first)

1.1 ☐ **portals_and_four_part_paths.md**  
- **Status:** ✅ *Drafted; needs review*  
- **Owner:** —  
- **Depends on:** —  
- **DoD:** Reviewed; diagrams for portal classes + 4-part path schema; examples for node ↔ path resolution; testable rules.

1.2 ☐ **workspace_registry.md**  
- **Owner:** —  
- **Depends on:** 1.1  
- **DoD:** Canonical registry schema (IDs, slugs, path roots, visibility); CRUD rules; collision policy; sample seed file.

1.3 ☐ **workflow.md**  
- **Owner:** —  
- **Depends on:** 1.1, 1.2  
- **DoD:** End-to-end authoring flow: create → link → test → publish → archive; state diagram; rollback/merge policy.

> **Exit gate for Step 1:** All path/link resolution is deterministic and testable across workspaces.

---

## Step 2 — Identity & Standards (unblocks naming + language; mostly parallel after Step 1)

2.1 ☐ **README.md** *(workspace-level)*  
- **Owner:** —  
- **Depends on:** 1.1 (reference linking model)  
- **DoD:** Purpose/scope; quickstart; folder map; link to critical docs; contribution rules; “what’s in/out” table.

2.2 ☐ **conventions.md**  
- **Owner:** —  
- **Depends on:** 2.1  
- **DoD:** Naming rules (files, stanzas, nodes); commit style; doc tone; capitalization; filename prefixes; examples.

2.3 ☐ **glossary.md**  
- **Owner:** —  
- **Depends on:** 2.2  
- **DoD:** Canon terms with short defs + crosslinks; “anti-terms” to avoid; living update policy.

> **Exit gate for Step 2:** Names, tone, and vocabulary are stable; newcomers can read README → conventions → glossary and navigate.

---

## Step 3 — Testing & Navigation (formalizes validation + maps; depends on Steps 1–2)

3.1 ☐ **test_strategy.md**  
- **Owner:** —  
- **Depends on:** 1.3, 2.2  
- **DoD:** Required tests per tier/file; minimal test sets; fixtures; CI hooks; skip rules; sample test matrix.

3.2 ☐ **worldmap.md**  
- **Owner:** —  
- **Depends on:** 1.1, 1.2  
- **DoD:** Island/mode map; traversal rules; node address format; “you are here” locator spec; sample mini-map.

3.3 ☐ **acronyms.md** *(parallelizable with 3.2)*  
- **Owner:** —  
- **Depends on:** 2.3  
- **DoD:** Acronym → expansion table; crosslinks to glossary; usage notes; lint rule for first‑use expansion.

> **Exit gate for Step 3:** CI can validate builds; navigation has a canonical map; teams share test vocabulary.

---

## Step 4 — Secondary Structural References (nice-to-have for velocity; do after 1–3)

4.1 ☐ **planning_spaces.md**  
- **Owner:** —  
- **Depends on:** 1.2, 1.3  
- **DoD:** Standard layout for planning areas; status labels; merge rules to canon; archival/expiry policy.

4.2 ☐ **milestones.md**  
- **Owner:** —  
- **Depends on:** 1.3, 2.2  
- **DoD:** Milestone schema; cadence (e.g., every two nodes); required fields; sample entries; rollup logic.

4.3 ☐ **gameplay_principles.md**  
- **Owner:** —  
- **Depends on:** 2.1  
- **DoD:** Core design tenets; do/don’t table; examples tied to node tiers; tradeoff guidance.

4.4 ☐ **camouflage_layers.md**  
- **Owner:** —  
- **Depends on:** 4.3, 2.2  
- **DoD:** Layer taxonomy; triggers; accessibility notes; testing hooks; fallback visuals/text.

> **Exit gate for Step 4:** Teams can plan, log, and align design choices without blocking core builds.

---

## Step 5 — Advanced AI / Recursive Control (governance + safety; start when 1–3 are solid)

5.1 ☐ **philosophy.md**  
- **Owner:** —  
- **Depends on:** 2.1  
- **DoD:** Project north star; safety lens; fun/commerce balance; interpretive examples.

5.2 ☐ **tiny_steps.md**  
- **Owner:** —  
- **Depends on:** 1.3, 5.1  
- **DoD:** Doctrine checklist; “slice until safe” rules; escalation halts; CI gate mapping.

5.3 ☐ **ai_agents.md**  
- **Owner:** —  
- **Depends on:** 2.3  
- **DoD:** Agent roster, roles, inputs/outputs, boundaries; example traces; versioning.

5.4 ☐ **ai_agency_theory.md**  
- **Owner:** —  
- **Depends on:** 5.1, 5.3  
- **DoD:** Agency levels; permission model; oversight lanes; risks and mitigations.

5.5 ☐ **ai_handshake_protocol.md**  
- **Owner:** —  
- **Depends on:** 5.3, 2.2  
- **DoD:** Request/response format; error classes; abort/rollback; logging spec; worked examples.

5.6 ☐ **agent_escalation_matrix.md**  
- **Owner:** —  
- **Depends on:** 5.5  
- **DoD:** Severity tiers; who escalates to whom; timing windows; auto‑halts; human‑in‑the‑loop triggers.

5.7 ☐ **recursive_anomaly_protocol.md**  
- **Owner:** —  
- **Depends on:** 5.6, 3.1  
- **DoD:** Detection signals; quarantine flows; reentry criteria; test harness.

5.8 ☐ **secondary_purpose.md**  
- **Owner:** —  
- **Depends on:** 5.1, 4.3  
- **DoD:** Non‑primary goals; guardrails to prevent drift; when/how to park nice‑to‑haves.

5.9 ☐ **node_tiers.md**  
- **Owner:** —  
- **Depends on:** 2.2, 1.3  
- **DoD:** Tier definitions; capabilities; inputs/outputs; promotion criteria.

5.10 ☐ **tier_1_minigame_node_structure.md**  
- **Owner:** —  
- **Depends on:** 5.9, 3.1  
- **DoD:** Required files; L/R behavior spec; tests; templates.

5.11 ☐ **tier_2_minigame_node_structure.md**  
- **Owner:** —  
- **Depends on:** 5.9, 3.1  
- **DoD:** As above, with numbered list activation; orchestration notes.

5.12 ☐ **tier_3_minigame_node_structure.md**  
- **Owner:** —  
- **Depends on:** 5.9, 3.1  
- **DoD:** Tier‑3 combined logic (leftrightmain), lists cycling, safety rails; tests.

---

## Fast Critical Path (single-file order)
1) 1.1 portals_and_four_part_paths.md →  
2) 1.2 workspace_registry.md →  
3) 1.3 workflow.md →  
4) 2.1 README.md →  
5) 2.2 conventions.md →  
6) 2.3 glossary.md →  
7) 3.1 test_strategy.md →  
8) 3.2 worldmap.md

> After step 8, most remaining items are **parallelizable** with their local deps satisfied.

---

## Acceptance Gates (per phase)
- **Gate A (after Step 1):** Links resolve deterministically across workspaces.  
- **Gate B (after Step 2):** Names/tone fixed; glossary usable; onboarding possible.  
- **Gate C (after Step 3):** CI/fixtures run green; map + locator spec usable in docs.  
- **Gate D (after Step 4):** Planning/milestones/design principles standardized.  
- **Gate E (after Step 5):** AI safety + escalation + anomaly handling operational; tiers codified.
