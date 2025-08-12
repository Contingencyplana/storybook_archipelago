param([string]$TodoPath)
# Replace all 'pick' with 'reword' to prompt message edits for each commit in the range.
(Get-Content -LiteralPath $TodoPath) -replace '^pick\s','reword ' | Set-Content -LiteralPath $TodoPath -NoNewline
