"""Задача 4. Палиндром: возвращение

Для Python существует множество различных библиотек для работы с данными,
причём как встроенных, так и внешних. С некоторыми из них мы уже работали,
например с модулем collections, когда использовали специальный класс OrderedDict,
с помощью которого делали упорядоченный словарь.
Конечно же, в этой библиотеке есть и другие возможности (на самом деле их совсем немного).
Вот официальная документация: collections — Container datatypes.

Используя модуль collections и новые знания о функциях, реализуйте функцию can_be_poly,
которая принимает на вход строку и проверяет, можно ли получить из неё палиндром.

Пример кода:
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

Результат:
True
False
"""
import collections


def can_be_poly(line: str) -> bool:
    reverse_line = collections.deque(line)
    reverse_line.reverse()
    return str(reverse_line) == line


def main():
    print(can_be_poly("abcba"))
    print(can_be_poly("abbbc"))


if __name__ == "__main__":
    main()
