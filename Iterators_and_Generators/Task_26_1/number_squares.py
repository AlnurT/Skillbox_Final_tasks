"""Задача 1. Квадраты чисел

Пользователь вводит число N. Напишите программу,
которая генерирует последовательность из квадратов чисел от 1 до N
(1 ** 2, 2 ** 2, 3 ** 2 и так далее).
Реализацию напишите тремя способами: класс-итератор,
функция-генератор и генераторное выражение.
"""
from collections.abc import Iterable

from Task_26_1.number_squares_classes import SquareIterator


def generate_squares(number: int) -> Iterable[int]:
    for n in range(1, number + 1):
        yield n**2


def main() -> None:
    number = 10
    iterator = SquareIterator(number=number)
    for square in iterator:
        print(square, end=" ")

    print()

    func_generator = generate_squares(number=number)
    for square in func_generator:
        print(square, end=" ")

    print()

    generator = (n**2 for n in range(1, number + 1))
    for square in generator:
        print(square, end=" ")


if __name__ == "__main__":
    main()
