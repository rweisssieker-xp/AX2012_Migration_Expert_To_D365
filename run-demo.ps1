param(
  [string]$Output = "demo-projects"
)

$ErrorActionPreference = "Stop"
python .\axmigrate.py demo-projects --output $Output
Write-Host "Dashboards generated under $Output"
