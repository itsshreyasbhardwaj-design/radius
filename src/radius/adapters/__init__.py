"""Adapter registry and detection."""

from __future__ import annotations

from pathlib import Path

from ..config import Config
from .base import Adapter
from .pytest_adapter import PytestAdapter

# Ordered by detection priority. New languages register here.
_REGISTRY: list[type] = [PytestAdapter]


class AdapterError(RuntimeError):
    pass


def available_names() -> list[str]:
    return [cls.name for cls in _REGISTRY]


def get_adapter(name: str, root: Path, config: Config) -> Adapter:
    """Resolve an adapter by name, or auto-detect when ``name == "auto"``."""
    if name and name != "auto":
        for cls in _REGISTRY:
            if cls.name == name:
                return cls()  # type: ignore[return-value]
        raise AdapterError(
            f"unknown adapter '{name}'. Available: {', '.join(available_names())}"
        )

    for cls in _REGISTRY:
        candidate = cls()
        if candidate.is_available(root, config):
            return candidate  # type: ignore[return-value]
    raise AdapterError(
        "could not auto-detect a test adapter. Set [core] adapter in radius.toml. "
        f"Known adapters: {', '.join(available_names())}"
    )


__all__ = ["Adapter", "AdapterError", "get_adapter", "available_names"]
