from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsScene, QBrush, QPen, QColor
from bone import GraphicItemBone

class AnimationGraphicsScene(QGraphicsScene):
    Select, Move, Rotate, Scale = range(4)

    def __init__(self, parent = None):
        super(QGraphicsScene, self).__init__(parent)
        self.__bones = []
        self.__adjustMode = self.Select

    def initUI(self, x, y, w, h):
        self.setBackgroundBrush(QBrush(QColor(128, 128, 128), Qt.SolidPattern))

        self.setSceneRect(x, y, w, h)

        rect = self.sceneRect()

        self.addLine(rect.left(), 0, rect.right(), 0, QPen(QColor(0, 0, 0)))
        self.addLine(0, rect.top(), 0, rect.bottom(), QPen(QColor(0, 0, 0)))

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
        elif event.key() == Qt.Key_R:
            self.__adjustMode = self.Scale
        else:
            self.__adjustMode = self.Select

        print "mode: %d" % (self.__adjustMode)

    def mouseMoveEvent(self, event):
        selectedItems = self.selectedItems()
        # offset = event.pos() - event.lastPos()
        offset = event.scenePos() - event.lastScenePos()

        print "offset: %f, %f" % (offset.x(), offset.y())

        if self.__adjustMode == self.Move:
            for item in selectedItems:
                item.translate(offset.x(), offset.y())
                # m = item.matrix()
                # m *= QMatrix().translate(offset.x(), offset.y())
                # item.setMatrix(m)
            event.accept()
        elif self.__adjustMode == self.Rotate:
            for item in selectedItems:
                item.rotate(offset.x())
                # m = item.matrix()
                # m *= QMatrix().rotate(offset.x())
                # item.setMatrix(m)
            event.accept()
        elif self.__adjustMode == self.Scale:
            for item in selectedItems:
                item.scale(1 + 1 * offset.x(), 1 + 1 * offset.y())
                # m = item.matrix()
                # m.scale(1 + 1 * offset.x(), 1 + 1 * offset.y())
                # item.setMatrix(m)
            event.accept()
        else:
            super(AnimationGraphicsScene, self).mouseMoveEvent(event)
