"""Задача 4. Дебаг

Напишите декоратор debug, который при каждом вызове декорируемой функции выводит её имя
(вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает.
После этого выводится результат её выполнения.

Пример декорируемой функции:
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

Основной код:
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

Результат:
Вызывается greeting('Том')
'greeting' вернула значение 'Привет, Том!'
Привет, Том!

Вызывается greeting('Миша', age=100)
'greeting' вернула значение 'Ого, Миша! Тебе уже 100 лет, ты быстро растёшь!'
Ого, Миша! Тебе уже 100 лет, ты вырос!

Вызывается greeting(name='Катя', age=16)
'greeting' вернула значение 'Ого, Катя! Тебе уже 16 лет, ты быстро растёшь!'
Ого, Катя! Тебе уже 16 лет, ты быстро растешь!

Совет: попробуйте самостоятельно изучить функцию repr. Это поможет в решении задачи.
"""
from typing import Callable


def debug(func: Callable) -> Callable:
    return func


@debug
def greeting(name, age=None) -> str:
    if age:
        return f"Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!"
    return f"Привет, {name}!"


def main() -> None:
    func_name = greeting.__name__

    func = greeting("Том")
    print(f"{repr(func_name)} вернула значение {repr(func)}")
    print(func)

    func = greeting(name="Том", age=18)
    print(f"{repr(func_name)} вернула значение {repr(func)}")
    print(func)


if __name__ == "__main__":
    main()
