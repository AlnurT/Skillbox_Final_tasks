"""Задача 5. ПИН-код

Недавно Влад решил протестировать новый электронный замок и с его помощью
запер свой чемодан. Правда, уже через час Влад забыл ПИН-код для открытия своего замка.
Поэтому он решил пойти путём brute force, то есть просто перебрать все возможные коды.

ПИН-код состоит из четырёх цифр. На каждой позиции ПИН-кода находится цифра от 0 до 9.
Позиции не зависят друг от друга.

Напишите программу, которая переберёт все возможные коды. Не используйте вложенные циклы.
"""
import itertools


def main():
    lock_code = 4269
    lock_code_t = tuple(lock_code // 10 ** (3 - n) % 10 for n in range(4))

    for code in itertools.product(range(10), repeat=4):
        if code == lock_code_t:
            print(code)
            break


if __name__ == "__main__":
    main()
