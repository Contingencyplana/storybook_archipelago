<!-- Save to: ops/release_and_versioning.md -->

# 🚀 Release & Versioning — Storybook Archipelago

**Goal:** ship reproducible, test-verified ZIPs that match Git tags exactly, with clear contracts between **trunk routers** and **leaf nodes**.

- **Audience:** devs, CI, and “drag-badge” ZIP consumers.  
- **Scope:** version scheme, tagging, packaging, release gates, hotfixes, and rollback.

---

## 1) Version Scheme

We use **SemVer** with pre-releases while under active development.

- **Stable:** `MAJOR.MINOR.PATCH` → `1.2.3`  
- **Pre-release:** `MAJOR.MINOR.PATCH-qualifier.N+YYYYMMDDHHMM`  
  - Examples: `0.3.0-alpha.4+20250811`, `0.3.0-rc.1+20250812`  
- **Start in 0.y:** breaking changes are allowed between minors; we still log them.

**When to bump**  
- `MAJOR`: incompatible contract changes (router↔leaf return contract, four-part paths format, etc.).  
- `MINOR`: add gameplay nodes/features, keep contracts stable.  
- `PATCH`: doc/test/bugfix that doesn’t change contracts or behavior surfaces.

**Contract labels (required in release notes)**  
- `trunk_router_spec`: e.g., `v0.1`  
- `leaf_contract`: e.g., `v0.1`  
- If either changes incompatibly → **MAJOR**.

---

## 2) Tags & Naming

- **Git tag:** `vX.Y.Z` or `vX.Y.Z-qualifier.N`  
- **ZIP artifact:**  
  - Stable: `dist/storybook_archipelago-vX.Y.Z.zip`  
  - Pre: `dist/storybook_archipelago-vX.Y.Z-qualifier.N+YYYYMMDD-HHMM.zip`  
- **Checksum:** `dist/storybook_archipelago-vX.Y.Z.zip.sha256`

These names must match what users drag into Chat (and what CI publishes).

---

## 3) Packaging (deterministic)

Preferred: `git archive` (honors `.gitattributes export-ignore`).

- `.gitattributes` should include:

/.*                  export-ignore
/.venv/              export-ignore
**/__pycache__/      export-ignore
**/*.pyc             export-ignore
.vscode/             export-ignore
dist/                export-ignore

- Fallback (PowerShell `Compress-Archive`) must exclude: `.git/`, `.venv/`, `__pycache__/`, `.vscode/`, `.github/`, `dist/`.

**Determinism tips**  
- Build from a **clean** index (`git status` empty).  
- Package from a **tag** (not a moving branch) for released builds.

---

## 4) Release Gates (must be green)

Before tagging:

1. **Tests:** `pytest -q` → all pass.  
2. **Guards:**  
 - Lint: disallow closed-bracket portal tags (only allow `[PORTAL:`).  
 - Lint: disallow non-string returns in handlers/story.  
3. **Milestones updated:** root `milestones.md` + node `taskmaps/milestones.md`.  
4. **Portal maps:** four-part paths only; no placeholders for activated nodes.  
5. **Contracts unchanged or documented:** if changed, bump version per §1.

---

## 5) Release Procedure (checklist)

**A. Choose version**  
- Decide stable `X.Y.Z` or pre `X.Y.Z-alpha.N`.

**B. Cut the build**  
- Ensure working tree clean.  
- Run: tests + guards.  
- Package ZIP (VS Code task **“Package: make clean ZIP”**).  
- Compute checksum:

```powershell
Get-FileHash -Algorithm SHA256 "dist\storybook_archipelago-<name>.zip" |
  ForEach-Object { $_.Hash } > "dist\storybook_archipelago-<name>.zip.sha256"
```

### C. Tag & Annotate

```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z

Contracts:
- trunk_router_spec: v0.1
- leaf_contract: v0.1

Notes:
- Added/changed nodes...
- Portal activations...
- Breaking changes...
- CI: green (tests+guards)."
git push origin vX.Y.Z
```

### D. Publish Artifacts

- Attach ZIP + `.sha256` to the GitHub Release.  
- Paste Release Notes (template below).  

---

### 6) Hotfixes & Rollback

**Hotfix (PATCH)**  
- Branch from tag `vX.Y.(Z-1)` or current `vX.Y.Z`.  
- Minimal fix, update tests, bump to `vX.Y.(Z+1)`.  
- Repackage, tag, release.  

**Rollback**  
- If a release fails in the wild:  
  - Mark bad release in GitHub as *Deprecated*.  
  - Reinstate previous tag’s ZIP as *Latest*.  
  - Open an incident note under `ops/incidents/`.  

---

### 7) CI Alignment

On push/tag:  
- Run tests + guards.  
- For tags matching `v*`:  
  - Build ZIP via `git archive`.  
  - Upload ZIP + `.sha256` as artifacts and to GitHub Release.  

⚖ Local VS Code tasks and GitHub Actions should use the same ripgrep patterns and exit-code handling to avoid drift.  

---

### 8) Release Notes Template

# Storybook Archipelago vX.Y.Z — YYYY-MM-DD

## Contracts
- trunk_router_spec: v0.1 (unchanged)  
- leaf_contract: v0.1 (unchanged)  

## Highlights
- <1–3 bullets of player-visible changes>  

## Nodes & Portals
- Activated: `a0_0_sailing_mode/.../a0_0_whispering_grove_node (L/R → drifting_glade)`  
- Updated portal maps: <files>  

## Tests & Guards
- pytest: all green  
- Guards: portal-tag + non-string-returns — pass  

## Breaking Changes
- None / <details + migration>  

## Artifacts
- ZIP: `storybook_archipelago-vX.Y.Z.zip`  
- SHA256: `<hash>`  
- Tag: `vX.Y.Z`  

### 9) Version Examples

**First playable pre-release:**  
- Tag: `v0.3.0-alpha.1`  
- ZIP: `storybook_archipelago-v0.3.0-alpha.1+20250811-1502.zip`  

**First stable cut (same contracts):**  
- Tag/ZIP: `v0.3.0`  

**Breaking contract change to trunk router:**  
- Tag/ZIP: `v1.0.0`  

---

### 10) Quick Commands (PowerShell)

From repo root, after tests/guards:

```powershell
# Package current state (using VS Code task or directly)
# VS Code: Terminal → Run Task → "Package: make clean ZIP"

# Direct (git archive):
$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
$zip   = "dist\storybook_archipelago-v0.3.0-rc.1+$stamp.zip"
$env:GIT_PAGER=''
$env:GIT_DIR=$null; $env:GIT_WORK_TREE=$null
git --no-pager archive -o $zip --format zip --worktree-attributes HEAD

Get-FileHash -Algorithm SHA256 $zip | % { $_.Hash } > "$zip.sha256"
```

### 11) Governance (lightweight)

- **Single source of truth:** the tag + its attached ZIP.  
- **Docs must match:** `milestones.md`, `portalmap.md` reflect the tagged state.  
- **No mutable re-uploads:** if you rebuild, bump the version.  

---

### Appendix A — Contract Compatibility Grid (starter)

| Trunk Router Spec | Leaf Contract | Compatible? | Notes                   |
|-------------------|---------------|-------------|-------------------------|
| v0.1              | v0.1          | ✅           | Current baseline        |
| v0.1              | v0.2          | ⚠️           | Leaf back-compat needed |
| v0.2              | v0.1          | ❌           | Router breaking change  |

⚖ Keep this aligned with `testing/contract_test_matrix.md`.

---

**Bottom line:** Tag it, test it, zip it, checksum it, and write it down.  
