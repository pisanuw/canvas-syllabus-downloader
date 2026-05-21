"""Shared configuration / secret loading for canvas-syllabus-downloader.

Resolution order for every value:
    explicit CLI argument  >  environment variable  >  default

Environment variables are read from the real environment *and* from a `.env`
file in the current working directory (loaded automatically below). Secrets are
never written to disk by this project and never passed on the command line in a
way that would store them in shell history unless you choose to do so.
"""
from __future__ import annotations

import os

from dotenv import load_dotenv

# Load a .env file from the current working directory, if one exists.
load_dotenv()

DEFAULT_CANVAS_BASE_URL = "https://canvas.uw.edu"
DEFAULT_GITHUB_BRANCH = "main"


def _first(*values):
    """Return the first truthy value, else None."""
    for value in values:
        if value:
            return value
    return None


def canvas_token(cli_value=None):
    token = _first(cli_value, os.getenv("CANVAS_API_TOKEN"), os.getenv("CANVAS_TOKEN"))
    if not token:
        raise SystemExit(
            "No Canvas token found. Put CANVAS_API_TOKEN in .env (see .env.example) "
            "or pass --canvas-token."
        )
    return token


def canvas_base_url(cli_value=None):
    return _first(cli_value, os.getenv("CANVAS_BASE_URL"), DEFAULT_CANVAS_BASE_URL)


def github_token(cli_value=None):
    token = _first(cli_value, os.getenv("GITHUB_TOKEN"), os.getenv("GH_TOKEN"))
    if not token:
        raise SystemExit(
            "No GitHub token found. Put GITHUB_TOKEN in .env (see .env.example) "
            "or pass --github-token."
        )
    return token


def github_repo(cli_value=None):
    repo = _first(cli_value, os.getenv("GITHUB_REPO"))
    if not repo:
        raise SystemExit(
            "No GitHub repo found. Put GITHUB_REPO=owner/name in .env or pass --repo."
        )
    return repo


def github_branch(cli_value=None):
    return _first(cli_value, os.getenv("GITHUB_BRANCH"), DEFAULT_GITHUB_BRANCH)
