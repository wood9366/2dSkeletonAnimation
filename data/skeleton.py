import sys
from util import uid

class Skeleton(object):
    """skeleton data"""

    def __init__(self):
        self.__id = uid.generateUID()
        self.__bones = []
        self.__boneTop = None

    @property
    def id(self):
        return self.__id

    @property
    def top(self):
        return self.__boneTop

    def addBone(self, bone, parentBone = None):
        if (parentBone is None):
            if (self.__boneTop is not None):
                print "skeleton has top bone"
            else:
                self.__boneTop = bone
                self.__bones.append(bone)
        else:
            if (parentBone in self.__bones):
                self.__bones.append(bone)
                bone.parent = parentBone
                parentBone.addChild(bone)
            else:
                print "add a bone(%s)'s parent bone(%s) don't exist in skeleton" % (str(bone), str(parentBone))

        return bone

    def removeBone(self, bone):
        if (not bone.hasChild()):
            self.__bones.remove(bone)
            if (bone.parent is not None):
                bone.parent.removeChild(bone)

    def __str__(self):
        return "\n".join([str(bone) for bone in self.__bones])
