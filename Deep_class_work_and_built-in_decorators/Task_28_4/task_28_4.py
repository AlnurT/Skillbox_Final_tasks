"""Задача 4. Дата

Реализуйте класс Date, который должен:

проверять числа даты на корректность;
конвертировать строку даты в объект класса Date,
состоящий из соответствующих числовых значений дня, месяца и года.
Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

При тестировании программы объект класса Date должен инициализироваться исключительно
через метод конвертации, например: date = Date.from_string('10-12-2077').

Неверный вариант: date = Date(10, 12, 2077).

Пример основного кода:

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

Результат:
День: 10    Месяц: 12    Год: 2077
True
False
"""
from datetime import datetime


class Date:
    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        try:
            datetime.strptime(data, "%d-%m-%Y")
        except ValueError:
            return False
        return True

    @classmethod
    def from_string(cls, data: str) -> str:
        if cls.is_date_valid(data):
            day, month, year = data.split("-")
            return f"День: {day}\tМесяц: {month}\tГод: {year}"
        return f"{data} - неверный формат даты"


def main() -> None:
    print(Date.is_date_valid("10-12-2077"))
    print(Date.from_string("10-12-2077"))
    print()
    print(Date.is_date_valid("31-11-2077"))
    print(Date.from_string("31-11-2077"))


if __name__ == "__main__":
    main()
