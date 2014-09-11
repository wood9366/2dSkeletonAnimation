from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsScene, QBrush, QPen, QColor, QVector2D
from bone import GraphicItemBone
import math

class AnimationGraphicsScene(QGraphicsScene):
    Select, Move, Rotate = range(3)

    def __init__(self, parent = None):
        super(QGraphicsScene, self).__init__(parent)
        self.__bones = []
        self.__adjustMode = self.Select

    @property
    def adjustMode(self):
        return self.__adjustMode

    def initUI(self, x, y, w, h):
        self.setBackgroundBrush(QBrush(QColor(128, 128, 128), Qt.SolidPattern))
        self.setSceneRect(x, y, w, h)

        # coordinate
        rect = self.sceneRect()

        self.addLine(rect.left(), 0, rect.right(), 0, QPen(QColor(0, 0, 0)))
        self.addLine(0, rect.top(), 0, rect.bottom(), QPen(QColor(0, 0, 0)))

        # bones
        bone1 = self.__createBone(None)
        bone2 = self.__createBone(bone1)

    def __createBone(self, parent):
        bone = GraphicItemBone(parent, self)
        self.__bones.append(bone)
        return bone

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_E:
            self.__adjustMode = self.Rotate
        elif event.key() == Qt.Key_W:
            self.__adjustMode = self.Move
        else:
            self.__adjustMode = self.Select

        print "mode: %d" % (self.__adjustMode)
