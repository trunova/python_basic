import math


class Square:
    """
    Базовый класс Квадрат
    """
    def __init__(self, side: float):
        self._side = side

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, side):
        self._side = side

    def perimeter(self) -> float:
        return 4 * self._side

    def square(self) -> float:
        return self._side * self._side


class Triangle:
    """
    Базовый класс Треугольник
    """
    def __init__(self, base: float, height: float):
        self._base = base
        self._height = height

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def perimeter(self) -> float:
        return math.sqrt(self._height * self._height + self._base * self._base / 4) * 2 + self._base

    def square(self) -> float:
        return self._base * self._height / 2


class Cube:
    """
    Класс, реализующий Куб
    """

    def __init__(self, square: Square):
        self._listSquare = list()
        for _ in range(0, 6):
            self._listSquare.append(square)

    def surfaceArea(self) -> float:
        return 6 * self._listSquare[0].getSide()


class Pyramid:
    """
    Класс, реализующий Пирамиду
    """

    def __init__(self, square: Square, triangle: Triangle):
        self._listFigures = list()
        self._listFigures.append(square)
        for _ in range(0, 4):
            self._listFigures.append(triangle)

    def surfaceArea(self) -> float:
        return self._listFigures[0].square() + self._listFigures[1].getHeight() * (self._listFigures[0].perimeter() / 2)