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
"""from math import sqrt"""


class Square:
    def __init__(self, side: int) -> None:
        self.__side = side

    @property
    def square_side(self) -> int:
        return self.square_side

    @square_side.setter
    def square_side(self, side: int) -> None:
        self.__side = side

    @property
    def square_surface_area(self) -> int:
        return self.__side**2

    @property
    def square_perimeter(self) -> int:
        return self.__side * 4


"""class Triangle:
    @property
    def surface_area(self) -> int:
        return self.surface_area

    @surface_area.setter
    def surface_area(self, base_height: tuple) -> None:
        base, height = base_height
        self.surface_area = base * height / 2

    @property
    def perimeter(self) -> int:
        return self.perimeter

    @perimeter.setter
    def perimeter(self, base_height: tuple) -> None:
        side = sqrt(self.__height ** 2 + (self.__base / 2) ** 2)
        self.perimeter = self.__base + side * 2"""


class Cube(Square):
    def __init__(self, side: int) -> None:
        super().__init__(side)
        self.__surfaces_list = [Square(side=side) for _ in range(6)]
        self.__cube_surface_area = 0

    @property
    def cube_surface_area(self) -> int:
        for surface in self.__surfaces_list:
            self.__cube_surface_area += surface.square_surface_area
        return self.__cube_surface_area


"""class Pyramid(Square, Triangle):
    def __init__(self, base: int, height: int) -> None:
        self.__base = base
        self.__height = height
        self.__surfaces_list = [Triangle for _ in range(4)]
        self.__cube_surface_area = 0

    def calculate_cube_area(self) -> int:
        for _ in self.__surfaces_list:
            self.__cube_surface_area += self.calculate_square_area()
        return self.__cube_surface_area"""


def main():
    cube = Cube(side=5)
    print(f"Площадь поверхности куба: {cube.cube_surface_area}")
    print(f"Площадь грани: {cube.square_surface_area}")
    print(f"Периметр грани: {cube.square_perimeter}")


"""    pyramid = Pyramid(base=4, height=5)
    print(f"Площадь поверхности куба: {cube.calculate_cube_area}")
    print(f"Площадь грани: {cube.surface_area}")
    print(f"Периметр грани: {cube.perimeter}")"""


if __name__ == "__main__":
    main()
