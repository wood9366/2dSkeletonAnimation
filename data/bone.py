from util import uid
from PyQt4 import QtGui, QtCore

class Bone(object):
    """Bone data"""

    def __init__(self):
        self.__id = uid.generateUID()

        self.__name = "bone" + self.__id
        self.__pos = QtCore.QPointF(0, 0)
        self.__scale = QtCore.QPointF(1, 1)
        self.__length = 0
        self.__angle = 0

        self.__nodes = []

        self.__parent = None
        self.__children = []

    @property
    def id(self):
        return self.__id

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, bone):
        self.__parent = bone

    def hasChild(self):
        return len(self.__children) > 0

    def addChild(self, bone):
        if bone not in self.__children:
            self.__children.append(bone)
            bone.parent = self

    def removeChild(self, bone):
        if bone in self.__children:
            self.__children.remove(bone)
            bone.parent = None

    def __str__(self):
        args = [self.__id, (self.__parent.id if (self.__parent is not None) else -1)]
        for child in self.__children:
            args.append(child.id)

        return ("bone %d (%d|" + (",".join(["%d"] * len(self.__children))) + ")") % tuple(args)
