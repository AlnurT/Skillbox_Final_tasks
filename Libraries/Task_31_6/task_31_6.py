"""Задача 6. Web scraping

Дан несложный пример HTML-страницы: Sample Web Page.
Изучите код этой страницы и реализуйте программу, которая получает список всех
подзаголовков сайта (они заключены в теги h3).

Ожидаемый результат:

['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters',
'4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables',
'9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet',
'11. Where to go from here', '12. Postscript: Cell Phones']

Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.
"""
import re
from typing import List

import requests


def get_site_subtitles(code_str: str) -> List[str]:
    pattern = re.compile(r"<h3.*>(.*)</h3>")
    return pattern.findall(code_str)


def main():
    browser_page = requests.get("http://www.columbia.edu/~fdc/sample.html")

    subtitles_list = get_site_subtitles(browser_page.text)
    print(subtitles_list)


if __name__ == "__main__":
    main()
