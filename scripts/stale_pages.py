"""List handbook pages whose last_reviewed date is older than 90 days (or missing)."""
import datetime as dt
import pathlib
import re

DAYS = 90
today = dt.date.today()
stale = []

for page in sorted(pathlib.Path("docs").rglob("*.md")):
    if page.name.startswith("_") or page.name in {"index.md", "updates.md", "disclaimer.md"}:
        continue
    m = re.search(r"^last_reviewed:\s*(\d{4}-\d{2}-\d{2})", page.read_text(encoding="utf-8"), re.M)
    if not m:
        stale.append((page, "missing"))
        continue
    reviewed = dt.date.fromisoformat(m.group(1))
    age = (today - reviewed).days
    if age > DAYS:
        stale.append((page, f"{reviewed} ({age} days)"))

print("## Pages to review\n")
if stale:
    for page, note in stale:
        print(f"- [ ] `{page}` — last reviewed {note}")
else:
    print("All pages were reviewed in the last 90 days.")
print("\nCheck new ACC/AHA, HRS, IDSA, ADA, KDIGO, GOLD, and ABIM blueprint changes. "
      "Log each change in `docs/updates.md`.")
