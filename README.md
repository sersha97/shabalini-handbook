# Hospitalist Handbook

Source for **shabalini.com/handbook** — a practical hospital medicine handbook for the wards and ABIM boards. Educational use only; not medical advice.

## Add or update a page

1. Copy `docs/_template.md` into the right system folder (for example `docs/cardiology/heart-failure.md`).
2. Fill in the sections. Set `last_reviewed` to today.
3. Add the page to `nav:` in `mkdocs.yml`.
4. Add one line to `docs/updates.md`.
5. Commit to `main`. GitHub Actions builds the site and uploads it.

You can edit directly on github.com (pencil icon) — no install needed.

## Preview on your computer (optional)

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000.

## One-time deploy setup

In GitHub: **Settings → Secrets and variables → Actions → New repository secret**. Add:

| Secret | Value |
|---|---|
| `FTP_SERVER` | FTP host from ADM.TOOLS |
| `FTP_USERNAME` | FTP user |
| `FTP_PASSWORD` | FTP password |
| `FTP_SERVER_DIR` | Server folder for `/handbook/`, ending in `/` (for example `/shabalini.com/www/handbook/`) |

## Automations

- **deploy.yml** — builds on every push and PR; deploys from `main`.
- **quarterly-review.yml** — opens a review issue on Jan 1, Apr 1, Jul 1, Oct 1 listing pages not reviewed in 90 days.
