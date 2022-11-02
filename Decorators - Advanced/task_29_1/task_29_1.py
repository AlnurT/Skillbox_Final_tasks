"""Задача 1. Права доступа

На вас возложили задачу по созданию и поддержке специализированного сайта-форума.
Вы только начали выполнять задачу и сейчас остановились на реализации действий,
которые могут совершать посетители форума.
И конечно же, для разных пользователей прописаны разные возможности.

Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ
к вызываемой функции, и если нет, то выдаёт исключение PermissionError.

Пример кода:

user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

Результат:
Удаляем сайт
PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment
"""
from typing import Callable


def check_permission(user: str) -> Callable:
    def check_user_name(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs):
            try:
                if user.lower() != "admin":
                    raise PermissionError
            except PermissionError:
                print(
                    f"PermissionError: У пользователя недостаточно прав, "
                    f"чтобы выполнить функцию {func.__name__}"
                )
                return None
            return func(*args, **kwargs)

        return wrapped_func

    return check_user_name


def main():
    @check_permission("admin")
    def delete_site():
        print("Удаляем сайт")

    @check_permission("user_1")
    def add_comment():
        print("Добавляем комментарий")

    delete_site()
    add_comment()


if __name__ == "__main__":
    main()
