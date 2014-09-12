from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsScene, QBrush, QPen, QColor, QVector2D
from bone import GraphicItemBone
import math

class AnimationGraphicsScene(QGraphicsScene):
    Select, Move, Rotate, Link = range(4)

    def __init__(self, parent = None):
        super(QGraphicsScene, self).__init__(parent)
        self.__bones = []
        self.__adjustMode = self.Select

        self.__linkFrom = None

    @property
    def adjustMode(self):
        return self.__adjustMode

    @adjustMode.setter
    def adjustMode(self, mode):
        self.__adjustMode = mode

    def initUI(self, x, y, w, h):
        self.setBackgroundBrush(QBrush(QColor(128, 128, 128), Qt.SolidPattern))
        self.setSceneRect(x, y, w, h)

        # coordinate
        rect = self.sceneRect()

        self.addLine(rect.left(), 0, rect.right(), 0, QPen(QColor(0, 0, 0)))
        self.addLine(0, rect.top(), 0, rect.bottom(), QPen(QColor(0, 0, 0)))

    def __createBone(self, parent):
        bone = GraphicItemBone(parent, self)
        self.__bones.append(bone)
        return bone

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_E:
            self.adjustMode = self.Rotate
        elif event.key() == Qt.Key_W:
            self.adjustMode = self.Move
        elif event.key() == Qt.Key_L:
            self.adjustMode = self.Link
            self.__linkFrom = self.__linkTo = None
        else:
            self.adjustMode = self.Select

        print "mode: %d" % (self.__adjustMode)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.adjustMode == self.Select:
                bone = self.__createBone(None)
                bone.setPos(bone.mapToParent(bone.mapFromScene(event.scenePos())))
            else:
                self.__adjustMode = self.Select
        elif event.button() == Qt.LeftButton:
            if self.adjustMode == self.Link:
                item = self.itemAt(event.scenePos())
                if self.__linkFrom is None:
                    if item is not None:
                        self.__linkFrom = item
                else:
                    pos = self.__linkFrom.scenePos()
                    self.__linkFrom.setParentItem(item)
                    if item is not None: self.__linkFrom.setPos(item.mapFromScene(pos))
                    self.adjustMode = self.Select
            else:
                super(AnimationGraphicsScene, self).mousePressEvent(event)
        else:
            super(AnimationGraphicsScene, self).mousePressEvent(event)
