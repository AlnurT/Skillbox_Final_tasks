"""Задача 3. Пути файлов

Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам
указанной директории (по умолчанию — корневой диск),
находит указанный пользователем каталог и генерирует пути всех встреченных файлов.

Решение задачи должно быть без рекурсии.

Подсказка:
Существует функция, которая может получать все имена файлов в дереве каталогов.
Попробуйте найти ее самостоятельно.
"""
import os
from collections.abc import Iterable


def gen_files_path(directory: str, catalog: str) -> Iterable[str]:
    tree = os.walk(directory)
    for address, dirs, _ in tree:
        yield os.path.abspath(address)
        if catalog in dirs:
            yield os.path.join(address, catalog)
            return
    yield "Каталог не найден"


def main():
    directory_path = "C:\\Python_Projects\\Skillbox_Final_tasks"
    catalog = "Alnur"
    generator_path = gen_files_path(directory=directory_path, catalog=catalog)
    for path in generator_path:
        print(path)


if __name__ == "__main__":
    main()
