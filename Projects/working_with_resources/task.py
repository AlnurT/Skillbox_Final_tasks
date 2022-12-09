"""
Работа с ресурсами и базой данных

Задачи:
- Сохранить фото людей в папку
- Обрезать фото до портрета
- Сохранить в базу данных
"""
import os
import re

import requests
from bs4 import BeautifulSoup


def save_file(file_url: str) -> None:
    """
    Сохранение каждой фото в папку

    :param file_url: неполная ссылка на фото
    """

    filename_match = re.match(r".*/(\w+).*\.(\w+)", file_url)
    if filename_match and filename_match.group(1) != "def_avatar":
        file_name = ".".join(filename_match.groups())
        file_path = os.path.join(os.getcwd(), "photos", file_name)
        with open(file_path, "wb") as file:
            file.write(requests.get(file_url).content)


def find_url_with_img(url: str) -> None:
    """
    Сохранение всех фото в папку

    Функция ищет все фотографии по ссылке и сохраняет каждую в папку со своим именем
    :param url: ссылка на сайт для скачивания фотографий
    """
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    for link in soup.find_all("img"):
        file_url = f"https://spbau.ru/{link.get('src')}"
        if file_url:
            save_file(file_url)


def main() -> None:
    find_url_with_img(url="https://spbau.ru/kontaktyi/sotrudniki")


if __name__ == "__main__":
    main()
