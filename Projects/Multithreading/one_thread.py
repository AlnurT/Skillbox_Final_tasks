"""
Однопоточное программирование

Задача:

- получить html
- узнать какие css и js файлы нужны для отображения
- подсчитать общий размер этих файлов
- вывести результат на консоль
"""
from threading import Thread
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from Multithreading.utils import timer


class PageSizer(Thread):
    def __init__(self, url: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.url_base: str = url
        self.size: int = 0

    def run(self) -> None:
        html_data = self._count_bytes(url=self.url_base)
        soup = BeautifulSoup(html_data, "lxml")

        for link in soup.find_all(name=["link", "script"]):
            if link.get("rel") == "stylesheet":
                extra_url = urljoin(self.url_base, link.get("href"))
            elif link.get("src"):
                extra_url = urljoin(self.url_base, link.get("src"))
            else:
                continue
            self._count_bytes(url=extra_url)

    def _count_bytes(self, url: str) -> str:
        url_req = requests.get(url)
        html_data = url_req.text
        size = len(html_data)
        self.size += size
        print(f"{url:<115} {size // 1024:<4} Kb ({size:<7} b)")
        return html_data


@timer
def main() -> None:
    sites = [
        "https://www.weblancer.net",
        "https://www.freelancer.com.ru",
        "https://kwork.ru",
        "https://work-zilla.com",
        "https://iklife.ru",
    ]
    sizers = [PageSizer(url=url) for url in sites]

    print(f"Сайт:{' ' * 110} Размер:")
    print("-" * 135)

    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()

    total_bytes = sum(sizer.size for sizer in sizers) // 1024
    print(f"\nОбщий размер: {total_bytes} Kb")


if __name__ == "__main__":
    main()
