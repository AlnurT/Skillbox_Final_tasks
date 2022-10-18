"""Задача 4. Последовательность Хофштадтера

Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором).
Сама последовательность выглядит так:

Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))

В итератор (или генератор) передаётся список из двух чисел.
Например, QHofstadter([1, 1]) генерирует точную последовательность Хофштадтера.
Если передать значения [1, 2], то последовательность должна немедленно завершиться.
"""
from collections.abc import Iterable


def get_qhofstadter_sequence(q: list, sequence_len: int = 20) -> Iterable[int]:
    if not q[0] == q[1] == 1:
        sequence_len = 2
    for n in range(sequence_len):
        if n > 1:
            q.append(q[n - q[n - 1]] + q[n - q[n - 2]])
        yield q[n]


def main():
    numbers = [1, 1]
    qhofstadter_sequence = get_qhofstadter_sequence(q=numbers)
    for q in qhofstadter_sequence:
        print(q, end=" ")


if __name__ == "__main__":
    main()
