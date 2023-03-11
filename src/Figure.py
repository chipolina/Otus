from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, a=None, b=None, c=None, radius=None):
        self.a = a
        self.b = b
        self.c = c
        self.radius = radius
        self._check_sides()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure) -> float:
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError

    def _check_sides(self):
        """
        Если стороны/радиус не равны None, проверяем принадлежность к int/float.
        Если стороны/радиус меньше или равна 0, выбрасываем ошибку
        """
        for side in [self.a, self.b, self.c, self.radius]:
            if not side is None:
                if not isinstance(side, (float, int)):
                    raise TypeError("Одна из сторон не является числом")
                if side <= 0:
                    raise ValueError("Одна из сторон меньше или равна 0")
