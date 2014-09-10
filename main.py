from PyQt4.QtCore import *
from PyQt4.QtGui import *
from lib.ui.bone import *
from lib.ui.animation_scene import AnimationGraphicsScene

class AnimationGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(QGraphicsView, self).__init__(scene, parent)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

    def wheelEvent(self, event):
        factor = 1.41 ** (event.delta() / 240.0)
        self.scale(factor, factor)
        event.accept()

class MainForm(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        quitButton = QPushButton("Quit")

        scene = AnimationGraphicsScene()
        scene.initUI(-300, -300, 600, 600)

        view = AnimationGraphicsView(scene)
        view.setCacheMode(QGraphicsView.CacheBackground)
        view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
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
