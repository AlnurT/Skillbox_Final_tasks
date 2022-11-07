"""Задача 2. Функция обратного вызова

При работе с сетью и веб-сервисами иногда используется функция callback,
так называемая функция обратного вызова.
Это функция, которая вызывается при срабатывании определённого события
(переходе на страницу, получении сообщения или окончании обработки процессором).
В неё можно передать функцию, чтобы она выполнилась после определённого события.
Это используется, например, в HTTP-серверах в ответ на URL-запросы.
Реализуйте такую функцию.

Пример функции:

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

Основной код:
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

Ожидаемый результат:
Пример функции, которая возвращает ответ сервера
Ответ: OK

Подсказка: функция callback может быть вызвана следующим действием в зависимости
от условия или просто так.
"""
from typing import Callable


def callback(_func=None, *, condition: str = ""):
    def check_condition(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs):
            if condition == "//":
                return func(*args, **kwargs)
            else:
                return None

        return wrapped_func

    if _func is None:
        return check_condition
    return check_condition(_func)


@callback(condition="//")
def example():
    print("Пример функции, которая возвращает ответ сервера")
    return "OK"


def main():
    response = example()
    if response:
        print("Ответ:", response)
    else:
        print("Такого пути нет")


if __name__ == "__main__":
    main()
