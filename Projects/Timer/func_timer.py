import time
from collections.abc import Iterable
from typing import Callable


def timer(func: Callable) -> Callable:
    start = time.time()
    func()
    end = time.time()
    print(f"Время работы {func.__name__}:\t{1000 * (end - start)}")
    return func


@timer
def base_for() -> list:
    l: list = []
    for i in range(1000):
        l.append(i**i)
    return l


@timer
def list_comprehension() -> list:
    return [i**i for i in range(1000)]


@timer
def generator() -> Iterable:
    return (i**i for i in range(1000))


@timer
def generator_y() -> Iterable:
    for i in range(1000):
        yield i**i


@timer
def dictionary() -> dict:
    d = {}
    for i in range(1000):
        d[i] = i**i
    return d


def main():
    base_for()
    list_comprehension()
    generator()
    generator_y()
    dictionary()


if __name__ == "__main__":
    main()
