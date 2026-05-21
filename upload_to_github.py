#!/usr/bin/env python3
"""Upload a local syllabus tree to a GitHub repository via the Contents API,
preserving the year/quarter/course-code directory structure.

Workflow:
    1. python download_syllabi.py            # writes ./output/...
    2. python upload_to_github.py            # commits ./output/... to the repo

Existing files are updated (commit with the current blob SHA); new files are
created. The target repository may be empty — the first upload will initialize
the branch.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import config


def build_parser():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--github-token", help="GitHub token (overrides .env).")
    p.add_argument("--repo", help="Target repo as owner/name (overrides .env).")
    p.add_argument("--branch", help="Branch to commit to (default: main).")
    p.add_argument(
        "--source", default="output", help="Local directory to upload (default: output)."
    )
    p.add_argument("--prefix", default="", help="Optional path prefix inside the repo.")
    p.add_argument(
        "--message", default="Add/update Canvas syllabi", help="Commit message per file."
    )
    p.add_argument(
        "--dry-run", action="store_true", help="List what would be uploaded; change nothing."
    )
    return p


def repo_path_for(file_path, source, prefix):
    rel = file_path.relative_to(source).as_posix()
    return f"{prefix.rstrip('/')}/{rel}" if prefix else rel


def main(argv=None):
    args = build_parser().parse_args(argv)

    source = Path(args.source)
    if not source.is_dir():
        print(f"Source '{source}' not found. Run download_syllabi.py first.")
        return 1

    files = sorted(f for f in source.rglob("*") if f.is_file())
    if not files:
        print(f"No files found under '{source}'.")
        return 1

    if args.dry_run:
        target = args.repo or "(repo from .env / GITHUB_REPO)"
        print(f"[dry-run] Would upload {len(files)} file(s) to {target}:")
        for f in files:
            print(f"  {repo_path_for(f, source, args.prefix)}")
        return 0

    from github import Auth, Github, GithubException

    gh = Github(auth=Auth.Token(config.github_token(args.github_token)))
    repo = gh.get_repo(config.github_repo(args.repo))
    branch = config.github_branch(args.branch)

    created = updated = errors = 0
    for f in files:
        path = repo_path_for(f, source, args.prefix)
        content = f.read_bytes()
        try:
            existing = repo.get_contents(path, ref=branch)
            repo.update_file(path, args.message, content, existing.sha, branch=branch)
            updated += 1
            print(f"  updated  {path}")
        except GithubException as exc:
            # 404: file does not exist. 409: repository/branch is empty.
            if exc.status in (404, 409):
                repo.create_file(path, args.message, content, branch=branch)
                created += 1
                print(f"  created  {path}")
            else:
                errors += 1
                msg = exc.data.get("message", exc) if isinstance(exc.data, dict) else exc
                print(f"  ! error  {path}: {msg}")

    print(
        f"\nDone. {created} created, {updated} updated"
        + (f", {errors} error(s)" if errors else "")
        + f" on {repo.full_name}@{branch}."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
