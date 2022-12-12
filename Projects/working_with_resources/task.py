"""
Работа с ресурсами и базой данных

Задачи:
- Сохранить фото людей в папку
- Сохранить в базу данных
"""
import os
import re
from multiprocessing import Process

import peewee
import requests
from bs4 import BeautifulSoup
from working_with_resources.utils import timer


class Photos(peewee.Model):
    """
    Класс таблицы базы данных
    """

    name = peewee.CharField()
    path = peewee.CharField()
    url = peewee.CharField()

    class Meta:
        database = peewee.SqliteDatabase("photo.db")


class PhotoSaver(Process):
    def __init__(self, file_url: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.file_url = file_url

    def run(self) -> None:
        """
        Сохранение каждой фото в папку и базу данных
        """

        filename_match = re.match(r".*/(\w+).*\.(\w+)", self.file_url)
        if filename_match and filename_match.group(1) != "def_avatar":
            file_name = ".".join(filename_match.groups())
            img_path = os.path.join(os.getcwd(), "photos", file_name)
            with open(img_path, "wb") as file:
                img = requests.get(self.file_url).content
                file.write(img)
            Photos.create(name=file_name, path=img_path, url=self.file_url)


@timer
def main() -> None:
    url = "https://spbau.ru/kontaktyi/sotrudniki"
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    Photos.create_table()

    finder = []
    for link in soup.find_all("img"):
        file_url = f"https://spbau.ru/{link.get('src')}"
        if file_url:
            finder.append(PhotoSaver(file_url=file_url))

    for photo in finder:
        photo.start()
    for photo in finder:
        photo.join()


if __name__ == "__main__":
    main()
