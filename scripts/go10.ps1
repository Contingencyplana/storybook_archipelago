param([int]$Count = 10)
$ErrorActionPreference = 'Stop'
# Safety tag
$ts = Get-Date -Format 'yyyyMMdd-HHmmss'
$tag = "pre-reword-$Count-$ts"
& git tag $tag
& git push origin $tag | Out-Null

# Compute range: min(Count, total-1)
$env:GIT_PAGER = ''
$total = [int](& git rev-list --count HEAD)
if ($total -lt 2) { Write-Host 'Nothing to rewrite'; exit 0 }
$n = [Math]::Min($Count, $total - 1)

# Use absolute path to the msg-filter
$repo = (Resolve-Path .).Path
$filter = Join-Path $repo 'scripts/rewrite_msg_filter.ps1'
if (-not (Test-Path $filter)) { throw "Missing filter script: $filter" }

# Rewrite messages for the last N commits only
# Use HEAD~n..HEAD to include exactly the last n commits
& git filter-branch -f --msg-filter "pwsh -NoProfile -ExecutionPolicy Bypass -File `"$filter`"" HEAD~$n..HEAD
if ($LASTEXITCODE -ne 0) { throw "filter-branch failed ($LASTEXITCODE)" }

Write-Host "Rewritten last $n commits. Review with: git --no-pager log --oneline -n $Count"
Write-Host "Push with: git push --force-with-lease origin HEAD:master"
