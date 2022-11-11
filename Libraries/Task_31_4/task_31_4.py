"""Задача 4. Телефонные номера

В одной организации перед записью телефонного номера в базу данных его проверяют
на соответствие следующим критериям:

Длина номера — ровно 10 знаков.
Номер начинается с цифры 8 или с цифры 9.
Остальные знаки — только цифры.

На вход в программу подаётся список номеров (можно взять готовый или запросить
у пользователя). Реализуйте код, который проверяет каждый номер из списка
на соответствие критериям и выводит на экран соответствующие сообщения.

Пример списка:
['9999999999', '999999-999', '99999x9999']

Результат:
первый номер: всё в порядке
второй номер: не подходит
третий номер: не подходит
"""
import re
from collections.abc import Iterator


def is_correct_mobile_number(numbers: list) -> Iterator:
    pattern = re.compile(r"\b[89]\d{9}\b")
    for number in numbers:
        yield pattern.findall(number)


def main():
    mobile_number: list = [
        "9674567457",
        "8475757777",
        "956784-676",
        "92346x9576",
        "97878445887",
        "925335544",
        "0999958787",
        "967456745!",
        "",
    ]

    number_count = 0
    for number in is_correct_mobile_number(mobile_number):
        number_count += 1
        if number:
            print(f"{number_count} номер: всё в порядке")
        else:
            print(f"{number_count} номер: не подходит")


if __name__ == "__main__":
    main()
