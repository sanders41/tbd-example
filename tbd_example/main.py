from __future__ import annotations

from typing import Union


def add(number_list: list[Union[int, float]]) -> float:
    return sum(number_list)


def main() -> None:
    nums = [2, 2, 2.5]
    print(add(nums))  # noqa: T001


if __name__ == "__main__":
    main()
