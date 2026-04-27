#!/usr/bin/env python3
"""Generate a local HTML command-center UI for wizard, gates, demos, and command launch guidance."""

from __future__ import annotations

import argparse
from pathlib import Path


PROFILES = ["ax40", "ax2009", "ax2012", "finance", "manufacturing", "commerce", "crm", "pos", "solo", "multi-country", "corporate-rollout"]


def html() -> str:
    options = "\n".join(f"<option value=\"{profile}\">{profile}</option>" for profile in PROFILES)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AX to D365FO Migration Autonomy UI</title>
  <style>
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: #f4f7fa; color: #172033; }}
    header {{ background: #17446b; color: white; padding: 24px 32px; }}
    main {{ padding: 24px 32px; display: grid; gap: 18px; }}
    section {{ background: white; border: 1px solid #d9e2ec; border-radius: 8px; padding: 18px; }}
    label {{ display: block; font-weight: 600; margin: 12px 0 6px; }}
    input, select {{ width: 100%; max-width: 720px; padding: 10px; border: 1px solid #aebdca; border-radius: 6px; }}
    button {{ margin-top: 14px; padding: 10px 14px; border: 0; border-radius: 6px; background: #0f5f8f; color: white; font-weight: 600; }}
    pre {{ background: #101820; color: #e8f1f8; padding: 14px; border-radius: 8px; overflow: auto; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; }}
  </style>
</head>
<body>
  <header><h1>Migration Autonomy UI</h1><p>Wizard, router, evidence gates, demos and exports as copy-ready local commands.</p></header>
  <main>
    <section>
      <h2>Project Wizard</h2>
      <label>Project name</label><input id="project" value="Contoso AX Migration">
      <label>Profile</label><select id="profile">{options}</select>
      <button onclick="build()">Generate commands</button>
      <pre id="commands"></pre>
    </section>
    <div class="grid">
      <section><h2>Evidence Gates</h2><pre>python .\\axmigrate.py evidence-gates migration-analysis\\sample --ciso-approval yes --cutover-rehearsal yes --finance-reconciliation yes --uat-signoff yes --rollback-plan yes --output evidence-gates\\sample</pre></section>
      <section><h2>Router</h2><pre>python .\\axmigrate.py orchestrate migration-analysis\\sample --output orchestration\\sample</pre></section>
      <section><h2>Memory Store</h2><pre>python .\\axmigrate.py memory-store migration-analysis\\sample --project "Contoso AX Migration" --output migration-memory-store\\sample</pre></section>
      <section><h2>Security Scan</h2><pre>python .\\axmigrate.py security-scan migration-analysis\\sample --output security-scan\\sample</pre></section>
    </div>
  </main>
  <script>
    function slug(v) {{ return v.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'migration-project'; }}
    function build() {{
      const p = document.getElementById('project').value;
      const profile = document.getElementById('profile').value;
      const s = slug(p);
      document.getElementById('commands').textContent = [
        `python .\\\\axmigrate.py wizard --profile ${{profile}} --project "${{p}}" --output migration-wizard\\\\${{s}}`,
        `python .\\\\axmigrate.py demo-projects --output demo-projects`,
        `python .\\\\axmigrate.py orchestrate migration-wizard\\\\${{s}} --output orchestration\\\\${{s}}`,
        `python .\\\\axmigrate.py evidence-gates migration-wizard\\\\${{s}} --output evidence-gates\\\\${{s}}`,
        `python .\\\\axmigrate.py memory-store migration-wizard\\\\${{s}} --project "${{p}}" --output migration-memory-store\\\\${{s}}`
      ].join('\\n');
    }}
    build();
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="migration-ui")
    args = parser.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "project-wizard.html").write_text(html(), encoding="utf-8")
    print(f"Generated project UI into {(output / 'project-wizard.html').resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
