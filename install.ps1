param(
  [string]$Target = "."
)

$ErrorActionPreference = "Stop"
Write-Host "AX to D365FO Migration Expert install check"
python .\axmigrate.py doctor
python .\axmigrate.py validate
Write-Host "Plugin is ready in $((Resolve-Path $Target).Path)"
