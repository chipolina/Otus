
import pytest

from src.Square import Square
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Circle import Circle


class TestFigures:
    """
    Класс с тестами на расчет площади, периметра и
    возможности создания каждой фигуры.

    """

    @pytest.mark.parametrize("a,b,c, area, perimeter", [
        pytest.param(13, 13, 13, 73.18, 19.5, id="isosceles triangle"),
        pytest.param(13.0, 14, 15, 84, 21, id="Float number"),
        pytest.param(13, 14, 15, 84, 21, id="Int number")
    ])
    def test_check_good_triangle(self, a, b, c, area, perimeter):
        """
        Проверяем создание треугольника

        :param a: Сторона 1
        :param b: Сторона 2
        :param c: Сторона 3
        :param area: Ожидаемая площадь
        :param perimeter: Ожидаемый периметр
        """
        figure = Triangle(a, b, c)
        assert figure.area == area
        assert figure.perimeter == perimeter

    @pytest.mark.parametrize("a,b,c,error", [
        pytest.param(4, 5, 10, ValueError, id="Incorrect Triangle"),
        pytest.param('4', 5, 10, TypeError, id="String char"),
        pytest.param(-4, 5, 10, ValueError, id="Negative side"),
        pytest.param(0, 5, 10, ValueError, id="Zero Side")
    ])
    def test_check_bad_triangle(self, a, b, c, error):
        """
        Проверяем ошибки при создании треугольника
        :param a: Сторона 1
        :param b: Сторона 2
        :param c: Сторона 3
        :param error: Ожидаемая ошибка
        """
        with pytest.raises(error):
            Triangle(a, b, c)

    @pytest.mark.parametrize("a, area, perimeter", [
        pytest.param(15, 225, 30, id="Int numbers"),
        pytest.param(15.0, 225, 30, id="Float number")
    ])
    def test_check_good_square(self, a, area, perimeter):
        """
        Проверяем создание Квадрата
        :param a: Сторона
        :param area: Ожидаемая площадь
        :param perimeter: Ожидаемый периметр
        """
        figure = Square(a)
        assert figure.area == area
        assert figure.perimeter == perimeter

    @pytest.mark.parametrize("a, error", [
        pytest.param(-15, ValueError, id="Negative side"),
        pytest.param("15.0", TypeError, id="String char"),
        pytest.param(0, ValueError, id="Zero Side"),
    ])
    def test_check_bad_square(self, a, error):
        """
        Проверяем ошибки при создании Квадрата
        :param a: Сторона
        :param error: Ожидаемая ошибка
        """
        with pytest.raises(error):
            Square(a)

    @pytest.mark.parametrize("a, b, area, perimeter", [
        pytest.param(15, 10, 150, 50, id="Int numbers"),
        pytest.param(15.0, 10, 150.0, 50.0, id="Float number")
    ])
    def test_check_good_rectangle(self, a, b, area, perimeter):
        """
        Проверяем создание Прямоугольника
        :param a: Длина
        :param b: Ширина
        :param area: Ожидаемая площадь
        :param perimeter: Ожидаемый периметр

        """
        figure = Rectangle(a, b)
        assert figure.area == area
        assert figure.perimeter == perimeter

    @pytest.mark.parametrize("a, b, error", [
        pytest.param(-15, 10, ValueError, id="Negative side"),
        pytest.param("15.0", 10, TypeError, id="String char"),
        pytest.param(0, 225, ValueError, id="Zero Side"),
    ])
    def test_check_bad_rectangle(self, a, b, error):
        """
        Проверяем ошибки при создании прямоугольника
        :param a: Длина
        :param b: Ширина
        :param error: Ожидаемая ошибка
        """
        with pytest.raises(error):
            Rectangle(a, b)

    @pytest.mark.parametrize("a, area, perimeter", [
        pytest.param(15, 706.86, 94.25, id="Int numbers"),
        pytest.param(15.0, 706.86, 94.25, id="Float number")
    ])
    def test_check_good_circle(self, a, area, perimeter):
        """
        Проверяем создание Круга
        :param a: Радиус
        :param area: Ожидаемая площадь
        :param perimeter: Ожидаемая длина окружности
        """
        figure = Circle(a)
        assert figure.area == area
        assert figure.perimeter == perimeter

    @pytest.mark.parametrize("a, error", [
        pytest.param(-15, ValueError, id="Negative side"),
        pytest.param("15.0", TypeError, id="String char"),
        pytest.param(0, ValueError, id="Zero Side"),
    ])
    def test_check_bad_circle(self, a, error):
        """
        Проверяем ошибки при создании Круга
        :param a: Радиус
        :param error: Ожидаемая ошибка
        """
        with pytest.raises(error):
            Circle(a)


class TestFigureMethods:
    """
    Класс с тестами на расчет суммирования площадей 2 фигур

    """

    def test_square_triangle_add_area(self):
        """
        Проверяем расчет Квадрата и Треугольника

        """
        fig1 = Square(10)
        fig2 = Triangle(13, 14, 15)
        assert fig2.add_area(fig1) == 184

    def test_circle_rectangle_add_area(self):
        """
        Проверяем расчет Круга и Прямоугольника

        """
        fig1 = Circle(15)
        fig2 = Rectangle(10, 15)
        assert fig2.add_area(fig1) == 856.86

    def test_check_add_area_error(self):
        """
        Проверяем, что можем суммировать только экземпляры класса Figure

        """
        fig1 = 100
        fig2 = Triangle(13, 14, 15)
        with pytest.raises(ValueError):
            fig2.add_area(fig1)
