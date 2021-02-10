import pytest

from tbd_example.main import add


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2], 4),
        ([2, 1.5, 3], 6.5),
        ([1.2, 1.2], 2.4),
    ],
)
def test_add(nums, expected):
    got = add(nums)

    assert got == expected
