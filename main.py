from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QImage, QPen, QColor, QBrush)

class AnimationGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(QGraphicsScene, self).__init__(parent)

    def initUI(self, x, y, w, h):
        self.setBackgroundBrush(QBrush(QColor(0, 0, 0), Qt.Dense7Pattern));

        self.setSceneRect(x, y, w, h)

        rect = self.sceneRect()

        self.addLine(rect.left(), 0, rect.right(), 0, QPen(QColor(0, 0, 0)));
        self.addLine(0, rect.top(), 0, rect.bottom(), QPen(QColor(0, 0, 0)));


class AnimationGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(QGraphicsView, self).__init__(scene, parent)

class MainForm(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        quitButton = QPushButton("Quit")

        scene = AnimationGraphicsScene()
        scene.initUI(-300, -300, 600, 600)

        view = AnimationGraphicsView(scene)
        view.setCacheMode(QGraphicsView.CacheBackground)
        view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        view.setDragMode(QGraphicsView.ScrollHandDrag)
        view.setWindowTitle("Skeleton View")

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(view)
        mainLayout.addWidget(quitButton)

        self.setLayout(mainLayout)
        self.setWindowTitle("2d Skeleton Animation")
        self.resize(300, 300)

if __name__ == '__main__':
	import sys
	
	app = QApplication(sys.argv)
	
	screen = MainForm()
	screen.show()
	
	sys.exit(app.exec_())
