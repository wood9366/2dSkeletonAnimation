from PyQt4.QtCore import Qt
from PyQt4.QtGui import QGraphicsScene, QBrush, QPen, QColor, QVector2D, QAction, QActionGroup, QPixmap
from ui.bone import GraphicItemBone
import math

class AnimationGraphicsScene(QGraphicsScene):
    Select, Move, Rotate, Link = range(4)

    def __init__(self, parent = None):
        super(QGraphicsScene, self).__init__(parent)

        self.__project = None

        self.__bones = []
        self.__adjustMode = self.Select

        self.__linkFrom = None

        self.__actionModeSelect = QAction("Select", self, checkable = True)
        self.__actionModeMove = QAction("Move", self, checkable = True)
        self.__actionModeRotate = QAction("Rotate", self, checkable = True)
        self.__actionModeLink = QAction("Link", self, checkable = True)
        self.__actions = [self.__actionModeSelect, self.__actionModeMove, self.__actionModeRotate, self.__actionModeLink]

        self.__actionGroupMode = QActionGroup(self)
        self.__actionGroupMode.addAction(self.__actionModeSelect)
        self.__actionGroupMode.addAction(self.__actionModeMove)
        self.__actionGroupMode.addAction(self.__actionModeRotate)
        self.__actionGroupMode.addAction(self.__actionModeLink)
        self.__actionGroupMode.triggered[QAction].connect(self.__changeSceneMode)

        self.__actionModeSelect.setChecked(True)

    def laod(self, project):
        self.__project = project

    def actions(self):
        return self.__actions

    @property
    def adjustMode(self):
        return self.__adjustMode

    @adjustMode.setter
    def adjustMode(self, mode):
        if self.__adjustMode != mode:
            self.__adjustMode = mode

            if self.__adjustMode == self.Link:
                self.__linkFrom = self.__linkTo = None

            self.__actions[self.adjustMode].setChecked(True)

    def initUI(self, x, y, w, h):
        self.setSceneRect(x, y, w, h)

        # coordinate
        rect = self.sceneRect()

        self.addLine(rect.left(), 0, rect.right(), 0, QPen(QColor(0, 0, 0)))
        self.addLine(0, rect.top(), 0, rect.bottom(), QPen(QColor(0, 0, 0)))

    def __changeSceneMode(self, action):
        if action == self.__actionModeLink:
            self.adjustMode = self.Link
        elif action == self.__actionModeMove:
            self.adjustMode = self.Move
        elif action == self.__actionModeRotate:
            self.adjustMode = self.Rotate
        else:
            self.adjustMode = self.Select

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
        else:
            self.adjustMode = self.Select

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
                    self.__linkFrom = self.__linkTo = None
                    # self.adjustMode = self.Select
            else:
                super(AnimationGraphicsScene, self).mousePressEvent(event)
        else:
            super(AnimationGraphicsScene, self).mousePressEvent(event)
