"""Задача 2. Замедление кода

В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
Типичный пример — функция, которая постоянно проверяет,
изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько
секунд.
"""
import time
from typing import Callable


def decorator(func: Callable) -> Callable:
    time_start = time.time()
    time.sleep(1)
    time_end = time.time()
    total_time = round(time_end - time_start, 5)
    print(f"Время выполнения: {total_time}")
    return func


@decorator
def some_func():
    for symbol in "Hello world!":
        print(symbol, end=" ")


def main():
    some_func()


if __name__ == "__main__":
    main()
