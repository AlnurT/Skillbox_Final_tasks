"""Задача 4. Весь мир — декоратор…

Реализуйте декоратор для декораторов: он должен декорировать другую функцию,
которая должна быть декоратором, и даёт возможность любому декоратору принимать
произвольные аргументы.

Пример использования:

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

Результат:
Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
Привет, Юзер 101
"""
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Переданные арги и кварги в декоратор: {dec_args} {dec_kwargs}")
        return func(*args, **kwargs)

    return wrapper


@decorated_decorator(100, "рублей", 200, "друзей")
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


def main() -> None:
    decorated_function("Юзер", 101)


if __name__ == "__main__":
    main()
