import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), os.path.pardir))
from lib.math.matrix23 import Matrix23
from lib.math.vector2 import Vector2
del sys.path[0]
del sys
del os

class TestMath(unittest.TestCase):
    def test_vector_construct(self):
        v = Vector2()
        
        self.assertEqual(v._Vector2__x, 0)
        self.assertEqual(v._Vector2__y, 0)

        v = Vector2(5, 8)

        self.assertEqual(v._Vector2__x, 5)
        self.assertEqual(v._Vector2__y, 8)

    def test_vector_xy(self):
        v = Vector2()

        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)

        v.x = 5
        self.assertEqual(v.x, 5)

        v.y = 20
        self.assertEqual(v.y, 20)

    def test_vector_length(self):
        v = Vector2(15, 32)

        self.assertAlmostEqual(v.length(), 35.3412, 4)

    def test_vector_distance(self):
        v1 = Vector2(4, 8)
        v2 = Vector2(13, 23)

        self.assertAlmostEqual(Vector2.Distance(v1, v2), 17.4929, 4)

    def test_vector_identity(self):
        v = Vector2(15, 32)

        v.identity()

        self.assertAlmostEqual(v.x, 0.4244, 4)
        self.assertAlmostEqual(v.y, 0.9055, 4)

    def test_vector_plus(self):
        v1 = Vector2(3, 12)
        v2 = Vector2(33, 24)

        v1.plus(v2)

        self.assertEqual(v1.x, 36)
        self.assertEqual(v1.y, 36)

        v3 = Vector2(22, 32)
        v4 = Vector2(12, 9)

        v5 = Vector2.Plus(v3, v4)
        self.assertEqual(v5.x, 34)
        self.assertEqual(v5.y, 41)

    def test_vector_minus(self):
        v1 = Vector2(14, 20)
        v2 = Vector2(203, 22)

        v1.minus(v2)

        self.assertEqual(v1.x, -189)
        self.assertEqual(v1.y, -2)

        v3 = Vector2(12, 45)
        v4 = Vector2.Minus(v3, v2)
        self.assertEqual(v4.x, -191)
        self.assertEqual(v4.y, 23)

    def test_vector_dot(self):
        v1 = Vector2(20, 18)
        v2 = Vector2(3, 4)

        self.assertEqual(v1.dot(v2), 132)
        self.assertEqual(Vector2.Dot(v1, v2), 132)

    def test_vector_mul(self):
        v = Vector2(5, 12)
        m = Matrix23([1,2,3,4,5,6])

        v.mul(m)
        self.assertEqual(v.x, 46)
        self.assertEqual(v.y, 64)

        v1 = Vector2(14, 20)
        m1 = Matrix23([3,4,5,6,7,8])
        v2 = Vector2.Mul(v1, m1)
        self.assertEqual(v2.x, 149)
        self.assertEqual(v2.y, 184)

if __name__ == '__main__':
    unittest.main()
