from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ..data.bone import Bone

class GraphicItemBone(QGraphicsPolygonItem):
    # Select, Move, Rotate, Scale = range(4)

    """Bone graphic item"""

    def __init__(self, parent = None, scene = None):
        super(QGraphicsPolygonItem, self).__init__(parent, scene)

        self.setPolygon(QPolygonF([QPointF(-1, 0), QPointF(1, 0), QPointF(0, 3)]))
        self.setPen(QPen(QColor(0, 255, 0)))
        self.setBrush(QBrush(QColor(0, 128, 0, 128)))

        # self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsFocusable)

        # self.__adjustMode = self.Select
        self.__data = Bone()
    #
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_E:
    #         self.__adjustMode = self.Rotate
    #     elif event.key() == Qt.Key_W:
    #         self.__adjustMode = self.Move
    #     elif event.key() == Qt.Key_R:
    #         self.__adjustMode = self.Scale
    #     else:
    #         self.__adjustMode = self.Select
    #
    #     print "mode: %d" % (self.__adjustMode)
    #
    # def mouseMoveEvent(self, event):
    #     m = self.matrix()
    #     offset = event.pos() - event.lastPos()
    #     if self.__adjustMode == self.Move:
    #         m.translate(offset.x(), offset.y())
    #         self.setMatrix(m)
    #         event.accept()
    #     elif self.__adjustMode == self.Rotate:
    #         m.rotate(offset.x())
    #         self.setMatrix(m)
    #         event.accept()
    #     elif self.__adjustMode == self.Scale:
    #         m.scale(offset.x(), offset.y())
    #         self.setMatrix(m)
    #         event.accept()
    #     else:
    #         super(GraphicItemBone, self).mouseMoveEvent(event)
