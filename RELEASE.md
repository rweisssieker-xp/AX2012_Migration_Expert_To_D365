# Release Process

1. Update version in `plugins/ax-to-d365fo-migration-expert/.codex-plugin/plugin.json`.
2. Update `plugins/ax-to-d365fo-migration-expert/CHANGELOG.md`.
3. Run:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py doctor
python -m unittest discover plugins\ax-to-d365fo-migration-expert\tests
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
Copy-Item README.md "$releaseRoot\README.md"
Copy-Item docs "$releaseRoot\docs" -Recurse
Compress-Archive -Path "$releaseRoot\*" -DestinationPath "dist\ax-to-d365fo-migration-expert-$version.zip" -Force
```

5. Attach the ZIP to the GitHub release.

6. Release notes should state the validated scope:

- 92 skills.
- 264 templates.
- 49 Python scripts.
- 25 JSON configs.
- 46 analyzer outputs.
- Commerce/CXP/CRM/POS smoke tests.
- Solo/Master-Orchestrator smoke tests.
- Autonomous Governance & Evidence Intelligence smoke tests.
