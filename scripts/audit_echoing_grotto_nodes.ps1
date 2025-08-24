# scripts/audit_echoing_grotto_nodes.ps1
# Audits the six Echoing Grotto nodes against the canonical 16-file layout.
# Safe by default (no changes). Use -DeleteEmpty to remove empty ghost nodes.
# Use -ScaffoldMissing to create only files that are missing (never overwrite).

param(
  [switch]$DeleteEmpty,
  [switch]$ScaffoldMissing
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Step($m){ Write-Host "==> $m" -ForegroundColor Cyan }
function Info($m){ Write-Host "   $m" }
function Warn($m){ Write-Host "   $m" -ForegroundColor Yellow }
function Good($m){ Write-Host "   $m" -ForegroundColor Green }

# Resolve repo root
try { $root = (git rev-parse --show-toplevel).Trim() } catch { $root = (Get-Location).Path }
Set-Location $root
Step "Repo root: $root"

$base = "a0_0_sailing_mode\a1_2_echoing_grotto_minigame"
$nodes = @(
  "a0_0_gate_of_echoes_node",
  "a0_0_resonant_chamber_node",
  "a0_1_mirror_pool_node",
  "a0_1_whisper_chorus_node",
  "a0_2_resonance_pool_node",
  "a0_2_whispering_arch_node"
)

# Canonical 16 files
$required = @(
  "__init__.py",
  "README.md",
  "integration.py",
  "integtest.py",
  "camouflage.py",
  "camoutest.py",
  "orchestration.py",
  "orchtest.py",
  "leftmain.py",
  "lefttest.py",
  "rightmain.py",
  "righttest.py",
  "story.py",
  "storytest.py",
  "portalmap.md",
  "subtaskmap.md"
)

# Minimal safe stub contents
$stubPy = @"
\"\"\"Stub file — Echoing Grotto node.
This stub exists to satisfy the 16-file layout. Replace with real logic later.
\"\"\"
def _stub(): return "stub"
"@

$stubReadme = @"
# Node (Echoing Grotto)

Scaffold placeholder for canonical 16-file layout. Replace with real description.
"@

$stubMD = @"
<!-- Scaffold placeholder. Replace with real content. -->
"@

# Helper to create a stub once
function Ensure-Stub {
  param([string]$path)
  if (Test-Path $path) { return }
  $ext = [IO.Path]::GetExtension($path).ToLowerInvariant()
  $dir = Split-Path -Parent $path
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  switch ($ext) {
    ".py" { Set-Content -LiteralPath $path -Value $stubPy -Encoding UTF8 }
    ".md" {
      if ([IO.Path]::GetFileName($path) -ieq "README.md") {
        Set-Content -LiteralPath $path -Value $stubReadme -Encoding UTF8
      } else {
        Set-Content -LiteralPath $path -Value $stubMD -Encoding UTF8
      }
    }
    default { Set-Content -LiteralPath $path -Value "" -Encoding UTF8 }
  }
  Info "Created stub: $path"
}

$summary = @()

foreach ($n in $nodes) {
  $nodePath = Join-Path $base $n
  Step "Auditing: $nodePath"

  if (-not (Test-Path $nodePath)) {
    Warn "Missing directory."
    if ($ScaffoldMissing) {
      New-Item -ItemType Directory -Force -Path $nodePath | Out-Null
      Info "Created directory: $nodePath"
    }
    $summary += [pscustomobject]@{ Node=$n; Status="Missing Dir"; Missing=16; Extra=0 }
    continue
  }

  $files = Get-ChildItem -LiteralPath $nodePath -File -ErrorAction SilentlyContinue
  if (-not $files) {
    Warn "Directory exists but is empty."
    if ($DeleteEmpty) {
      Remove-Item -Recurse -Force $nodePath
      Info "Removed empty node directory."
      $summary += [pscustomobject]@{ Node=$n; Status="Removed Empty"; Missing=16; Extra=0 }
      continue
    } else {
      if ($ScaffoldMissing) {
        foreach ($req in $required) { Ensure-Stub (Join-Path $nodePath $req) }
        $files = Get-ChildItem -LiteralPath $nodePath -File -ErrorAction SilentlyContinue
      }
    }
  }

  $presentNames = $files.Name
  $missing = @($required | Where-Object { $_ -notin $presentNames })
  $extra   = @($presentNames | Where-Object { $_ -notin $required })

  if ($missing.Count -eq 0 -and $extra.Count -eq 0) {
    Good "OK: canonical 16/16 present."
    $summary += [pscustomobject]@{ Node=$n; Status="OK"; Missing=0; Extra=0 }
  } else {
    if ($missing.Count -gt 0) { Warn ("Missing: " + ($missing -join ", ")) }
    if ($extra.Count   -gt 0) { Warn ("Extra: "   + ($extra   -join ", ")) }

    if ($ScaffoldMissing -and $missing.Count -gt 0) {
      foreach ($m in $missing) {
        Ensure-Stub (Join-Path $nodePath $m)
      }
      Good "Filled missing files with stubs."
    }

    $summary += [pscustomobject]@{
      Node=$n; Status="Needs Attention"; Missing=$missing.Count; Extra=$extra.Count
    }
  }
}

Step "Summary"
$summary | Format-Table -AutoSize

if ($ScaffoldMissing) {
  Step "Staging newly created stubs (if any)"
  git add $base
  $st = git diff --cached --name-only
  if ([string]::IsNullOrWhiteSpace($st)) {
    Info "Nothing to commit."
  } else {
    Step "Running pytest (quick gate)"
    try {
      pytest -q
      if ($LASTEXITCODE -eq 0) {
        Step "Committing + pushing"
        git commit -m "Echoing Grotto: scaffold missing 16-file layout (safe stubs, no overwrite)"
        git push
      } else {
        Warn "Tests failed; not committing. Inspect changes."
      }
    } catch {
      Warn "Pytest threw; not committing."
    }
  }
} else {
  Info "No changes made (read-only audit). Re-run with -ScaffoldMissing and/or -DeleteEmpty if desired."
}
