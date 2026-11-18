"""Print a Markdown checklist of chapters whose `reviewed:` date is older than 90 days."""
import re
from datetime import date, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
cutoff = date.today() - timedelta(days=90)
rows = []
for f in sorted((ROOT / "content").glob("*/*.md")):
    if f.parent.name == "tools":
        continue
    m = re.match(r"^---\n(.*?)\n---\n", f.read_text(encoding="utf-8"), re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    rev = fm.get("reviewed")
    if isinstance(rev, str):
        rev = date.fromisoformat(rev)
    if not rev or rev < cutoff:
        rows.append(f"- [ ] **{fm.get('title', f.stem)}** (`{f.relative_to(ROOT)}`) — last reviewed {rev or 'never'}")

print("Check new guidelines (ACC/AHA, ESC, IDSA, ATS, ADA, AASLD, ACG, KDIGO, SCCM, AHA/ASA), update the chapter, change `reviewed:`, and add a line to `content/tools/guideline-watch.md`.\n")
print("\n".join(rows) if rows else "All chapters were reviewed in the last 90 days. ✅")
