"""pytest adapter — the reference implementation.

Builds a per-test coverage map using pytest-cov's test contexts, which are
labelled with the exact pytest node id (``path::test``). That means the map
keys, ``--collect-only`` output, and the ids we hand back to pytest all speak
the same language, with no fragile label reconciliation.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from ..config import Config


def _py() -> str:
    return sys.executable or "python3"


def _rel(root: Path, raw: str) -> str | None:
    """Normalise a coverage path to a repo-root-relative POSIX string."""
    p = Path(raw)
    if not p.is_absolute():
        p = (root / p).resolve()
    else:
        p = p.resolve()
    try:
        return p.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None  # outside the repo (e.g. site-packages) — ignore


def map_from_coverage_json(data: dict, root: Path) -> dict[str, dict]:
    """Invert coverage.py's context JSON into ``{test_id: {"files": {...}}}``.

    Pure and I/O-free so it can be unit-tested against fixture JSON.
    """
    tests: dict[str, dict] = {}
    for raw_path, fdata in data.get("files", {}).items():
        rel = _rel(root, raw_path)
        if rel is None:
            continue
        contexts: dict[str, list[str]] = fdata.get("contexts", {})
        for lineno, ctx_list in contexts.items():
            try:
                line = int(lineno)
            except (TypeError, ValueError):
                continue
            for ctx in ctx_list:
                test_id = ctx.rsplit("|", 1)[0] if "|" in ctx else ctx
                if "::" not in test_id:
                    continue  # import-time / empty context, not a test
                files = tests.setdefault(test_id, {"files": {}})["files"]
                files.setdefault(rel, []).append(line)
    for entry in tests.values():
        for path, lines in entry["files"].items():
            entry["files"][path] = sorted(set(lines))
    return tests


class PytestAdapter:
    name = "pytest"

    def _cov_sources(self, root: Path, config: Config) -> list[str]:
        srcs = [sp for sp in config.source_paths if (root / sp).exists()]
        return srcs or ["."]

    def _existing_test_paths(self, root: Path, config: Config) -> list[str]:
        return [tp for tp in config.test_paths if (root / tp).exists()]

    def is_available(self, root: Path, config: Config) -> bool:
        try:
            subprocess.run(
                [_py(), "-c", "import pytest"],
                cwd=str(root),
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
        return bool(self._existing_test_paths(root, config))

    def collect_tests(self, root: Path, config: Config) -> list[str]:
        paths = self._existing_test_paths(root, config)
        proc = subprocess.run(
            [_py(), "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider", *paths],
            cwd=str(root),
            capture_output=True,
            text=True,
        )
        ids: list[str] = []
        for line in proc.stdout.splitlines():
            line = line.strip()
            if "::" in line and not line.startswith("<"):
                ids.append(line)
        return ids

    def build_map(self, root: Path, config: Config) -> dict[str, dict]:
        try:
            subprocess.run(
                [_py(), "-c", "import coverage, pytest_cov"],
                cwd=str(root),
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            raise RuntimeError(
                "The pytest adapter needs 'coverage' and 'pytest-cov'. "
                "Install with:  pip install radius-tia[pytest]"
            ) from exc

        paths = self._existing_test_paths(root, config)
        cov_args = [f"--cov={s}" for s in self._cov_sources(root, config)]
        with tempfile.TemporaryDirectory() as tmp:
            data_file = str(Path(tmp) / ".coverage")
            json_file = Path(tmp) / "coverage.json"
            env = {**os.environ, "COVERAGE_FILE": data_file}
            subprocess.run(
                [
                    _py(), "-m", "pytest",
                    *cov_args,
                    "--cov-context=test",
                    "--cov-report=",  # suppress; we produce our own JSON
                    "-p", "no:cacheprovider",
                    *paths,
                ],
                cwd=str(root),
                env=env,
            )
            subprocess.run(
                [
                    _py(), "-m", "coverage", "json",
                    "--data-file", data_file,
                    "--show-contexts",
                    "-o", str(json_file),
                ],
                cwd=str(root),
                env=env,
                check=True,
            )
            data = json.loads(json_file.read_text(encoding="utf-8"))
        return map_from_coverage_json(data, root)

    def run(self, root: Path, config: Config, test_ids: list[str] | None) -> int:
        if test_ids is None:
            targets = self._existing_test_paths(root, config)
        elif not test_ids:
            return 0  # nothing to run — a clean pass
        else:
            targets = test_ids
        proc = subprocess.run(
            [_py(), "-m", "pytest", "-p", "no:cacheprovider", *targets],
            cwd=str(root),
        )
        return proc.returncode
