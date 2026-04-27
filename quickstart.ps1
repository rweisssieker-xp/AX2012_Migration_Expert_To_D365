$ErrorActionPreference = "Stop"
python .\axmigrate.py validate
python .\axmigrate.py demo-projects --output demo-projects
Write-Host "Open demo-projects\commerce-pos\analysis\dashboard.html"
