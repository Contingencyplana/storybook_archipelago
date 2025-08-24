# scripts/clean_echoing_grotto_ghosts.ps1
# Cleans up Echoing Grotto ghost node directories.
# Removes:
#   1. Empty node directories
#   2. Duplicate node directories (only one allowed per index a0_0..a0_3)
#
# Safe and idempotent. After cleanup, runs pytest and commits changes.

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

if (-not (Test-Path $base)) {
  Warn "Base path not found: $base"
  exit 0
}

# 1) Delete empty node directories
Step "Checking for empty node directories"
$empties = Get-ChildItem -LiteralPath $base -Directory -Recurse -ErrorAction SilentlyContinue |
  Where-Object { -not (Get-ChildItem -LiteralPath $_.FullName -Force -File -ErrorAction SilentlyContinue) }

foreach ($d in $empties) {
  Warn "Deleting empty directory: $($d.FullName)"
  Remove-Item -Recurse -Force $d.FullName
  git rm -r --cached --ignore-unmatch $d.FullName 2>$null | Out-Null
}

# 2) Delete duplicate node directories by index
Step "Checking for duplicate node directories"
$groups = @{}
Get-ChildItem -LiteralPath $base -Directory -ErrorAction SilentlyContinue | ForEach-Object {
  if ($_.Name -match "^(a\d+_\d+)_") {
    $idx = $matches[1]
    if (-not $groups.ContainsKey($idx)) { $groups[$idx] = @() }
    $groups[$idx] += $_
  }
}

foreach ($idx in $groups.Keys) {
  $dirs = $groups[$idx]
  if ($dirs.Count -gt 1) {
    Warn "Duplicate index $idx found: $($dirs.Name -join ', ')"
    # Keep the first (alphabetically), delete the rest
    $keep = $dirs | Sort-Object Name | Select-Object -First 1
    $remove = $dirs | Where-Object { $_.FullName -ne $keep.FullName }
    foreach ($r in $remove) {
      Warn "Deleting duplicate directory: $($r.FullName)"
      Remove-Item -Recurse -Force $r.FullName
      git rm -r --cached --ignore-unmatch $r.FullName 2>$null | Out-Null
    }
    Good "Kept $($keep.Name), removed $($remove.Name -join ', ')"
  }
}

# 3) Stage deletions
Step "Staging deletions (if any)"
git add -A

# 4) Run pytest
Step "Running pytest"
pytest -q
if ($LASTEXITCODE -eq 0) {
  Step "Committing + pushing"
  git commit -m "Echoing Grotto: cleanup ghost + duplicate node directories"
  git push
} else {
  Warn "Tests failed; not committing. Inspect changes."
}
