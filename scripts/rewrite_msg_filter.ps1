$ErrorActionPreference = 'Stop'
# Reads the original commit message from STDIN, rewrites subject with mapping or fallback, writes to STDOUT.

# Read full message from stdin
$old = [Console]::In.ReadToEnd()
if (-not $old) {
    exit 0
}
$lines = $old -split "\r?\n"
$subject = $lines[0]
$body = if ($lines.Length -gt 1) { ($lines[1..($lines.Length-1)] -join "`n") } else { '' }

# Load mapping by exact subject if available
$mapPath = Join-Path $PSScriptRoot 'commit_messages_map_by_subject.json'
$mapping = $null
if (Test-Path $mapPath) {
    try { $mapping = Get-Content -Raw -LiteralPath $mapPath | ConvertFrom-Json } catch { $mapping = $null }
}

$newSubject = $null
if ($mapping -ne $null) {
    $newSubject = $mapping.$subject
}

# If not mapped, keep if already looks like Conventional Commits
if (-not $newSubject) {
    if ($subject -match '^(feat|fix|docs|ci|chore|refactor|test|build|perf|revert)(\(.+\))?: ') {
        $newSubject = $subject
    } else {
        $newSubject = "chore(repo): " + $subject
    }
}

# Emit the new message
if ([string]::IsNullOrEmpty($body)) {
    [Console]::Out.Write($newSubject)
} else {
    [Console]::Out.Write($newSubject + "`n" + $body)
}
