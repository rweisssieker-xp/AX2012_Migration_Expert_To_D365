# Erweiterte AI/KI Control Features

Dieses Dokument beschreibt die 12 erweiterten AI/KI-Control-Features oberhalb von Guided Run, Health Snapshot und USP Pack. Jedes Feature hat ein eigenes CLI-Kommando, erzeugte Artefakte und Validator-Abdeckung.

## Kommandos

| Feature | Kommando | Hauptoutputs | Zweck |
| --- | --- | --- | --- |
| USP-to-Action Engine | `usp-actions` | `usp-to-action-map.md`, `usp-to-action-map.json` | Uebersetzt USPs in konkrete Skills, Kommandos, Proof-Artefakte und Demo-Narrative. |
| Project Truth Detector | `truth-detector` | `project-truth-detector.md`, `project-truth-detector.json` | Vergleicht behaupteten Projektstatus mit vorhandener Evidence, Gates, Tests und Artefakten. |
| Cutover Confidence Engine | `cutover-confidence` | `cutover-confidence-score.md`, `cutover-confidence-score.json` | Bewertet Go-live-Vertrauen aus Rehearsal, Rollback, Smoke Tests, Finance, Security und Commerce/POS-Signalen. |
| AI Meeting-to-Migration Actions | `meeting-actions` | `meeting-to-migration-actions.md`, `meeting-to-migration-actions.csv` | Wandelt Notizen in Entscheidungen, Risiken, Aufgaben, Evidence-Gaps, Owner und naechste Kommandos um. |
| AI Proposal / Sales Pack Generator | `proposal-pack` | `proposal-sales-pack.md`, `proposal-sales-pack.html` | Erzeugt eine sales-faehige Migrationsstory aus USPs, Demos, Health und Analyse-Signalen. |
| AI Role Prompt Packs 2.0 | `role-prompt-pack` | `role-prompt-pack-2.md`, `role-prompt-pack-2.json` | Generiert rollenbasierte Prompts fuer CEO, CIO, CISO, CFO, PMO, QA und Key User. |
| Evidence Freshness Monitor | `evidence-freshness` | `evidence-freshness-monitor.md`, `evidence-freshness-monitor.json` | Klassifiziert Evidence als aktuell, alternd, veraltet oder fehlend. |
| Dependency Risk Graph | `dependency-risk-graph` | `dependency-risk-graph.md`, `dependency-risk-graph.json` | Visualisiert Abhaengigkeiten zwischen Workstreams, Gates, Tests, Integrationen und Cutover. |
| Partner Deliverable Checker | `partner-deliverable-check` | `partner-deliverable-check.md`, `partner-deliverable-check.json` | Prueft Partner-Lieferobjekte, Scope-Kontrolle, Evidence, Meilensteine und Sign-offs. |
| Release ZIP Builder | `release-pack` | `release-pack-manifest.md`, `ax-to-d365fo-migration-expert-release.zip` | Baut ein verteilbares Plugin-ZIP und ein Release-Manifest. |
| Demo Portal 2.0 | `demo-portal` | `demo-portal-2.md`, `demo-portal-2.html` | Verlinkt Guided Runs, Health Snapshots, USP Packs, Demo-Dashboards und Pitch-Story. |
| Interactive Local Wizard UI 2.0 | `wizard-ui` | `wizard-ui-2.md`, `interactive-wizard-ui-2.html` | Liefert eine lokale HTML-Oberflaeche fuer Projektart, Gates, Evidence, Packs und Kommandos. |

## Beispiel

```powershell
python .\axmigrate.py truth-detector guided-runs\sample --project "Contoso AX Migration" --output truth\sample
python .\axmigrate.py cutover-confidence guided-runs\sample --project "Contoso AX Migration" --output cutover-confidence\sample
python .\axmigrate.py demo-portal guided-runs\sample --project "Contoso AX Migration" --output demo-portal\sample
```

## Betriebsmodell

Diese Kommandos machen das Plugin staerker zu einem Migration-Control-System statt nur zu einem Reportgenerator. Sie nutzen lokale Project Evidence und erzeugte Artefakte, um bessere Entscheidungen fuer Management, PMO, Security, Finance, Delivery, Testing, Partner und Sales zu liefern.
