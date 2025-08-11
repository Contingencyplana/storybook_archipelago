# Save as: C:\Users\Admin\storybook_archipelago\tools\ZipDragBadge.ps1
# Shortcut target:
# powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\Admin\storybook_archipelago\tools\ZipDragBadge.ps1"

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.IO.Compression.FileSystem

# Ensure STA (drag/drop & WinForms need it)
if ([Threading.Thread]::CurrentThread.ApartmentState -ne 'STA') {
  Write-Error 'This script must run in STA. Launch via the shortcut shown in the header.'
  exit 1
}

function New-Zip {
  param(
    [string]$Workspace,
    [string]$DistDir,
    [System.Windows.Forms.Label]$Status,
    [System.Windows.Forms.ProgressBar]$Bar,
    [ref]$OutZipPath,
    [ref]$WasGit,          # [bool] set to $true if git archive used
    [ref]$WasCanceled,     # [bool] set to $true if user canceled
    [ref]$ErrorText,       # [string] any final error
    [scriptblock]$IsCanceled # scriptblock returning $true when user hits Cancel
  )

  $WasGit.Value = $false
  $WasCanceled.Value = $false
  $ErrorText.Value = $null

  try {
    if (-not (Test-Path $DistDir)) { New-Item -ItemType Directory -Path $DistDir | Out-Null }
    $stamp = Get-Date -Format 'yyyyMMdd-HHmm'
    $zip   = Join-Path $DistDir ("storybook_archipelago-$stamp.zip")

    # Try git archive first (honors .gitattributes export-ignore)
    $Status.Text = "Using git archive (fast)…"
    $Bar.Style = 'Marquee'
    $Bar.MarqueeAnimationSpeed = 25
    $Bar.Value = 0
    $Status.Refresh()
    [Windows.Forms.Application]::DoEvents()

    $env:GIT_PAGER = ''
  $env:GIT_DIR = $null
  $env:GIT_WORK_TREE = $null
    git --no-pager -C $Workspace archive -o $zip --format zip --worktree-attributes HEAD 2>$null
    $code = $LASTEXITCODE

    if ($code -eq 0 -and (Test-Path $zip)) {
      $WasGit.Value = $true
      $OutZipPath.Value = $zip
      return
    }

    # Fallback: manual zip with progress & cancel
    if (Test-Path $zip) { Remove-Item -Force $zip }
    $Status.Text = "Gathering files…"
    $Bar.Style = 'Continuous'
    $Bar.Value = 0
  $Bar.Maximum = 100
  $Bar.Style = [System.Windows.Forms.ProgressBarStyle]::Continuous
    $Status.Refresh()
    [Windows.Forms.Application]::DoEvents()

    # Exclusions
    $exclude = {
      param($full)
      return ($full -match '\\\.git(\\|$)') -or
             ($full -match '\\\.venv(\\|$)') -or
             ($full -match '\\__pycache__(\\|$)') -or
             ($full -match '\\dist(\\|$)') -or
             ($full -match '\\\.vscode(\\|$)') -or
             ($full -match '\\\.github(\\|$)')
    }

    $all = Get-ChildItem -LiteralPath $Workspace -Force -Recurse -File |
      Where-Object { -not (& $exclude $_.FullName) }

    if (& $IsCanceled) { $WasCanceled.Value = $true; return }

    # Totals
    [long]$total = ($all | Measure-Object Length -Sum).Sum
    if (-not $total) { $total = 1 } # avoid div by zero
    [long]$done = 0
    $sw = [System.Diagnostics.Stopwatch]::StartNew()

    $Status.Text = "Creating ZIP (0%)…"
    $Status.Refresh()
    $Bar.Value = 0
    [Windows.Forms.Application]::DoEvents()

    $zipStream = [System.IO.File]::Open($zip, [System.IO.FileMode]::Create)
    try {
      $archive = New-Object System.IO.Compression.ZipArchive($zipStream, [System.IO.Compression.ZipArchiveMode]::Create, $true)
      try {
        foreach ($f in $all) {
          if (& $IsCanceled) { $WasCanceled.Value = $true; break }

          # Entry path relative to workspace (simpler & robust)
          $rel = [System.IO.Path]::GetRelativePath($Workspace, $f.FullName)

          $entry = $archive.CreateEntry($rel, [System.IO.Compression.CompressionLevel]::Optimal)
          $entry.LastWriteTime = $f.LastWriteTime

          # Copy with streaming to keep UI responsive
          $inStream  = $null
          $outStream = $null
          try {
            $inStream  = [System.IO.File]::OpenRead($f.FullName)
            $outStream = $entry.Open()
            $buf = New-Object byte[] 65536
            while (($read = $inStream.Read($buf,0,$buf.Length)) -gt 0) {
              if (& $IsCanceled) { $WasCanceled.Value = $true; break }
              $outStream.Write($buf,0,$read)
              $done += $read

              # UI update ~every 80ms
              if ($sw.ElapsedMilliseconds -ge 80) {
                $pct = [math]::Min(100,[math]::Round(100.0*$done/$total,1))
                $mb  = "{0:N1}" -f ($done/1MB)

                $Status.Text = "Creating ZIP ($pct%)… ($mb MB)"
                $Bar.Value = [int]([Math]::Min(100,[Math]::Max(0,$pct)))
                $Status.Refresh()
                [Windows.Forms.Application]::DoEvents()
                $sw.Restart()
              }
            }
          } finally {
            $inStream?.Close()
            $outStream?.Close()
          }
        }

        if ($WasCanceled.Value) {
          try { $archive.Dispose() } catch {}
          try { $zipStream.Close() } catch {}
          Remove-Item -Force $zip -ErrorAction SilentlyContinue
          return
        }
      } finally {
        $archive.Dispose()
      }
    } finally {
      $zipStream.Close()
    }

    if (-not (Test-Path $zip)) {
      $ErrorText.Value = "Failed to create ZIP file."
    } else {
      $OutZipPath.Value = $zip
    }
  } catch {
    $ErrorText.Value = $_.ToString()
  }
}
