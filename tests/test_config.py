from __future__ import annotations

from radius.config import Config


def test_defaults_without_file(tmp_path):
    config = Config.load(tmp_path)
    assert config.adapter == "auto"
    assert config.test_paths == ["tests"]
    assert "conftest.py" in config.always_run


def test_parse_toml(tmp_path):
    (tmp_path / "radius.toml").write_text(
        '[core]\n'
        'adapter = "pytest"\n'
        'test_paths = ["t"]\n'
        'source_paths = ["lib"]\n'
        '[safety]\n'
        'always_run = ["only.py"]\n'
        'stale_after_commits = 5\n'
    )
    config = Config.load(tmp_path)
    assert config.adapter == "pytest"
    assert config.test_paths == ["t"]
    assert config.source_paths == ["lib"]
    assert config.always_run == ["only.py"]
    assert config.stale_after_commits == 5
