"""Задача 5. Синглтон

Синглтон — это порождающий паттерн проектирования, который гарантирует,
что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.
Синглтонами мы уже пользовались, к ним относятся, например, None, True и False.
Именно потому, что None является синглтоном,
мы можем использовать оператор is — он возвращает True только для объектов,
представляющих одну и ту же сущность.

Реализуйте декоратор singleton, который превращает класс в одноэлементный.
То есть при множественной инициализации объекта этого класса будет сохранён
только первый инстанс, а все остальные попытки создания будут возвращать первый экземпляр.

Пример кода:

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)

Результат:
1986890616688
1986890616688
True
"""


def singleton(cls):
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None

    return wrapper


@singleton
class Example:
    pass


def main():
    my_obj = Example()
    my_another_obj = Example()

    print(id(my_obj))
    print(id(my_another_obj))
    print(my_obj is my_another_obj)


if __name__ == "__main__":
    main()
