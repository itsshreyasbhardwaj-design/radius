"""Thin wrappers over ``git``.

radius never imports a git library; it shells out so it works with whatever
git the developer already has. All paths returned are repo-root-relative POSIX
strings so they line up with the coverage map regardless of platform.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

_HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


class GitError(RuntimeError):
    """git was unavailable or returned non-zero."""


def _run(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def repo_root(start: Path | None = None) -> Path:
    start = start or Path.cwd()
    out = _run(["rev-parse", "--show-toplevel"], cwd=start)
    return Path(out.strip())


def head_sha(root: Path) -> str | None:
    try:
        return _run(["rev-parse", "HEAD"], cwd=root).strip()
    except GitError:
        return None  # unborn branch — no commits yet


def short_sha(root: Path, sha: str) -> str:
    try:
        return _run(["rev-parse", "--short", sha], cwd=root).strip()
    except GitError:
        return sha[:8]


def is_ancestor(root: Path, ancestor: str, descendant: str = "HEAD") -> bool:
    proc = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    return proc.returncode == 0


def commits_since(root: Path, base: str) -> int:
    try:
        out = _run(["rev-list", "--count", f"{base}..HEAD"], cwd=root).strip()
        return int(out or "0")
    except (GitError, ValueError):
        return 0


@dataclass(frozen=True)
class LineChange:
    """Which *old-file* lines a diff touched, and whether pure insertions exist.

    ``old_lines`` are line numbers in the version the map was built against, so
    they can be intersected directly with recorded coverage. ``pure_insertion``
    is True when a hunk adds lines that map to no old line — coverage from the
    old version cannot see that code, so the file must fall back to file-level
    selection to stay correct.
    """

    old_lines: frozenset[int]
    pure_insertion: bool


def changed_files(root: Path, base: str) -> dict[str, str]:
    """Return ``{path: status}`` for everything changed since ``base``.

    Status is a single letter: A(dded) M(odified) D(eleted) R(enamed). Renames
    yield both sides. Untracked files are reported as A so brand-new code is
    never silently ignored.
    """
    result: dict[str, str] = {}
    out = _run(["diff", "--name-status", "-M", base, "--"], cwd=root)
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0][0]
        if status == "R" and len(parts) >= 3:
            result[parts[1]] = "D"  # old path effectively removed
            result[parts[2]] = "A"  # new path effectively added
        else:
            result[parts[1]] = status
    for path in untracked_files(root):
        result.setdefault(path, "A")
    return result


def untracked_files(root: Path) -> list[str]:
    out = _run(["ls-files", "--others", "--exclude-standard"], cwd=root)
    return [p for p in out.splitlines() if p]


def line_changes(root: Path, base: str, path: str) -> LineChange:
    """Compute the :class:`LineChange` for a single modified file."""
    out = _run(["diff", "--unified=0", base, "--", path], cwd=root)
    old_lines: set[int] = set()
    pure_insertion = False
    for line in out.splitlines():
        m = _HUNK.match(line)
        if not m:
            continue
        old_start = int(m.group(1))
        old_len = 1 if m.group(2) is None else int(m.group(2))
        new_len = 1 if m.group(4) is None else int(m.group(4))
        if old_len > 0:
            old_lines.update(range(old_start, old_start + old_len))
        elif new_len > 0:
            # -0,0 +N,M : lines inserted where nothing existed before.
            pure_insertion = True
    return LineChange(frozenset(old_lines), pure_insertion)
