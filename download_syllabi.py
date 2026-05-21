#!/usr/bin/env python3
"""Download Canvas course syllabi into a local year/quarter/course-code tree.

By default only the *current quarter's* courses (where you are the teacher) are
downloaded. Use --past to include previous quarters, --role to change the
enrollment filter, or --term to target a specific term by name.

Output layout:
    output/<year>/<quarter>/<COURSE_CODE>/syllabus.html
                                          syllabus.md         (if body present)
                                          page_<slug>.html    (matching Pages)
                                          page_<slug>.md
                                          metadata.json
                                          <any attached syllabus files>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import config
from canvas_client import (
    CanvasClient,
    quarter_from_month,
    term_is_current,
    term_year_quarter,
)


def slug(text):
    text = (text or "").strip()
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^A-Za-z0-9._-]", "", text)
    return text or "unknown"


def to_markdown(html):
    try:
        import html2text
    except ImportError:
        return None
    handler = html2text.HTML2Text()
    handler.body_width = 0
    return handler.handle(html)


def build_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--canvas-token", help="Canvas API token (overrides .env).")
    p.add_argument("--canvas-url", help="Canvas base URL (default: https://canvas.uw.edu).")
    p.add_argument(
        "--role",
        default="teacher",
        choices=["teacher", "ta", "student", "designer", "observer", "all"],
        help="Enrollment role to filter courses by (default: teacher).",
    )
    p.add_argument(
        "--past",
        "--all",
        dest="past",
        action="store_true",
        help="Include past quarters, not just the current one.",
    )
    p.add_argument(
        "--term",
        help="Only courses whose term name contains this text (e.g. 'Spring 2026').",
    )
    p.add_argument("--output", default="output", help="Output directory (default: output).")
    p.add_argument(
        "--no-files",
        action="store_true",
        help="Save only syllabus_body; skip downloading attached syllabus files.",
    )
    p.add_argument(
        "--no-pages",
        action="store_true",
        help="Skip searching course Pages for a syllabus page.",
    )
    p.add_argument("-v", "--verbose", action="store_true")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)

    client = CanvasClient(
        config.canvas_base_url(args.canvas_url),
        config.canvas_token(args.canvas_token),
    )

    print("Fetching courses from Canvas ...")
    courses = client.get_courses(args.role)
    if not courses:
        print("No courses returned. Check your token or --role filter.")
        return 1

    now = datetime.now(timezone.utc)
    current_yq = (str(now.year), quarter_from_month(now.month))
    out_root = Path(args.output)
    downloaded = 0

    for course in courses:
        term = course.get("term") or {}
        year, quarter = term_year_quarter(term)

        # ---- filtering -----------------------------------------------------
        if args.term:
            keep = args.term.lower() in (term.get("name") or "").lower()
        elif args.past:
            keep = True
        else:
            keep = term_is_current(term, now) or (year, quarter) == current_yq
        if not keep:
            continue

        code = slug(course.get("course_code") or course.get("name") or str(course["id"]))
        course_dir = out_root / year / quarter / code
        course_dir.mkdir(parents=True, exist_ok=True)

        body = course.get("syllabus_body") or ""
        (course_dir / "syllabus.html").write_text(body, encoding="utf-8")
        md = to_markdown(body) if body.strip() else None
        if md:
            (course_dir / "syllabus.md").write_text(md, encoding="utf-8")

        files_saved = []
        if not args.no_files:
            for f in client.search_syllabus_files(course["id"]):
                fname = slug(f.get("display_name") or f.get("filename") or "file")
                try:
                    client.download_file(f["url"], course_dir / fname)
                    files_saved.append(fname)
                except Exception as exc:  # noqa: BLE001 - best-effort per file
                    if args.verbose:
                        print(f"    ! could not download {fname}: {exc}")

        pages_saved = []
        if not args.no_pages:
            for pg in client.search_pages(course["id"]):
                try:
                    page_body = client.get_page_body(course["id"], pg["url"])
                except Exception as exc:  # noqa: BLE001 - best-effort per page
                    if args.verbose:
                        print(f"    ! could not fetch page '{pg.get('url')}': {exc}")
                    continue
                if not page_body.strip():
                    continue
                pslug = slug(pg.get("url") or pg.get("title") or "page")
                (course_dir / f"page_{pslug}.html").write_text(page_body, encoding="utf-8")
                page_md = to_markdown(page_body)
                if page_md:
                    (course_dir / f"page_{pslug}.md").write_text(page_md, encoding="utf-8")
                pages_saved.append(
                    {"title": pg.get("title"), "url": pg.get("url"),
                     "html_url": pg.get("html_url")}
                )

        meta = {
            "course_id": course["id"],
            "name": course.get("name"),
            "course_code": course.get("course_code"),
            "term": term.get("name"),
            "year": year,
            "quarter": quarter,
            "syllabus_url": f"{client.base_url}/courses/{course['id']}/assignments/syllabus",
            "has_syllabus_body": bool(body.strip()),
            "files": files_saved,
            "pages": pages_saved,
            "downloaded_at": now.isoformat(),
        }
        (course_dir / "metadata.json").write_text(
            json.dumps(meta, indent=2), encoding="utf-8"
        )

        status = "body" if body.strip() else "no-body"
        extra = ""
        if files_saved:
            extra += f" +{len(files_saved)} file(s)"
        if pages_saved:
            extra += f" +{len(pages_saved)} page(s)"
        print(f"  {year}/{quarter}/{code}  [{status}{extra}]  {course.get('name')}")
        downloaded += 1

    print(f"\nDone. {downloaded} syllabus folder(s) written under '{out_root}/'.")
    if downloaded == 0:
        print("Tip: try --past for previous quarters, or --term 'Spring 2026'.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
