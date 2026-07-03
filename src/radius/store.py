"""Persistence for the coverage map under ``.radius/``.

The map is deliberately a plain, human-diffable JSON document:

    {
      "version": 1,
      "tests": {
        "tests/test_calc.py::test_add": {
          "files": {"src/calc.py": [1, 2, 5]}
        }
      }
    }

``meta.json`` pins the map to the commit it was built at — the anchor every
diff is measured against.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

MAP_VERSION = 1
DIR_NAME = ".radius"


@dataclass
class Meta:
    built_at_commit: str | None
    built_at: str
    adapter: str
    test_count: int
    file_count: int


class Store:
    def __init__(self, root: Path):
        self.root = root
        self.dir = root / DIR_NAME
        self.map_path = self.dir / "map.json"
        self.meta_path = self.dir / "meta.json"

    def exists(self) -> bool:
        return self.map_path.exists() and self.meta_path.exists()

    def ensure_dir(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)

    # -- coverage map ----------------------------------------------------
    def load_map(self) -> dict:
        if not self.map_path.exists():
            return {"version": MAP_VERSION, "tests": {}}
        return json.loads(self.map_path.read_text(encoding="utf-8"))

    def save_map(self, tests: dict[str, dict]) -> None:
        self.ensure_dir()
        payload = {"version": MAP_VERSION, "tests": tests}
        self.map_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    # -- metadata --------------------------------------------------------
    def load_meta(self) -> Meta | None:
        if not self.meta_path.exists():
            return None
        data = json.loads(self.meta_path.read_text(encoding="utf-8"))
        return Meta(**data)

    def save_meta(self, meta: Meta) -> None:
        self.ensure_dir()
        self.meta_path.write_text(
            json.dumps(asdict(meta), indent=2) + "\n", encoding="utf-8"
        )
