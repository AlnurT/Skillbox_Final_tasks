"""Задача 5. Счётчик

Реализуйте декоратор counter, считающий и выводящий количество вызовов
декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal
(об этом мы ещё расскажем).
"""
"""from typing import Callable

def counter(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функция вызвана {wrapper.count} раз")
        return result

    wrapper.count = 0
    return wrapper


@counter"""


def function():
    return "Привет!"


def main() -> None:
    for _ in range(5):
        print(function())


if __name__ == "__main__":
    main()
