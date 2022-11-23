"""
Однопоточное программирование

Задача:

- получить html
- узнать какие css и js файлы нужны для отображения
- подсчитать общий размер этих файлов
- вывести результат на консоль
"""
import time
from collections import defaultdict
from typing import Callable
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class PageSizer:
    def __init__(self, sites: list) -> None:
        self.sites: list = sites
        self.url_size: dict = defaultdict()

    def find_tag(self, url_base: str):
        html_data = self.count_bytes(url=url_base)
        soup = BeautifulSoup(html_data, "lxml")

        for link in soup.find_all(name=["link", "script"]):
            if link.get("rel") == "stylesheet":
                extra_url = urljoin(url_base, link.get("href"))
            elif link.get("src"):
                extra_url = urljoin(url_base, link.get("src"))
            else:
                continue
            self.count_bytes(url=extra_url)

    def count_bytes(self, url: str) -> str:
        url_req = requests.get(url)
        html_data = url_req.text
        self.url_size[url] = len(html_data)
        return html_data


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        func_time = round(time.time() - start, 2)
        print(f"Время выполнения операции: {func_time} c")
        return func

    return wrapped_func


@timer
def main() -> None:
    sites = [
        "https://www.weblancer.net",
        "https://www.freelancer.com.ru",
        "https://kwork.ru",
        "https://work-zilla.com",
        "https://iklife.ru",
    ]
    sizer = PageSizer(sites=sites)

    for url in sites:
        sizer.find_tag(url_base=url)

    print(f"Сайт:{' ' * 110} Размер:")
    print("-" * 135)
    for url, size in sizer.url_size.items():
        print(f"{url:<115} {size // 1024:<4} Kb ({size:<7} b)")

    total_bytes = sum(sizer.url_size.values()) // 1024
    print(f"\nОбщий размер: {total_bytes} Kb")


if __name__ == "__main__":
    main()
