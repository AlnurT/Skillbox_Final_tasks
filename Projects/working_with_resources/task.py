"""
Работа с ресурсами и базой данных

Задачи:
- Сохранить фото людей в папку
- Обрезать фото до портрета
- Сохранить в базу данных
"""
import re

import requests
from bs4 import BeautifulSoup


def save_all_photos(url: str) -> None:
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    for link in soup.find_all("img"):
        file_path = link.get("src")
        filename_match = re.match(r".*/(\w+).*\.(\w+)", file_path)
        if filename_match:
            filename = ".".join(filename_match.groups())
            print(filename)


def main() -> None:
    save_all_photos(url="https://spbau.ru/kontaktyi/sotrudniki")


if __name__ == "__main__":
    main()
