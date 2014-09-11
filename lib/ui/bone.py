from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ..data.bone import Bone

class GraphicItemBone(QGraphicsItem):
    """Bone graphic item"""

    def __init__(self, parent = None, scene = None):
        super(GraphicItemBone, self).__init__(parent, scene)

        self.__polygon = QPolygon([QPoint(-1, 0), QPoint(1, 0), QPoint(0, 3)])
        self.__axisLen = 5

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsFocusable)

        self.__isShowBoundingRect = False
        self.__isShowAxis = True

        self.__data = Bone()
    
    def shape(self):
        path = QPainterPath()
        path.addPolygon(QPolygonF(self.__polygon))
        return path

    def boundingRect(self):
        region = QRegion()
        region += QRegion(QRect(QPoint(0, 0), QPoint(self.__axisLen, self.__axisLen)))
        region += QRegion(self.__polygon)
        return QRectF(region.boundingRect())

    def paint(self, painter, option, widget = None):
        # draw bone polygon
        painter.setPen(QPen(QColor(0, 255, 0)))
        painter.setBrush(QBrush(QColor(0, 128, 0, 128)))
        painter.drawPolygon(self.__polygon)

        # draw local coordinate
        if self.__isShowAxis:
            painter.setPen(QColor(0, 255, 0))
            painter.drawLine(0, 0, self.__axisLen, 0)
            painter.setPen(QColor(255, 0, 0))
            painter.drawLine(0, 0, 0, self.__axisLen)

        # draw bounding rect
        if self.__isShowBoundingRect:
            painter.setPen(QPen(QColor(0, 0, 0, 100)))
            painter.setBrush(QBrush(QColor(0, 0, 255, 100)))
            painter.drawRect(self.boundingRect())
