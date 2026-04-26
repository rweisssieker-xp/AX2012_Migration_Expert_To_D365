param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("validate", "sample", "package", "test", "doctor")]
    [string]$Task
)

$ErrorActionPreference = "Stop"

switch ($Task) {
    "validate" {
        python .\axmigrate.py validate
    }
    "sample" {
        python .\axmigrate.py analyze .\plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv --output .\migration-analysis\sample
    }
    "test" {
        python -m unittest discover .\plugins\ax-to-d365fo-migration-expert\tests
    }
    "doctor" {
        python .\axmigrate.py doctor
    }
    "package" {
        $version = Get-Content .\VERSION -Raw
        $version = $version.Trim()
        $releaseRoot = "dist\ax-to-d365fo-migration-expert-$version"
        Remove-Item $releaseRoot -Recurse -Force -ErrorAction SilentlyContinue
        New-Item -ItemType Directory -Path "$releaseRoot\plugins" -Force | Out-Null
        New-Item -ItemType Directory -Path "$releaseRoot\.agents\plugins" -Force | Out-Null
        Copy-Item .\plugins\ax-to-d365fo-migration-expert "$releaseRoot\plugins" -Recurse
        Copy-Item .\.agents\plugins\marketplace.json "$releaseRoot\.agents\plugins\marketplace.json"
        Copy-Item .\DISTRIBUTION.md "$releaseRoot\INSTALL.md"
        Compress-Archive -Path "$releaseRoot\*" -DestinationPath "dist\ax-to-d365fo-migration-expert-$version.zip" -Force
    }
}
