import unittest
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), os.path.pardir))
from lib.data.bone import Bone
del sys.path[0]
del sys
del os

class TestBone(unittest.TestCase):
    def test_construct(self):
        bone = Bone()

        self.assertTrue(isinstance(bone, Bone))
        self.assertEqual(bone._Bone__parent, None)
        self.assertEqual(len(bone._Bone__children), 0)

    def test_id(self):
        bone = Bone()

        self.assertEqual(bone.id, bone._Bone__id)

    def test_parent(self):
        bone = Bone()
        parent = Bone()

        self.assertEqual(bone.parent, None);
        
        bone.parent = parent;
        self.assertEqual(bone.parent, parent);

    def test_children(self):
        bone = Bone()
        child1 = Bone()
        child2 = Bone()

        bone.addChild(child1)

        self.assertEqual(len(bone._Bone__children), 1)
        self.assertEqual(child1.parent, bone)

        bone.addChild(child2)

        self.assertEqual(len(bone._Bone__children), 2)
        self.assertEqual(child2.parent, bone)

if __name__ == '__main__':
    unittest.main()
