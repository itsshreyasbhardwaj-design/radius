# Writing a radius adapter

An adapter is the only language-specific code in radius. The core (git diff,
selection, map storage) never changes. To add a language you implement four
methods against that ecosystem's **native** coverage tooling — you never write
instrumentation yourself.

## The contract

See [`src/radius/adapters/base.py`](../src/radius/adapters/base.py):

```python
class Adapter(Protocol):
    name: str

    def is_available(self, root, config) -> bool: ...
    def collect_tests(self, root, config) -> list[str]: ...
    def build_map(self, root, config) -> dict[str, dict]: ...
    def run(self, root, config, test_ids: list[str] | None) -> int: ...
```

### `is_available(root, config) -> bool`
Can this adapter run here? Check that the runner and coverage tool exist and
that the configured test paths are present.

### `collect_tests(root, config) -> list[str]`
Return every test id the runner currently sees. radius uses this to detect
tests added since the map was built (which are always run). Test ids must be
**identical** to the keys produced by `build_map` and the ids accepted by
`run`.

### `build_map(root, config) -> {test_id: {"files": {path: [lines]}}}`
Run the full suite with per-test coverage, then translate the native coverage
output into the map shape. **Every path must be repo-root-relative POSIX** so it
lines up with `git diff`. Keep the translation a pure function (as the pytest
adapter's `map_from_coverage_json` is) so it can be unit-tested against fixture
output.

### `run(root, config, test_ids) -> int`
Run `test_ids` (or the whole suite when `None`) and return the process exit
code. Stream the runner's output through untouched — developers should see
their normal test report.

## The one invariant that matters

**Test ids must be stable and identical across all three surfaces** —
`collect_tests`, the keys of `build_map`, and the ids passed to `run`. The
pytest adapter gets this for free by using pytest-cov's test contexts, which are
labelled with the exact pytest node id (`path::test`). Prefer a coverage mode
that labels contexts with the runner's own node id; otherwise you must normalise
both sides to a canonical form.

## Native per-test coverage by language

| Language | Native tool | Per-test mechanism |
|---|---|---|
| Python | coverage.py + pytest-cov | `--cov-context=test` |
| JS/TS | c8 / istanbul | per-test coverage (Vitest/Jest) |
| Java | JaCoCo | per-test sessions |
| C# | coverlet | deterministic per-test reports |
| Go | `go test -cover` | per-package (coarser granularity) |
| Rust | llvm-cov / grcov | per-test profiles |
| C/C++ | gcov / llvm-cov | per-test profraw |

Granularity may vary (Go is package-level). Declare it honestly: never report
finer selection than the coverage data supports, so radius stays safe.

## Registering

Add the class to `_REGISTRY` in
[`src/radius/adapters/__init__.py`](../src/radius/adapters/__init__.py). Users
select it with `[core] adapter = "<name>"` or rely on auto-detection.
