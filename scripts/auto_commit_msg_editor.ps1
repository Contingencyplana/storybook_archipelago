param([string]$MsgPath)
$ErrorActionPreference = 'Stop'

# Load mapping file if present
$mapPath = Join-Path $PSScriptRoot 'commit_messages_map_by_subject.json'
$map = $null
if (Test-Path $mapPath) {
  try { $map = Get-Content -Raw -LiteralPath $mapPath | ConvertFrom-Json } catch { $map = $null }
}

# Read existing message (subject + optional body)
$old = Get-Content -Raw -LiteralPath $MsgPath
$lines = $old -split "\r?\n"
$subject = $lines[0]
$body = if ($lines.Length -gt 1) { ($lines[1..($lines.Length-1)] -join "`n") } else { '' }

# Prefer explicit mapping; otherwise keep CC-style subjects; otherwise fallback prefix
$newSubject = $null
if ($null -ne $map) { $newSubject = $map.$subject }
if (-not $newSubject) {
  if ($subject -match '^(feat|fix|docs|ci|chore|refactor|test|build|perf|revert)(\(.+\))?: ') {
    $newSubject = $subject
  } else {
    $newSubject = 'chore(repo): ' + $subject
  }
}

$new = if ([string]::IsNullOrEmpty($body)) { $newSubject } else { $newSubject + "`n" + $body }
Set-Content -LiteralPath $MsgPath -Value $new
