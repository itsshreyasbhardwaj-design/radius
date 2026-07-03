<h1 align="center">radius</h1>

<p align="center"><b>Test Impact Analysis for any language.</b><br>
Run only the tests your change can actually break — before CI does.</p>

<p align="center">
  <code>radius map</code> once &nbsp;·&nbsp; <code>radius test</code> forever &nbsp;·&nbsp; pure-stdlib core &nbsp;·&nbsp; local-first &nbsp;·&nbsp; MIT
</p>

---

## The problem

Almost every project runs its **entire** test suite on every change, because nobody knows which tests a diff can affect. So you wait — locally and in CI — while thousands of tests re-run to prove that the three you actually touched still pass. It's the single biggest, most universal source of wasted engineering time and CI spend, in every language.

The big labs solved this internally (Google's TIA, Meta's Skycastle, Microsoft's TIA). The open-source world only has **single-language slices** (`pytest-testmon`, Jest `--onlyChanged`) or tools welded to one **build system** (Bazel, Nx). There is no drop-in, build-system-agnostic, multi-language Test Impact Analysis tool.

**radius is that tool.**

```console
$ radius test
base 4ef8227   mode file   confidence file-level
changed files: src/radius/selector.py
9 affected (10 of 19 known skipped, 52% saved)

tests/test_selector.py ......... [100%]
9 passed in 0.2s
```

## How it works

radius never re-implements instrumentation. It stands on the coverage tooling every language already ships:

1. **`radius map`** runs your suite once with **per-test coverage** and stores an index: `test → {files, lines}`, pinned to the commit it was built at.
2. **`radius test`** takes `git diff` since that commit, inverts the index, and hands your **native runner** only the tests that touch changed code.
3. **`radius why <test>`** tells you exactly why any test was selected or skipped.

The map is plain JSON in `.radius/`. The core — diffing, selection, storage — is **pure Python standard library**; it shells out to `git` and to each language's coverage tool. Nothing phones home; there is no service and no account.

## Install

```bash
pip install "radius-tia[pytest]"      # core + the pytest adapter
```

Requires Python 3.11+ (for the tool itself; the code under test can be anything the adapter supports).

## Quickstart

```bash
radius init          # scaffold radius.toml, ignore .radius/
radius map           # one full run builds the coverage map
# ... edit some code ...
radius affected      # preview: which tests can my change break?
radius test          # run exactly those, with your normal pytest output
radius status        # is my map still fresh?
```

Try it on the bundled example in [`examples/demo`](examples/demo).

## Correctness comes first

A false negative — skipping a test that **should** have run — is the only unacceptable outcome. radius is engineered to never do that quietly:

| Situation | What radius does |
|---|---|
| No map yet, or map commit not in current history | **Full run** |
| A shared root changes (`conftest.py`, lockfiles, CI config, `pyproject.toml` …) | **Full run** (configurable `always_run`) |
| A brand-new test not yet in the map | **Always selected** |
| A covered file is deleted | Its tests are selected |
| New lines added (no old coverage to reason about) | Falls back to **file-level** for that file |
| Map drifts too far from HEAD | Warns you to rebuild |

Line-level precision (`--precise`) only ever *narrows* selection where the diff makes it provably safe; everywhere else it widens. When in doubt, radius runs more, not fewer.

## CLI

| Command | Purpose |
|---|---|
| `radius init` | Scaffold `radius.toml` and update `.gitignore` |
| `radius map` | Build the per-test coverage map (one full run) |
| `radius affected [--precise] [--base REF] [--json]` | List the tests a change can affect (no run) |
| `radius test [--precise] [--base REF] [--dry-run]` | Run only the affected tests |
| `radius why <test_id> [--base REF]` | Explain a single test's selection |
| `radius status` | Map freshness and safety state |

By default the diff base is the commit the map was built at — the only base for which the coverage data is meaningful. Override with `--base origin/main` for "what could break on this PR".

## How radius compares

| | radius | pytest-testmon | Jest `--onlyChanged` | Bazel / Nx |
|---|:--:|:--:|:--:|:--:|
| Language-agnostic | ✅ (adapters) | ❌ Python | ❌ JS | ⚠️ within the build graph |
| Works without adopting a build system | ✅ | ✅ | ✅ | ❌ |
| Local-first, no service | ✅ | ✅ | ✅ | ✅ |
| Explains *why* a test runs | ✅ | ❌ | ❌ | ⚠️ |
| Explicit full-run safety net | ✅ | ⚠️ | ⚠️ | ✅ |

## Adding a language

radius is universal by construction: teaching it a new ecosystem means implementing one small [`Adapter`](src/radius/adapters/base.py) against that ecosystem's native coverage output — no changes to the core. Each language already emits per-test coverage (JaCoCo for Java, coverlet for C#, c8/istanbul for JS/TS, `go test -cover` for Go, llvm-cov for Rust/C++). The [pytest adapter](src/radius/adapters/pytest_adapter.py) is the ~120-line reference. See [`docs/adapters.md`](docs/adapters.md).

## Roadmap

- **v0.1** (here): pure-stdlib core, file- & line-level selection, safety net, pytest adapter, dogfooded + tested.
- **Next**: JS/TS (c8) and Go adapters · CI plugins (GitHub Actions/GitLab) · incremental map refresh on every `radius test`.
- **Later**: shared team-wide map cache keyed by commit · merge-queue integration · fail-fast test ordering · flaky-test detection layered on the same coverage history.

## Development

```bash
uv venv --python 3.12 && uv pip install -e ".[dev]"
python -m pytest          # radius tests itself
radius map && radius affected   # radius dogfoods itself
```

## License

MIT © 2026 Shreyas Bhardwaj
