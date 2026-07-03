"""The adapter contract.

An adapter teaches radius how to talk to one test ecosystem. Adding a language
means implementing four methods against its *native* coverage tooling — radius
never re-implements instrumentation. This is what makes the tool universal
without becoming a pile of language-specific special cases.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from ..config import Config


@runtime_checkable
class Adapter(Protocol):
    #: Stable identifier used in config (``[core] adapter = "..."``).
    name: str

    def is_available(self, root: Path, config: Config) -> bool:
        """Whether this adapter can run in ``root`` (tools + project layout)."""

    def collect_tests(self, root: Path, config: Config) -> list[str]:
        """Every test id the runner currently sees (for new-test detection)."""

    def build_map(self, root: Path, config: Config) -> dict[str, dict]:
        """Run the full suite with per-test coverage and return the map body.

        The return value is ``{test_id: {"files": {path: [lines]}}}`` with all
        paths repo-root-relative POSIX strings.
        """

    def run(self, root: Path, config: Config, test_ids: list[str] | None) -> int:
        """Run ``test_ids`` (or the whole suite if ``None``); return exit code.

        Output must be streamed through untouched so developers see their normal
        test runner.
        """
