"""Задача 1. Работа с файлом 2

Реализуйте модернизированную версию контекст-менеджера File:

- теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и
открывает этот файл в режиме записи;

- на выходе из менеджера подавляются все исключения, связанные с файлами.
"""
import os


class File:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> "File":
        if self.file_name in os.listdir():
            self.file = open(self.file_name, "a", encoding="utf-8")
        else:
            self.file = open(self.file_name, "w", encoding="utf-8")
        return self

    def write(self, text: str) -> None:
        self.file.write(text + "\n")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


def main() -> None:
    file_name = "logi.txt"
    with File(file_name) as file:
        file.write("Привет!")


if __name__ == "__main__":
    main()
