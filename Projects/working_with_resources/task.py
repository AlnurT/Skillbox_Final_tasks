"""
Работа с ресурсами и базой данных

Задачи:
- Сохранить фото людей в папку
- Сохранить в базу данных
"""
import os
import re

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


def save_photo_add_in_database(file_url: str) -> None:
    """
    Сохранение каждой фото в папку и базу данных

    :param file_url: неполная ссылка на фото
    """

    filename_match = re.match(r".*/(\w+).*\.(\w+)", file_url)
    if filename_match:
        if filename_match.group(1) != "def_avatar" and filename_match.group(2) == "jpg":
            file_name = ".".join(filename_match.groups())
            img_path = os.path.join(os.getcwd(), "photos", file_name)
            with open(img_path, "wb") as file:
                img = requests.get(file_url).content
                file.write(img)
            Photos.create(name=file_name, path=img_path, url=file_url)


@timer
def main() -> None:
    url = "https://spbau.ru/kontaktyi/sotrudniki"
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    Photos.create_table()
    for link in soup.find_all("img"):
        file_url = f"https://spbau.ru/{link.get('src')}"
        if file_url:
            save_photo_add_in_database(file_url=file_url)


if __name__ == "__main__":
    main()
