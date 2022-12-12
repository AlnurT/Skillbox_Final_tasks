from collections.abc import Iterator


class SquareIterator:
    def __init__(self, number: int) -> None:
        self.__n = number
        self.__counter = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__counter <= self.__n:
            return self.__counter**2
        raise StopIteration
