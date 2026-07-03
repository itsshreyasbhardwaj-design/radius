"""Glue between git, the map store, the selector, and an adapter.

``plan()`` answers the one question the whole tool exists to answer — *given
where the code is right now, which tests could my change break?* — and is
shared by ``affected``, ``test``, and ``why`` so they can never disagree.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from . import gitutil
from .adapters import Adapter
from .config import Config
from .selector import MODE_FULL, Selection, select
from .store import Store


@dataclass
class Plan:
    selection: Selection
    base: str | None
    warnings: list[str] = field(default_factory=list)
    collected: bool = False


def _resolve_base(config: Config, meta_commit: str | None, override: str | None) -> str | None:
    return override or config.base or meta_commit


def plan(
    root: Path,
    config: Config,
    adapter: Adapter,
    store: Store,
    *,
    base_override: str | None = None,
    precise: bool = False,
    collect: bool = True,
) -> Plan:
    warnings: list[str] = []
    meta = store.load_meta()

    if meta is None:
        # No map: everything is unknown. Collect so we can name what will run.
        all_tests = adapter.collect_tests(root, config) if collect else []
        sel = select({"tests": {}}, {}, all_tests, config.always_run)
        return Plan(sel, None, ["no coverage map yet — run 'radius map'"], collect)

    base = _resolve_base(config, meta.built_at_commit, base_override)
    if base is None:
        all_tests = adapter.collect_tests(root, config) if collect else []
        sel = select({"tests": {}}, {}, all_tests, config.always_run)
        return Plan(sel, None, ["repository has no commits — full run"], collect)

    # If the map's commit is not an ancestor of HEAD (rebase, amend, force
    # push, wrong branch) the diff is meaningless — fall back to a full run.
    if base != "HEAD" and not gitutil.is_ancestor(root, base):
        warnings.append(
            f"map commit {gitutil.short_sha(root, base)} is not in the current "
            "history — running the full suite"
        )
        all_tests = adapter.collect_tests(root, config) if collect else []
        universe = set(store.load_map().get("tests", {})) | set(all_tests)
        sel = Selection(
            selected={t: "map out of history — full run" for t in universe},
            mode=MODE_FULL,
            confidence="full-run",
            changed_files=[],
            total_known_tests=len(store.load_map().get("tests", {})),
            full_run=True,
        )
        return Plan(sel, base, warnings, collect)

    behind = gitutil.commits_since(root, base)
    if behind > config.stale_after_commits:
        warnings.append(
            f"map is {behind} commits behind HEAD — consider 'radius map' "
            "to keep selection sharp"
        )

    changed = gitutil.changed_files(root, base)
    line_info = {}
    if precise:
        for path, status in changed.items():
            if status == "M":
                line_info[path] = gitutil.line_changes(root, base, path)

    all_tests = adapter.collect_tests(root, config) if collect else None
    coverage_map = store.load_map()
    sel = select(
        coverage_map,
        changed,
        all_tests,
        config.always_run,
        precise=precise,
        line_info=line_info,
    )
    return Plan(sel, base, warnings, collect)
