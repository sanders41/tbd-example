from __future__ import annotations


def factors_of(number: int) -> list[int]:
    """
    Factor an integer into a list where the product of the list is equal to the original number.
    """

    return [i for i in range(1, number + 1) if number % i == 0]


def main() -> None:
    number = 25
    print(factors_of(number))  # noqa: T001


if __name__ == "__main__":
    main()
