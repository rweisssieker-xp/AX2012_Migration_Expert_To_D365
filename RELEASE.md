# Release Process

1. Update version in `plugins/ax-to-d365fo-migration-expert/.codex-plugin/plugin.json`.
2. Update `plugins/ax-to-d365fo-migration-expert/CHANGELOG.md`.
3. Run:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

4. Build the distributable ZIP:

```powershell
        $version = Get-Content .\VERSION -Raw
        $version = $version.Trim()
$releaseRoot = "dist\ax-to-d365fo-migration-expert-$version"
Remove-Item $releaseRoot -Recurse -Force -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Path "$releaseRoot\plugins" -Force
New-Item -ItemType Directory -Path "$releaseRoot\.agents\plugins" -Force
Copy-Item plugins\ax-to-d365fo-migration-expert "$releaseRoot\plugins" -Recurse
Copy-Item .agents\plugins\marketplace.json "$releaseRoot\.agents\plugins\marketplace.json"
Copy-Item DISTRIBUTION.md "$releaseRoot\INSTALL.md"
Compress-Archive -Path "$releaseRoot\*" -DestinationPath "dist\ax-to-d365fo-migration-expert-$version.zip" -Force
```

5. Attach the ZIP to the GitHub release.
