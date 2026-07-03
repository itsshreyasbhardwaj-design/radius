"""Command-line interface for radius."""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import sys
from pathlib import Path

from . import __version__, gitutil
from .adapters import AdapterError, get_adapter
from .config import Config
from .engine import plan
from .store import Meta, Store

_USE_COLOR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def _c(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _USE_COLOR else text


def _dim(t: str) -> str:
    return _c(t, "2")


def _bold(t: str) -> str:
    return _c(t, "1")


def _green(t: str) -> str:
    return _c(t, "32")


def _yellow(t: str) -> str:
    return _c(t, "33")


def _cyan(t: str) -> str:
    return _c(t, "36")


def _err(msg: str) -> None:
    print(f"{_c('radius:', '31')} {msg}", file=sys.stderr)


def _find_root() -> Path:
    try:
        return gitutil.repo_root()
    except gitutil.GitError:
        _err("not inside a git repository. radius needs git to compute diffs.")
        raise SystemExit(2)


def _warn_all(warnings: list[str]) -> None:
    for w in warnings:
        print(f"  {_yellow('!')} {w}", file=sys.stderr)


# --------------------------------------------------------------------------- #
# commands
# --------------------------------------------------------------------------- #
def cmd_init(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    try:
        adapter = get_adapter(args.adapter or config.adapter, root, config)
    except AdapterError as exc:
        _err(str(exc))
        return 2

    toml_path = root / "radius.toml"
    if toml_path.exists() and not args.force:
        print(f"{_dim('exists')}  {toml_path.name} (use --force to overwrite)")
    else:
        toml_path.write_text(_DEFAULT_TOML.format(adapter=adapter.name), encoding="utf-8")
        print(f"{_green('created')} {toml_path.name}  (adapter: {_bold(adapter.name)})")

    # Keep the map out of version control by default.
    gi = root / ".gitignore"
    line = ".radius/"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    if line not in existing.splitlines():
        with gi.open("a", encoding="utf-8") as fh:
            if existing and not existing.endswith("\n"):
                fh.write("\n")
            fh.write(f"# radius coverage map\n{line}\n")
        print(f"{_green('updated')} .gitignore  (+ {line})")

    print()
    print("Next:")
    print(f"  {_cyan('radius map')}       build the coverage map (one full run)")
    print(f"  {_cyan('radius test')}      run only the tests your changes can affect")
    return 0


def cmd_map(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    store = Store(root)
    try:
        adapter = get_adapter(config.adapter, root, config)
    except AdapterError as exc:
        _err(str(exc))
        return 2

    print(f"{_bold('radius map')}  building per-test coverage with {adapter.name} …\n")
    try:
        tests = adapter.build_map(root, config)
    except RuntimeError as exc:
        _err(str(exc))
        return 2

    files = {p for entry in tests.values() for p in entry["files"]}
    store.save_map(tests)
    store.save_meta(
        Meta(
            built_at_commit=gitutil.head_sha(root),
            built_at=_dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            adapter=adapter.name,
            test_count=len(tests),
            file_count=len(files),
        )
    )
    print()
    print(
        f"{_green('mapped')} {_bold(str(len(tests)))} tests across "
        f"{_bold(str(len(files)))} files "
        f"{_dim('→ .radius/map.json')}"
    )
    if not tests:
        print(
            _yellow(
                "  no per-test coverage captured — is pytest-cov installed and are "
                "there tests under your test_paths?"
            )
        )
    return 0


def _print_selection(root: Path, p) -> None:
    sel = p.selection
    if sel.full_run:
        headline = _yellow("full run") + f" — {sel.count} tests"
    else:
        skipped = max(sel.total_known_tests - sel.count, 0)
        pct = (100 * skipped // sel.total_known_tests) if sel.total_known_tests else 0
        headline = (
            f"{_bold(str(sel.count))} affected "
            f"{_dim(f'({skipped} of {sel.total_known_tests} known skipped, {pct}% saved)')}"
        )
    base = gitutil.short_sha(root, p.base) if p.base else "—"
    print(f"{_cyan('base')} {base}   {_cyan('mode')} {sel.mode}   "
          f"{_cyan('confidence')} {sel.confidence}")
    if sel.changed_files:
        print(_dim(f"changed files: {', '.join(sel.changed_files[:8])}"
                   + (" …" if len(sel.changed_files) > 8 else "")))
    print(headline)


def cmd_affected(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    store = Store(root)
    try:
        adapter = get_adapter(config.adapter, root, config)
    except AdapterError as exc:
        _err(str(exc))
        return 2

    p = plan(root, config, adapter, store,
             base_override=args.base, precise=args.precise, collect=not args.no_collect)

    if args.json:
        import json
        print(json.dumps({
            "base": p.base,
            "mode": p.selection.mode,
            "confidence": p.selection.confidence,
            "full_run": p.selection.full_run,
            "changed_files": p.selection.changed_files,
            "total_known_tests": p.selection.total_known_tests,
            "selected": p.selection.selected,
        }, indent=2))
        return 0

    _warn_all(p.warnings)
    _print_selection(root, p)
    print()
    for test_id in sorted(p.selection.selected):
        print(f"  {_green('●')} {test_id}  {_dim(p.selection.selected[test_id])}")
    return 0


def cmd_test(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    store = Store(root)
    try:
        adapter = get_adapter(config.adapter, root, config)
    except AdapterError as exc:
        _err(str(exc))
        return 2

    p = plan(root, config, adapter, store,
             base_override=args.base, precise=args.precise, collect=True)
    _warn_all(p.warnings)
    _print_selection(root, p)

    sel = p.selection
    if args.dry_run:
        return 0
    if sel.count == 0 and not sel.full_run:
        print(_green("nothing affected — no tests to run ✓"))
        return 0

    print()
    test_ids = None if sel.full_run else sorted(sel.selected)
    return adapter.run(root, config, test_ids)


def cmd_why(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    store = Store(root)
    try:
        adapter = get_adapter(config.adapter, root, config)
    except AdapterError as exc:
        _err(str(exc))
        return 2

    p = plan(root, config, adapter, store,
             base_override=args.base, precise=args.precise, collect=True)
    _warn_all(p.warnings)
    reason = p.selection.selected.get(args.test_id)
    base_txt = gitutil.short_sha(root, p.base) if p.base else "—"
    if reason:
        print(f"{_green('SELECTED')} {args.test_id}")
        print(f"  reason: {reason}")
        print("  " + _dim(f"base {base_txt} · mode {p.selection.mode}"))
    else:
        print(f"{_dim('SKIPPED')}  {args.test_id}")
        print("  no changed file is covered by this test for the current diff")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    root = _find_root()
    config = Config.load(root)
    store = Store(root)
    meta = store.load_meta()
    print(_bold("radius status"))
    print(f"  adapter        {config.adapter}")
    if meta is None:
        print(f"  map            {_yellow('not built')} — run 'radius map'")
        return 0
    behind = gitutil.commits_since(root, meta.built_at_commit) if meta.built_at_commit else 0
    ancestor = (
        meta.built_at_commit == gitutil.head_sha(root)
        or (meta.built_at_commit and gitutil.is_ancestor(root, meta.built_at_commit))
    )
    print(f"  map commit     {gitutil.short_sha(root, meta.built_at_commit) if meta.built_at_commit else '—'}")
    print(f"  built at       {meta.built_at}")
    print(f"  tests / files  {meta.test_count} / {meta.file_count}")
    behind_txt = f"{behind} commits behind HEAD"
    print(f"  freshness      {(_green('current') if behind == 0 else _yellow(behind_txt))}")
    if not ancestor:
        print(f"  {_yellow('warning')}       map commit is not in current history — "
              "selection will fall back to full runs")
    return 0


_DEFAULT_TOML = """\
# radius — Test Impact Analysis
# https://github.com/  (your fork)

[core]
adapter = "{adapter}"
# Where tests live and which source trees to measure coverage for.
test_paths = ["tests"]
source_paths = ["src", "."]
# base = "origin/main"   # optional: diff against a ref instead of the map commit

[safety]
# Changing any of these forces a full run — impact is too broad to reason about.
always_run = [
  "conftest.py", "**/conftest.py",
  "pyproject.toml", "setup.cfg", "setup.py", "tox.ini", "radius.toml",
  "requirements*.txt", "poetry.lock", "uv.lock",
  ".github/workflows/**",
]
# Nudge to rebuild the map once it drifts this far from HEAD.
stale_after_commits = 100
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="radius",
        description="Test Impact Analysis — run only the tests your change can break.",
    )
    parser.add_argument("--version", action="version", version=f"radius {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="scaffold radius.toml and .gitignore")
    p_init.add_argument("--adapter", help="force an adapter instead of auto-detecting")
    p_init.add_argument("--force", action="store_true", help="overwrite existing radius.toml")
    p_init.set_defaults(func=cmd_init)

    p_map = sub.add_parser("map", help="build the per-test coverage map (one full run)")
    p_map.set_defaults(func=cmd_map)

    common_base = dict()
    for name, help_ in [("affected", "list the tests a change can affect (no run)"),
                        ("test", "run only the affected tests")]:
        pp = sub.add_parser(name, help=help_)
        pp.add_argument("--base", help="diff against this ref (default: the map commit)")
        pp.add_argument("--precise", action="store_true",
                        help="use line-level selection where the diff allows")
        if name == "affected":
            pp.add_argument("--json", action="store_true", help="machine-readable output")
            pp.add_argument("--no-collect", action="store_true",
                            help="skip test collection (faster; misses brand-new tests)")
            pp.set_defaults(func=cmd_affected)
        else:
            pp.add_argument("--dry-run", action="store_true",
                            help="show the plan without running tests")
            pp.set_defaults(func=cmd_test)

    p_why = sub.add_parser("why", help="explain why a specific test is selected or skipped")
    p_why.add_argument("test_id")
    p_why.add_argument("--base", help="diff against this ref (default: the map commit)")
    p_why.add_argument("--precise", action="store_true")
    p_why.set_defaults(func=cmd_why)

    p_status = sub.add_parser("status", help="show map freshness and safety state")
    p_status.set_defaults(func=cmd_status)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:  # pragma: no cover
        return 130
    except gitutil.GitError as exc:  # pragma: no cover
        _err(str(exc))
        return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
