$ErrorActionPreference = "Stop"
$version = (Get-Content .\VERSION -Raw).Trim()
$releaseRoot = "dist\ax-to-d365fo-migration-expert-$version"
Remove-Item $releaseRoot -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$releaseRoot\plugins" -Force | Out-Null
New-Item -ItemType Directory -Path "$releaseRoot\.agents\plugins" -Force | Out-Null
Copy-Item plugins\ax-to-d365fo-migration-expert "$releaseRoot\plugins" -Recurse
Copy-Item .agents\plugins\marketplace.json "$releaseRoot\.agents\plugins\marketplace.json"
Copy-Item DISTRIBUTION.md "$releaseRoot\INSTALL.md"
Copy-Item README.md "$releaseRoot\README.md"
Copy-Item docs "$releaseRoot\docs" -Recurse
Compress-Archive -Path "$releaseRoot\*" -DestinationPath "dist\ax-to-d365fo-migration-expert-$version.zip" -Force
Write-Host "Built dist\ax-to-d365fo-migration-expert-$version.zip"
