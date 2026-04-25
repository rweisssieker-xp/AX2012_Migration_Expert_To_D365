# Security Policy

## Supported Versions

The current supported version is the latest release on the default branch.

## Reporting a Vulnerability

Do not open public issues for vulnerabilities involving credentials, customer data, or connector behavior.

Report privately to:

```text
migration-expert@example.org
```

## Secrets Handling

The plugin expects external credentials through environment variables only:

- `AX_SQL_CONNECTION_STRING`
- `AZDO_ORG_URL`
- `AZDO_PROJECT`
- `AZDO_PAT`
- `LCS_BASE_URL`
- `LCS_BEARER_TOKEN`
- `D365FO_BASE_URL`
- `D365FO_BEARER_TOKEN`

Never commit real customer inventory, telemetry, SQL exports, tokens, or generated analysis outputs.

