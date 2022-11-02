"""Задача 3. Моделирование

В проекте по 3D-моделированию используются две фигуры — куб и пирамида.
Для моделирования этих фигур используются соответствующие 2D-фигуры,
а именно квадрат и треугольник.
Вся поверхность 3D-фигуры может храниться в виде списка.
Например, для куба это будет [Square, Square, Square, Square, Square, Square].

Квадрат инициализируется длинами сторон, а треугольник — основанием и высотой.
Каждая из 2D-фигур умеет находить свои периметр и площадь, а 3D-фигуры,
в свою очередь, могут находить площадь своей поверхности.

Используя входные данные о фигурах и знания математики, реализуйте соответствующие
классы и методы. Для базовых классов также реализуйте геттеры и сеттеры.
"""
from math import sqrt


class Square:
    def __init__(self, square_side: int) -> None:
        self.__square_side = square_side

    @property
    def square_side(self) -> int:
        return self.square_side

    @square_side.setter
    def square_side(self, square_side: int) -> None:
        self.__square_side = square_side

    @property
    def square_surface_area(self) -> int:
        return self.__square_side**2

    @property
    def square_perimeter(self) -> int:
        return self.__square_side * 4


class Triangle:
    def __init__(self, base: int, triangle_height: int) -> None:
        self.__base = base
        self.__triangle_height = triangle_height

    @property
    def base(self) -> int:
        return self.__base

    @base.setter
    def base(self, base: int) -> None:
        self.__base = base

    @property
    def triangle_height(self) -> int:
        return self.__triangle_height

    @triangle_height.setter
    def triangle_height(self, triangle_height: int) -> None:
        self.__triangle_height = triangle_height

    @property
    def triangle_surface_area(self) -> int:
        return round(self.__base * self.__triangle_height / 2)

    @property
    def triangle_perimeter(self) -> int:
        triangle_side = sqrt(self.__triangle_height**2 + (self.__base / 2) ** 2)
        return round(self.__base + triangle_side * 2)


class Cube(Square):
    def __init__(self, cube_side: int) -> None:
        super().__init__(square_side=cube_side)
        self.__surfaces_list = [Square(square_side=cube_side) for _ in range(6)]
        self.__cube_surface_area = 0

    @property
    def cube_surface_area(self) -> int:
        for surface in self.__surfaces_list:
            self.__cube_surface_area += surface.square_surface_area
        return self.__cube_surface_area


class Pyramid(Square, Triangle):
    def __init__(self, pyramid_base: int, pyramid_height: int) -> None:
        Square.__init__(self, square_side=pyramid_base)
        self.triangle_height = round(
            sqrt(pyramid_height**2 + (pyramid_base / 2) ** 2)
        )
        Triangle.__init__(self, base=pyramid_base, triangle_height=self.triangle_height)
        self.__pyramid_height = pyramid_height
        self.__surfaces_list = [
            Triangle(base=pyramid_base, triangle_height=self.triangle_height)
            if surface < 4
            else Square(square_side=pyramid_base)
            for surface in range(5)
        ]
        self.__pyramid_surface_area = 0

    @property
    def pyramid_surface_area(self) -> int:
        for surface in self.__surfaces_list:
            if isinstance(surface, Triangle):
                self.__pyramid_surface_area += surface.triangle_surface_area
            elif isinstance(surface, Square):
                self.__pyramid_surface_area += surface.square_surface_area
        return self.__pyramid_surface_area


def main():
    cube = Cube(cube_side=5)
    print(f"Площадь поверхности куба: {cube.cube_surface_area}")
    print(f"Площадь грани: {cube.square_surface_area}")
    print(f"Периметр грани: {cube.square_perimeter}\n")

    pyramid = Pyramid(pyramid_base=6, pyramid_height=4)
    print(f"Площадь поверхности пирамиды: {pyramid.pyramid_surface_area}")
    print(f"Площадь боковой поверхности: {pyramid.triangle_surface_area}")
    print(f"Периметр боковой поверхности: {pyramid.triangle_perimeter}")
    print(f"Площадь основания: {pyramid.square_surface_area}")
    print(f"Периметр основания: {pyramid.square_perimeter}")


if __name__ == "__main__":
    main()
