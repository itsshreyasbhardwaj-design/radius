"""Decide which tests a diff can affect.

This module is pure and side-effect free: it takes a coverage map, a set of
changed files, and (optionally) line-level change info, and returns the set of
tests to run with a human-readable reason for each. Everything git- or
runner-specific lives elsewhere so this logic can be unit-tested exhaustively.

Correctness posture: when in doubt, select more. A false negative (skipping a
test that should have run) is the one unacceptable failure, so every ambiguous
case widens the selection or escalates to a full run.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fnmatch import fnmatch

from .gitutil import LineChange

# Selection modes, in order of increasing precision.
MODE_FULL = "full"  # run everything — map missing/stale or a shared root changed
MODE_FILE = "file"  # a test is selected if it covers any changed file
MODE_PRECISE = "precise"  # line-level intersection where the diff allows it


@dataclass
class Selection:
    selected: dict[str, str] = field(default_factory=dict)  # test_id -> reason
    mode: str = MODE_FILE
    confidence: str = "file-level"
    changed_files: list[str] = field(default_factory=list)
    total_known_tests: int = 0
    full_run: bool = False

    @property
    def count(self) -> int:
        return len(self.selected)


def _matches_any(path: str, patterns: list[str]) -> bool:
    return any(fnmatch(path, pat) for pat in patterns)


def _file_index(tests: dict[str, dict]) -> dict[str, set[str]]:
    """Invert the map into ``{file: {test_id, ...}}`` for file-level lookup."""
    index: dict[str, set[str]] = {}
    for test_id, entry in tests.items():
        for path in entry.get("files", {}):
            index.setdefault(path, set()).add(test_id)
    return index


def select(
    coverage_map: dict,
    changed: dict[str, str],
    all_tests: list[str] | None,
    always_run: list[str],
    *,
    precise: bool = False,
    line_info: dict[str, LineChange] | None = None,
) -> Selection:
    """Return the tests to run for ``changed``.

    ``coverage_map`` is the stored map (``{"tests": {...}}``). ``changed`` maps
    path -> status. ``all_tests`` is the freshly collected test list used to
    detect tests added since the map was built; pass ``None`` to skip that
    check. ``line_info`` is required for meaningful ``precise`` mode.
    """
    tests = coverage_map.get("tests", {})
    known = set(tests)
    line_info = line_info or {}
    changed_paths = sorted(changed)

    # No map at all -> we know nothing -> run everything.
    if not tests:
        selected = {t: "no coverage map — full run" for t in (all_tests or [])}
        return Selection(
            selected=selected,
            mode=MODE_FULL,
            confidence="full-run",
            changed_files=changed_paths,
            total_known_tests=0,
            full_run=True,
        )

    # A shared root changed -> blast radius is the whole suite.
    triggered = [p for p in changed if _matches_any(p, always_run)]
    if triggered:
        universe = set(known) | set(all_tests or [])
        reason = f"shared file changed ({triggered[0]}) — full run"
        return Selection(
            selected={t: reason for t in universe},
            mode=MODE_FULL,
            confidence="full-run",
            changed_files=changed_paths,
            total_known_tests=len(known),
            full_run=True,
        )

    index = _file_index(tests)
    selected: dict[str, str] = {}
    used_line_precision = True

    for path, status in changed.items():
        covering = index.get(path)
        if not covering:
            continue  # nothing tested touches this file (yet)
        if status == "D":
            for t in covering:
                selected.setdefault(t, f"covered now-deleted {path}")
            continue

        lc = line_info.get(path)
        can_line_match = (
            precise and status == "M" and lc is not None and not lc.pure_insertion
        )
        if not can_line_match:
            # Added file, pure insertion, or no line data: file-level is the
            # only safe choice for this file.
            if precise and status == "M":
                used_line_precision = False
            for t in covering:
                selected.setdefault(t, f"covers changed {path}")
            continue

        for t in covering:
            covered_lines = set(tests[t]["files"].get(path, []))
            hit = covered_lines & lc.old_lines
            if hit:
                sample = min(hit)
                selected.setdefault(t, f"covers {path}:{sample} (changed)")

    # Tests that did not exist when the map was built have unknown impact.
    if all_tests is not None:
        for t in all_tests:
            if t not in known:
                selected.setdefault(t, "new test — not yet in map")

    mode = MODE_PRECISE if precise else MODE_FILE
    if precise:
        confidence = "line-precise" if used_line_precision else "file-level (fallback)"
    else:
        confidence = "file-level"

    return Selection(
        selected=selected,
        mode=mode,
        confidence=confidence,
        changed_files=changed_paths,
        total_known_tests=len(known),
        full_run=False,
    )
