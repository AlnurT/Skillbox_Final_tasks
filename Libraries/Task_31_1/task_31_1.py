"""Задача 1. Lorem ipsum

Для макетов веб-страниц часто используется какой-нибудь текст-рыба — это условный,
зачастую бессмысленный текст-заполнитель. Пусть дан следующий сгенерированный текст:

Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aenean commodo ligula eget dolor. Aenean massa.
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate

Напишите программу, которая обрабатывает этот текст и выводит список слов,
состоящих ровно из четырёх букв.

Результат:
['amet', 'elit', 'eget', 'quam', 'quis', 'quis', 'enim', 'pede']
"""
import re


def main():
    text = (
        " Lorem ipsum dolor sit amet, consectetuer adipiscing elit. "
        "Aenean commodo ligula eget dolor. Aenean massa. "
        "Cum sociis natoque penatibus et magnis dis parturient montes, "
        "nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, "
        "pretium quis, sem. Nulla consequat massa quis enim. "
        "Donec pede justo, fringilla vel, aliquet nec, vulputate"
    )

    list_with_four_words = re.findall(r"\b\w{4}\b", text)
    print(list_with_four_words)


if __name__ == "__main__":
    main()
