from __future__ import annotations

from radius.store import Meta, Store


def test_map_and_meta_roundtrip(tmp_path):
    store = Store(tmp_path)
    assert not store.exists()

    tests = {"tests/test_a.py::test_one": {"files": {"src/a.py": [1, 2]}}}
    store.save_map(tests)
    store.save_meta(Meta("abc123", "2026-07-03T10:00:00+00:00", "pytest", 1, 1))

    assert store.exists()
    assert store.load_map()["tests"] == tests
    meta = store.load_meta()
    assert meta is not None
    assert meta.built_at_commit == "abc123"
    assert meta.test_count == 1


def test_missing_map_returns_empty(tmp_path):
    store = Store(tmp_path)
    assert store.load_map() == {"version": 1, "tests": {}}
    assert store.load_meta() is None
