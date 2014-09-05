import math

class Vector2(object):
    """Vector2"""

    @staticmethod
    def Length(v1, v2):
        return v1.length(v2)

    @staticmethod
    def Distance(v1, v2):
        return Vector2(v1.x, v1.y).minus(v2).length()

    @staticmethod
    def Plus(v1, v2):
        return Vector2(v1.x, v1.y).plus(v2)

    @staticmethod
    def Minus(v1, v2):
        return Vector2(v1.x, v1.y).minus(v2)

    @staticmethod
    def Dot(v1, v2):
        return v1.dot(v2)

    @staticmethod
    def Mul(v, m):
        return v.mul(m)

    def __init__(self, x = 0, y = 0):
        self.__set(x, y)

    def __set(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def length(self):
        return math.sqrt(self.__x * self.__x + self.__y * self.__y)

    def identity(self):
        l = self.length()

        if (l > 0):
            self.__x /= l
            self.__y /= l

    def plus(self, v):
        self.__x += v.x
        self.__y += v.y
        return self

    def minus(self, v):
        self.__x -= v.x
        self.__y -= v.y
        return self

    def dot(self, v):
        return self.__x * v.x + self.__y * v.y

    def mul(self, m23):
        x = self.__x * m23.val(0,0) + self.__y * m23.val(1,0) + m23.val(2,0)
        y = self.__x * m23.val(0,1) + self.__y * m23.val(1,1) + m23.val(2,1)

        self.__set(x, y)

        return self

Zero = Vector2(0, 0)
X = Vector2(1, 0)
Y = Vector2(0, 1)
