"""Задача 2. Математический модуль

Ирина использует в своей программе очень много различных математических вычислений,
связанных с фигурами. Например, нахождение их площадей или периметров.
Поэтому, чтобы не захламлять код огромным количеством функций,
она решила выделить для них отдельный класс, подключить как модуль и использовать
по аналогии с модулем math.

Реализуйте класс MyMath, состоящий как минимум из следующих методов
(можете бонусом добавить и другие методы):

— вычисление длины окружности,
— вычисление площади окружности,
— вычисление объёма куба,
— вычисление площади поверхности сферы.

Пример основного кода:

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

Результат:
31.41592653589793
113.09733552923255
"""
from abc import ABC, abstractmethod
from math import pi


class MyMath(ABC):
    @classmethod
    @abstractmethod
    def circle_len(cls, radius: int):
        return 2 * pi * radius

    @classmethod
    @abstractmethod
    def circle_sq(cls, radius: int):
        return pi * radius**2

    @classmethod
    @abstractmethod
    def cube_volume(cls, side: int):
        return side**3

    @classmethod
    @abstractmethod
    def sphere_surface_area(cls, radius: int):
        return 4 * pi * radius**2


def main():
    res_1 = MyMath.circle_len(radius=5)
    res_2 = MyMath.circle_sq(radius=6)
    res_3 = MyMath.cube_volume(side=4)
    res_4 = MyMath.sphere_surface_area(radius=2)
    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)


if __name__ == "__main__":
    main()
