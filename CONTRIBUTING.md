# Contributing

## Development Setup

Run validation from the repository root:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py validate
```

## Expected Checks

Before opening a pull request:

- Run the plugin validator.
- Keep generated output out of version control.
- Do not commit credentials, connection strings, PATs, bearer tokens, or customer data.
- Add or update tests when changing analyzer behavior.
- Update `CHANGELOG.md` for user-visible changes.

## Useful Commands

Analyze the sample inventory:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py analyze `
  plugins\ax-to-d365fo-migration-expert\examples\sample-ax-inventory.csv `
  --output migration-analysis\sample
```

Create a workspace:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py init "Sample Migration"
```

Export deliverables:

```powershell
python plugins\ax-to-d365fo-migration-expert\scripts\migration_cli.py export migration-analysis\sample --output migration-exports\sample
```

