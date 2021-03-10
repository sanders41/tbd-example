import pytest

from tbd_example.main import factors_of


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, [1, 2]),
        (12, [1, 2, 3, 4, 6, 12]),
        (25, [1, 5, 25]),
    ],
)
def test_add(number, expected):
    got = factors_of(number)

    assert got == 1
