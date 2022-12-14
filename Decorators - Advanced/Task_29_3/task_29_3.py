"""Задача 3. Логирование в формате

Реализуйте декоратор, который будет логировать все методы декорируемого класса
(кроме магических методов) и в который можно передавать формат вывода даты и времени
логирования.

Пример кода, передаётся формат «Месяц День Год - Часы Минуты Секунды»:

@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()


Результат:

Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
test_sum_1

Завершение 'A.test_sum_1', время работы = 0.187s
Наследник test_sum_1

Завершение 'B.test_sum_1', время работы = 0.187s
Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
Наследник test_sum_2

Завершение 'B.test_sum_2', время работы = 0.370s
"""
import time
from datetime import datetime
from typing import Any, Callable


def timer(cls: Any, func: Callable, output: str) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        date = datetime.utcnow().strftime(output)
        start_time = time.time()

        print(
            f"Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {date}"
        )
        func(*args, **kwargs)
        end_time = round(time.time() - start_time, 3)
        print(f"Завершение {cls.__name__}.{func.__name__}, время работы = {end_time}\n")
        return func

    return wrapper


def log_methods(output: str) -> Callable:
    def decorate(cls: Any) -> Any:
        for method in dir(cls):
            if not method.startswith("__"):
                curent_method = getattr(cls, method)
                decorated_method = timer(cls=cls, func=curent_method, output=output)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> Any:
        print("test sum 1")
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self) -> Any:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num**2 for i_num in range(10000)])

        return result


def main() -> None:
    my_obj = B()
    my_obj.test_sum_1()
    my_obj.test_sum_2()


if __name__ == "__main__":
    main()
