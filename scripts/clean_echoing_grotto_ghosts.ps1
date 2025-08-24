# scripts/clean_echoing_grotto_ghosts.ps1
# Removes truly empty Echoing Grotto node directories; does not touch non-empty.

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Step($m){ Write-Host "==> $m" -ForegroundColor Cyan }
try { $root = (git rev-parse --show-toplevel).Trim() } catch { $root = (Get-Location).Path }
Set-Location $root
Step "Repo root: $root"

$base = Join-Path $root "a0_0_sailing_mode\a1_2_echoing_grotto_minigame"
if (-not (Test-Path $base)) { Write-Host "Nothing to do."; exit 0 }

$nodes = Get-ChildItem -LiteralPath $base -Directory | Where-Object { $_.Name -match '^a0_[0-2]_.+_node$' }
foreach ($n in $nodes) {
  $files = Get-ChildItem -LiteralPath $n.FullName -File -ErrorAction SilentlyContinue
  if (-not $files) {
    Step "Removing empty: $($n.FullName)"
    Remove-Item -Recurse -Force $n.FullName
  }
}

Step "Staging deletions (if any)"
git add -A
$st = git diff --cached --name-only
if ([string]::IsNullOrWhiteSpace($st)) {
  Write-Host "Nothing to commit."
} else {
  Step "Running pytest"
  pytest -q
  if ($LASTEXITCODE -eq 0) {
    Step "Committing + pushing"
    git commit -m "Echoing Grotto: remove empty ghost node directories"
    git push
  } else {
    Write-Host "Tests failed; not committing." -ForegroundColor Yellow
  }
}
