from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exception(self):
        a, b, c = self.a, self.b, self.c

        if type(a) not in [int, float]:
            raise TypeError('Первая сторона некорректная!')

        if type(b) not in [int, float]:
            raise TypeError('Вторая сторона некорректная!')

        if type(c) not in [int, float]:
            raise TypeError('Третья сторона некорректная!')

        if a <= 0:
            raise ValueError('Первая сторона должна быть положительной!')

        if b <= 0:
            raise ValueError('Вторая сторона должна быть положительной!')

        if c <= 0:
            raise ValueError('Третья сторона должна быть положительной!')

        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError('Такого треугольника не существует!')


    def getSquare(self):
        self.exception()

        a, b, c = self.a, self.b, self.c

        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))




