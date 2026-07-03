"""git helpers, exercised against real throwaway repositories."""

from __future__ import annotations

import os
import subprocess

import pytest

from radius import gitutil

_ENV = {
    **os.environ,
    "GIT_AUTHOR_NAME": "t",
    "GIT_AUTHOR_EMAIL": "t@example.com",
    "GIT_COMMITTER_NAME": "t",
    "GIT_COMMITTER_EMAIL": "t@example.com",
}

FIVE_LINES = "a = 1\nb = 2\nc = 3\nd = 4\ne = 5\n"


def _git(root, *args):
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, env=_ENV)


@pytest.fixture
def repo(tmp_path):
    _git(tmp_path, "init", "-q")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.py").write_text(FIVE_LINES)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "c0")
    return tmp_path, gitutil.head_sha(tmp_path)


def test_changed_files_tracks_modifications_and_untracked(repo):
    root, c0 = repo
    (root / "src" / "a.py").write_text("a = 1\nb = 2\nc = 33\nd = 4\ne = 5\n")
    (root / "extra.txt").write_text("hi")
    cf = gitutil.changed_files(root, c0)
    assert cf.get("src/a.py") == "M"
    assert cf.get("extra.txt") == "A"


def test_line_changes_modification(repo):
    root, c0 = repo
    (root / "src" / "a.py").write_text("a = 1\nb = 2\nc = 33\nd = 4\ne = 5\n")
    lc = gitutil.line_changes(root, c0, "src/a.py")
    assert 3 in lc.old_lines
    assert lc.pure_insertion is False


def test_line_changes_detects_pure_insertion(repo):
    root, c0 = repo
    (root / "src" / "a.py").write_text("a = 1\nb = 2\nx = 9\nc = 3\nd = 4\ne = 5\n")
    lc = gitutil.line_changes(root, c0, "src/a.py")
    assert lc.pure_insertion is True


def test_is_ancestor_and_commits_since(repo):
    root, c0 = repo
    assert gitutil.is_ancestor(root, c0, "HEAD")
    (root / "src" / "a.py").write_text("a = 1\nb = 2\nc = 33\nd = 4\ne = 5\n")
    _git(root, "add", "-A")
    _git(root, "commit", "-qm", "c1")
    assert gitutil.commits_since(root, c0) == 1
