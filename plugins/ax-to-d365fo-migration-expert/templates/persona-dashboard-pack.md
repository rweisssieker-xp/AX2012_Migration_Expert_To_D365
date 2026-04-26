# Persona Dashboard Pack

## Zweck
Automatisch erstelltes Rollenpaket fuer AX zu D365FO Migrationen. Dieses Dokument fuehrt die zielgruppenspezifischen Reports fuer CEO, CIO, CISO, Projektleitung und Projektteam zusammen.

## Automatisch befuellte Quellen
- Analyzer-Reports aus `analyze`
- Risiko-, Aufwand-, Wellen- und Abhaengigkeitsdaten
- Security-, Architektur- und Datenqualitaetsflags
- Azure DevOps Work Items und Entscheidungsprotokolle

## Rollenansichten
| Rolle | Automatisch erzeugter Nutzen | Hauptartefakte |
| --- | --- | --- |
| CEO | Business Case, Risikoexposition, Werthebel, Entscheidungsbedarf | `persona-ceo-summary.md`, `board-ceo-narrative.md` |
| CIO | Architekturpfad, Integrationsrisiken, technische Schulden | `persona-cio-architecture-view.md` |
| CISO | Security Gates, Compliance, Datenschutz, Segregation of Duties | `persona-ciso-security-view.md`, `ciso-security-gate-pack.md` |
| Projektleitung | RAID, RACI, Status, Gate Readiness, Eskalationen | `persona-project-manager-control-view.md`, `weekly-status-report.md` |
| Projektteam | Sprintfaehige Aufgaben, Workshop-Fragen, Owner und Akzeptanzkriterien | `persona-team-member-task-view.md`, `team-execution-pack.md` |

## AI-KI-USP
Die AI-KI erstellt nicht nur Analyseergebnisse, sondern uebersetzt dieselben Fakten automatisch in die Sprache jeder Zielgruppe. Dadurch entstehen Board-, Security-, Architektur- und Delivery-Unterlagen ohne manuelles Umformatieren.
