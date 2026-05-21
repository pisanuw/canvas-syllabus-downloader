"""Minimal Canvas LMS REST API client — just what we need for syllabi.

Docs: https://canvas.instructure.com/doc/api/
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import requests

# Map words that appear in Canvas term names to canonical quarter slugs.
QUARTER_WORDS = {
    "winter": "winter",
    "spring": "spring",
    "summer": "summer",
    "autumn": "autumn",
    "fall": "autumn",
}


def _parse_dt(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def quarter_from_month(month):
    """Approximate UW quarter from a calendar month."""
    if month in (1, 2, 3):
        return "winter"
    if month in (4, 5, 6):
        return "spring"
    if month in (7, 8):
        return "summer"
    return "autumn"  # 9–12


def term_year_quarter(term):
    """Return (year, quarter) as strings for a Canvas term dict.

    Prefers the term *name* (e.g. "Spring 2026"), falling back to the term's
    start date, then to placeholders so output is never silently dropped.
    """
    term = term or {}
    name = term.get("name") or ""

    quarter = None
    for word, canonical in QUARTER_WORDS.items():
        if word in name.lower():
            quarter = canonical
            break

    match = re.search(r"(20\d{2})", name)
    year = match.group(1) if match else None

    start = _parse_dt(term.get("start_at"))
    if quarter is None and start:
        quarter = quarter_from_month(start.month)
    if year is None and start:
        year = str(start.year)

    return (year or "unknown-year", quarter or "unknown-quarter")


def term_is_current(term, now=None):
    """True if `now` falls within the term's [start_at, end_at] window."""
    now = now or datetime.now(timezone.utc)
    start = _parse_dt((term or {}).get("start_at"))
    end = _parse_dt((term or {}).get("end_at"))
    if start and now < start:
        return False
    if end and now > end:
        return False
    return start is not None or end is not None


class CanvasClient:
    def __init__(self, base_url, token, session=None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _paginate(self, path, params=None):
        params = dict(params or {})
        params.setdefault("per_page", 100)
        url = f"{self.base_url}/api/v1/{path.lstrip('/')}"
        while url:
            resp = self.session.get(url, params=params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                yield from data
            else:
                yield data
            # Canvas paginates via RFC 5988 Link headers.
            url = resp.links.get("next", {}).get("url")
            params = None  # the "next" URL already carries query params

    def get_courses(self, role=None):
        """List courses (current + concluded) with syllabus body and term info."""
        params = {
            "include[]": ["syllabus_body", "term"],
            "state[]": ["available", "completed"],
        }
        if role and role != "all":
            params["enrollment_type"] = role
        return list(self._paginate("courses", params))

    def search_syllabus_files(self, course_id):
        """Return file objects whose name matches 'syllabus' (may be empty)."""
        try:
            return list(
                self._paginate(f"courses/{course_id}/files", {"search_term": "syllabus"})
            )
        except requests.HTTPError:
            # Files tab may be disabled or forbidden for this course.
            return []

    def search_pages(self, course_id, search_term="syllabus"):
        """Return page summaries whose title matches `search_term` (no body)."""
        try:
            return list(
                self._paginate(f"courses/{course_id}/pages", {"search_term": search_term})
            )
        except requests.HTTPError:
            # Pages tab may be disabled or forbidden for this course.
            return []

    def get_page_body(self, course_id, page_url):
        """Fetch a single page's HTML body by its url slug (or page id)."""
        resp = self.session.get(
            f"{self.base_url}/api/v1/courses/{course_id}/pages/{page_url}", timeout=30
        )
        resp.raise_for_status()
        return resp.json().get("body") or ""

    def download_file(self, url, dest_path):
        resp = self.session.get(url, timeout=60)
        resp.raise_for_status()
        Path(dest_path).write_bytes(resp.content)
