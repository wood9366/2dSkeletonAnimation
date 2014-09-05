import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), os.path.pardir))
from lib.data.skeleton import Skeleton
from lib.data.bone import Bone
del sys.path[0]
del sys
del os

class TestSkeleton(unittest.TestCase):
    def test_construct(self):
        skeleton = Skeleton()

        self.assertTrue(isinstance(skeleton, Skeleton))

        self.assertEqual(skeleton._Skeleton__boneTop, None)
        self.assertEqual(len(skeleton._Skeleton__bones), 0)

    def test_boneTop(self):
        skeleton = Skeleton()
        self.assertEqual(skeleton.top, None)

        bone1 = skeleton.addBone(Bone())
        self.assertEqual(skeleton.top, bone1)

        bone2 = skeleton.addBone(Bone())
        self.assertEqual(skeleton.top, bone1)

    def test_addRemoveBone(self):
        skeleton = Skeleton()
        bone1 = Bone()
        bone2 = Bone()
        bone3 = Bone()

        skeleton.addBone(bone1)
        self.assertEqual(len(skeleton._Skeleton__bones), 1)
        self.assertEqual(skeleton.top, bone1)

        skeleton.addBone(bone2, bone1)
        self.assertEqual(len(skeleton._Skeleton__bones), 2)
        self.assertEqual(bone2.parent, bone1)

        skeleton.addBone(bone3, bone2)
        self.assertEqual(len(skeleton._Skeleton__bones), 3)
        self.assertEqual(bone3.parent, bone2)

if __name__ == '__main__':
    unittest.main()
