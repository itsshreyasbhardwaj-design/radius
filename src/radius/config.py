"""Load and represent ``radius.toml``.

Config is optional: with no file, sensible defaults are used. Keeping this
pure-stdlib means the only hard requirement for the core is Python 3.11+
(for :mod:`tomllib`).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

try:  # 3.11+
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - exercised only on <3.11
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:  # pragma: no cover
        tomllib = None  # type: ignore[assignment]


# Files whose change means "we can't reason about the blast radius — run
# everything." These are shared roots: fixtures, dependency locks, build and CI
# config. Erring toward a full run here is the safety net, not a failure.
DEFAULT_ALWAYS_RUN: list[str] = [
    "conftest.py",
    "**/conftest.py",
    "pyproject.toml",
    "setup.cfg",
    "setup.py",
    "tox.ini",
    "radius.toml",
    "requirements*.txt",
    "poetry.lock",
    "Pipfile.lock",
    "uv.lock",
    ".github/workflows/**",
]


@dataclass
class Config:
    """Resolved radius configuration."""

    adapter: str = "auto"
    # Diff base. ``None`` means "use the commit the map was built at", which is
    # the only base that makes the coverage data meaningful.
    base: str | None = None
    test_paths: list[str] = field(default_factory=lambda: ["tests"])
    source_paths: list[str] = field(default_factory=lambda: ["src", "."])
    always_run: list[str] = field(default_factory=lambda: list(DEFAULT_ALWAYS_RUN))
    # Warn once the map is this many commits behind HEAD.
    stale_after_commits: int = 100

    @classmethod
    def load(cls, root: Path) -> "Config":
        path = root / "radius.toml"
        if not path.exists() or tomllib is None:
            return cls()
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        core = data.get("core", {})
        safety = data.get("safety", {})
        return cls(
            adapter=core.get("adapter", "auto"),
            base=core.get("base"),
            test_paths=list(core.get("test_paths", ["tests"])),
            source_paths=list(core.get("source_paths", ["src", "."])),
            always_run=list(safety.get("always_run", DEFAULT_ALWAYS_RUN)),
            stale_after_commits=int(safety.get("stale_after_commits", 100)),
        )
