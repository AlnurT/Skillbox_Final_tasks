"""Задача 1. Новые списки

Даны три списка:

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

Напишите код, который создаёт три новых списка. Вот их содержимое:

1) Каждое число из списка floats возводится в третью степень и округляется до трёх знаков
после запятой.
2) Из списка names берутся только те имена, в которых есть минимум пять букв.
3) Из списка numbers берётся произведение всех чисел.
"""
from functools import reduce
from typing import List


def cube_and_round_list(float_list: List[float]) -> list:
    result = (round(num**3, 3) for num in float_list)
    return list(result)


def filter_names(str_list: List[str]) -> list:
    result = filter(lambda x: len(x) >= 5, str_list)
    return list(result)


def multiply_numbers(int_list: List[int]) -> int:
    return reduce(lambda x, y: x * y, int_list)


def main():
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    new_floats = cube_and_round_list(float_list=floats)
    new_names = filter_names(str_list=names)
    new_numbers = multiply_numbers(int_list=numbers)

    print(new_floats)
    print(new_names)
    print(new_numbers)


if __name__ == "__main__":
    main()
