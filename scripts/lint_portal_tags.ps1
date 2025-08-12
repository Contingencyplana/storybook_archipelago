$ErrorActionPreference = 'Stop'

# Purpose: Detect any closed-bracket [PORTAL: ... ] tags in Markdown files.
# Policy: Only the open form "[PORTAL:" (no closing ]) is allowed in prose.
# Behavior:
# - Prints a match count and up to 25 sample lines when violations exist
# - Exits with code 1 when violations are found; 0 when none; propagates rg errors

if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
    Write-Error 'ripgrep (rg) not found in PATH.'
    exit 2
}

$pattern = '\[PORTAL:[^\]]*\]'
$rgArgs = @(
    '-n',            # show line numbers
    '--hidden',      # include hidden files
    '--no-messages', # suppress rg noise
    '-g', '!**/.git/**',
    '-g', '*.[mM][dD]',
    '-P', $pattern,
    '.'
)

$hits = & rg @rgArgs
$code = $LASTEXITCODE

switch ($code) {
    0 {
        $arr = @($hits)
        Write-Host ("PortalTagMatches={0}" -f $arr.Count)
        # Show first 25 lines for quick fix targeting
        $arr | Select-Object -First 25 | ForEach-Object { Write-Host $_ }
        Write-Error 'Found closed-bracket portal tags. Use the open form "[PORTAL:" only.'
        exit 1
    }
    1 {
        Write-Host 'PortalTagMatches=0'
        Write-Host 'No closed-bracket [PORTAL:] tags found.'
        exit 0
    }
    default {
        Write-Error ("ripgrep error ({0})" -f $code)
        exit $code
    }
}
