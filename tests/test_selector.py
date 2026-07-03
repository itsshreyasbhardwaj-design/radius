"""Selector behaviour — the correctness-critical core."""

from __future__ import annotations

from radius.gitutil import LineChange
from radius.selector import MODE_FILE, MODE_FULL, MODE_PRECISE, select

MAP = {
    "tests": {
        "tests/test_a.py::test_one": {"files": {"src/a.py": [1, 2, 3], "src/util.py": [10]}},
        "tests/test_b.py::test_two": {"files": {"src/b.py": [1, 2]}},
    }
}
ALWAYS = ["conftest.py", "**/conftest.py"]


def test_file_level_selects_only_covering_tests():
    sel = select(MAP, {"src/a.py": "M"}, None, ALWAYS)
    assert set(sel.selected) == {"tests/test_a.py::test_one"}
    assert sel.mode == MODE_FILE
    assert not sel.full_run


def test_unrelated_change_selects_nothing():
    sel = select(MAP, {"docs/readme.md": "M"}, None, ALWAYS)
    assert sel.selected == {}


def test_empty_map_is_a_full_run():
    sel = select({"tests": {}}, {"src/a.py": "M"}, ["tests/test_a.py::test_one"], ALWAYS)
    assert sel.full_run
    assert sel.mode == MODE_FULL
    assert set(sel.selected) == {"tests/test_a.py::test_one"}


def test_always_run_file_forces_full_run():
    sel = select(MAP, {"conftest.py": "M"}, None, ALWAYS)
    assert sel.full_run
    assert set(sel.selected) == set(MAP["tests"])


def test_new_test_is_always_selected():
    all_tests = list(MAP["tests"]) + ["tests/test_c.py::test_new"]
    sel = select(MAP, {"docs/x.md": "M"}, all_tests, ALWAYS)
    assert "tests/test_c.py::test_new" in sel.selected
    assert "new test" in sel.selected["tests/test_c.py::test_new"]


def test_deleted_covered_file_selects_its_tests():
    sel = select(MAP, {"src/b.py": "D"}, None, ALWAYS)
    assert set(sel.selected) == {"tests/test_b.py::test_two"}
    assert "deleted" in sel.selected["tests/test_b.py::test_two"]


def test_precise_intersects_changed_lines():
    line_info = {"src/a.py": LineChange(frozenset({2}), pure_insertion=False)}
    sel = select(MAP, {"src/a.py": "M"}, None, ALWAYS, precise=True, line_info=line_info)
    assert set(sel.selected) == {"tests/test_a.py::test_one"}
    assert sel.mode == MODE_PRECISE
    assert sel.confidence == "line-precise"


def test_precise_skips_when_changed_line_is_uncovered():
    line_info = {"src/a.py": LineChange(frozenset({99}), pure_insertion=False)}
    sel = select(MAP, {"src/a.py": "M"}, None, ALWAYS, precise=True, line_info=line_info)
    assert sel.selected == {}


def test_precise_falls_back_to_file_level_on_pure_insertion():
    # New lines have no old coverage, so we cannot line-match safely.
    line_info = {"src/a.py": LineChange(frozenset(), pure_insertion=True)}
    sel = select(MAP, {"src/a.py": "M"}, None, ALWAYS, precise=True, line_info=line_info)
    assert set(sel.selected) == {"tests/test_a.py::test_one"}
    assert "fallback" in sel.confidence
