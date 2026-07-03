"""The coverage-JSON -> map inversion, tested against fixture data."""

from __future__ import annotations

from radius.adapters.pytest_adapter import map_from_coverage_json


def test_inverts_contexts_into_per_test_map(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "a.py").write_text("x = 1\n")

    data = {
        "files": {
            "src/a.py": {
                "contexts": {
                    "1": ["tests/test_a.py::test_one|run", ""],
                    "2": [
                        "tests/test_a.py::test_one|run",
                        "tests/test_b.py::test_two|run",
                    ],
                }
            },
            "/opt/site-packages/lib.py": {  # outside the repo
                "contexts": {"5": ["tests/test_a.py::test_one|run"]}
            },
        }
    }

    m = map_from_coverage_json(data, tmp_path)

    assert m["tests/test_a.py::test_one"]["files"]["src/a.py"] == [1, 2]
    assert m["tests/test_b.py::test_two"]["files"]["src/a.py"] == [2]
    # Import-time (empty) context is ignored, and files outside the repo dropped.
    for entry in m.values():
        for path in entry["files"]:
            assert not path.startswith("/")


def test_empty_coverage_yields_empty_map(tmp_path):
    assert map_from_coverage_json({"files": {}}, tmp_path) == {}
