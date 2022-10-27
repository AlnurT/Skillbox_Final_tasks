"""Задача 3. Логирование

Реализуйте декоратор logging, который будет отвечать за логирование функций.
На экран выводится название функции и её документация. Если во время выполнения
декорируемой функции возникла ошибка, то в файл function_errors.log записываются
названия функции и ошибки.

Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения
первой же ошибки, а обрабатывала все декорируемые функции и сразу записывала все ошибки
в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
"""
from datetime import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    try:
        func()
    except BaseException as error:
        data_time = datetime.now().strftime("%Y, %B %d. %I:%M")
        with open("log.txt", "a", encoding="utf-8") as logi:
            logi.write(f"Ошибка: {error}\n")
            logi.write(f"Время ошибки: {data_time}\n\n")
    return func


@logging
def zero_error() -> float:
    """Функция для ошибки деления на ноль"""
    return 5 / 0


@logging
def value_error() -> int:
    """Функция для ошибки неправильного аргумента"""

    return int("Alnur")


@logging
def calculate_square(number: int = 5) -> int:
    """Функция для расчёта квадрата числа"""

    return number**2


def main() -> None:
    print(f"Название функции: {zero_error.__name__}")
    print(f"Документация:\n{zero_error.__doc__}\n")

    print(f"Название функции: {value_error.__name__}")
    print(f"Документация:\n{value_error.__doc__}\n")

    print(f"Название функции: {calculate_square.__name__}")
    print(f"Документация:\n{calculate_square.__doc__}")
    print(f"Результат: {calculate_square()}\n")


if __name__ == "__main__":
    main()
