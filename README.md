# canvas-syllabus-downloader

Two small Python programs:

1. **`download_syllabi.py`** — pulls course syllabi from Canvas into a local
   `output/<year>/<quarter>/<COURSE_CODE>/` tree.
2. **`upload_to_github.py`** — commits that tree to a GitHub repository, keeping
   the same directory structure.

They run independently, so you can inspect/curate downloads before publishing.

---

## What gets downloaded

For each matching course:

```
output/2026/spring/CSE_142_A/
├── syllabus.html      # the Canvas "Syllabus" body (raw HTML)
├── syllabus.md        # Markdown rendering of the same (if body is non-empty)
├── metadata.json      # course id, name, code, term, source URL, timestamp
└── <attached files>   # any course file whose name matches "syllabus" (e.g. a PDF)
```

`year` and `quarter` come from the Canvas **term** (e.g. `Spring 2026`), falling
back to the term's start date, then a UW month-based heuristic.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # then fill in your tokens
```

### Secrets

Secrets resolve in this order: **CLI flag → environment variable → `.env` in the
current directory**. Nothing is hardcoded. `.env` is git-ignored.

| Variable           | Used by              | Notes                                            |
| ------------------ | -------------------- | ------------------------------------------------ |
| `CANVAS_API_TOKEN` | download             | Canvas → Account → Settings → **+ New Access Token** |
| `CANVAS_BASE_URL`  | download (optional)  | Defaults to `https://canvas.uw.edu`              |
| `GITHUB_TOKEN`     | upload               | Fine-grained PAT, **Contents: Read and write** on the repo |
| `GITHUB_REPO`      | upload               | `owner/name`, e.g. `pisanuw/canvas-syllabus-downloader` |
| `GITHUB_BRANCH`    | upload (optional)    | Defaults to `main`                               |

---

## Usage

### Download (current quarter, teacher role — the default)

```bash
python download_syllabi.py
```

### Common variations

```bash
python download_syllabi.py --past                  # include all previous quarters
python download_syllabi.py --term "Spring 2026"    # one specific term
python download_syllabi.py --role student          # courses you're enrolled in
python download_syllabi.py --role all              # any enrollment role
python download_syllabi.py --no-files              # skip attached files, body only
python download_syllabi.py --canvas-token XXXX     # token via flag instead of .env
python download_syllabi.py --output ~/syllabi -v   # custom dir, verbose
```

### Upload to GitHub

```bash
python upload_to_github.py --dry-run               # preview the file list first
python upload_to_github.py                         # commit ./output to the repo
python upload_to_github.py --prefix syllabi        # nest everything under syllabi/
python upload_to_github.py --branch main --message "Spring 2026 syllabi"
```

The uploader updates existing files (so re-running is idempotent) and can
initialize an **empty** repository on the first push.

### End to end

```bash
python download_syllabi.py --term "Spring 2026"
python upload_to_github.py --message "Spring 2026 syllabi"
```

---

## Notes & limitations

- "Syllabus" means the Canvas syllabus **body** plus course files named like
  *syllabus*. If your syllabus lives elsewhere (a Page, a module item), point
  `--role`/`--term` as needed or extend `canvas_client.py`.
- A course with an empty syllabus body still produces a folder + `metadata.json`
  (`has_syllabus_body: false`) so you can see what was checked.
- The "current quarter" detection uses Canvas term dates when present; if a term
  has no dates set, it falls back to matching the current UW quarter by month.
- This project never stores your tokens. **Treat any token pasted into a chat,
  email, or shell history as compromised and rotate it.**
