"""Задача 3. Читабельность кода

Необходимо вывести на экран список простых чисел от 0 до 1000.
Реализуйте это двумя способами:

1) «однострочным» кодом, без объявления дополнительных функций;
2) обычным, «своим» кодом, который покажется вам наиболее красивым.

После этого ответьте себе (не куратору) на вопрос: какое из решений более читабельное?
"""
from math import sqrt
from typing import Iterable


def search_prime_numbers(max_number: int) -> Iterable[int]:
    yield 2
    for number in range(3, max_number + 1, 2):
        for divisor in range(2, int(sqrt(number) + 1)):
            if number % divisor == 0:
                break
        else:
            yield number


def main():
    max_number = 1000

    result_1 = list(
        filter(
            lambda x: all(
                map(lambda i: x % i != 0, range(2, int(sqrt(x) + 1))),
            ),
            range(2, int(max_number) + 1),
        )
    )
    result_2 = list(search_prime_numbers(max_number))

    print(result_1)
    print(result_2)
    print(result_1 == result_2)


if __name__ == "__main__":
    main()
