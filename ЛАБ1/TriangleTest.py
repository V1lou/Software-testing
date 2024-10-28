from unittest import *
from Triangle import Triangle
from math import sqrt

class TriangleTest(TestCase):
    # Обычный расчет площади (без исключений)

    # int
    def test1(self):
        test1 = Triangle(3, 4, 5)
        result1 = test1.getSquare()

        self.assertEqual(result1, 6)


    # float
    def test2(self):
        test1 = Triangle(2.5, 2.5, sqrt(12.5))
        result1 = test1.getSquare()

        self.assertEqual(result1, 3.125)


    #float
    def test3(self):
        test1 = Triangle(sqrt(4), sqrt(99), sqrt(103))
        result1 = test1.getSquare()

        self.assertEqual(result1, sqrt(99))



    # Расчет площади с исключениями


    # Первая сторона некорректная!
    def test4(self):
        test4 = Triangle('6', 8, 3)

        with self.assertRaisesRegex(TypeError, 'Первая сторона некорректная!'):
            test4.getSquare()


    # Вторая сторона некорректная!
    def test5(self):
        test5 = Triangle(6, '8', 3)

        with self.assertRaisesRegex(TypeError, 'Вторая сторона некорректная!'):
            test5.getSquare()


    # Третья сторона некорректная!
    def test6(self):
        test6 = Triangle(6, 8, '3')

        with self.assertRaisesRegex(TypeError, 'Третья сторона некорректная!'):
            test6.getSquare()


    # Первая сторона должна быть положительной!
    def test7(self):
        test7 = Triangle(-6, 8, 3)

        with self.assertRaisesRegex(ValueError, 'Первая сторона должна быть положительной!'):
            test7.getSquare()


    # Вторая сторона должна быть положительной!
    def test8(self):
        test8 = Triangle(6, -8, 3)

        with self.assertRaisesRegex(ValueError, 'Вторая сторона должна быть положительной!'):
            test8.getSquare()


    # Третья сторона должна быть положительной!
    def test9(self):
        test9 = Triangle(6, 8, -3)

        with self.assertRaisesRegex(ValueError, 'Третья сторона должна быть положительной!'):
            test9.getSquare()


    # Такого треугольника не существует!
    def test10(self):
        test10 = Triangle(1, 2, 5)

        with self.assertRaisesRegex(ValueError, 'Такого треугольника не существует!'):
            test10.getSquare()
