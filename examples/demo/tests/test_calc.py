import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calc import add, div, mul, sub  # noqa: E402


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 2) == 3


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(10, 2) == 5
    import pytest

    with pytest.raises(ZeroDivisionError):
        div(1, 0)
