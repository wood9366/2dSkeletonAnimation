class Matrix23(object):
    """Matrix 2 x 3"""

    @staticmethod
    def Mul(m1, m2):
        return m1.mul(m2)

    def __init__(self, vals = []):
        self.__set(vals)

    def __set(self, vals):
        if (len(vals) == 0):
            self.__m = [[0,0], [0,0], [0,0]]
        else:
            self.__m = [vals[:2], vals[2:4], vals[4:6]]
    
    def val(self, x, y):
        return self.__m[x][y]

    def mul(self, m):
        m00 = self.__m[0][0] * m[0][0] + self.__m[0][1] * m[1][0]
        m01 = self.__m[0][0] * m[0][1] + self.__m[0][1] * m[1][1]
        m10 = self.__m[1][0] * m[0][0] + self.__m[1][1] * m[1][0]
        m11 = self.__m[1][0] * m[0][1] + self.__m[1][1] * m[1][1]
        m20 = self.__m[2][0] * m[0][0] + self.__m[2][1] * m[1][0] + m[2][0]
        m21 = self.__m[2][0] * m[0][1] + self.__m[2][1] * m[1][1] + m[2][1]

        self.__set([m00, m01, m10, m11, m20, m21]);

        return self

Identify = Matrix23([1,0,0,1,0,0])
Zero = Matrix23([0,0,0,0,0,0])
