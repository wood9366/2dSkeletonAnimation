from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui.bone import *
from ui.animation_scene import AnimationGraphicsScene
import data.project    
import main_rc2

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

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.__project = None

        self.__scene = AnimationGraphicsScene()
        self.__scene.initUI(-500, -500, 1000, 1000)

        self.__scene.setBackgroundBrush(QBrush(QPixmap(':/res/cross.png')))

        self.__initActions()
        self.__initMenus()
        self.__initToolBar()

        self.__view = AnimationGraphicsView(self.__scene)
        self.__view.setCacheMode(QGraphicsView.CacheBackground)
        self.__view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.__view.setWindowTitle("Skeleton View")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.__view)

        self.__widget = QWidget()
        self.__widget.setLayout(mainLayout)
        self.setCentralWidget(self.__widget)
        self.setWindowTitle("2d Skeleton Animation")
        self.resize(500, 500)

        self.__newProject()
        
    def __initActions(self):
        self.__actionAbout = QAction("&About", self, triggered = self.__about)

    def __about(self):
        QMessageBox.about(self, "About 2d skeleton animation", "<b>2D</b> Skeleton Animation")

    def __initMenus(self):
        self.__menuHelp = self.menuBar().addMenu("&Help")
        self.__menuHelp.addAction(self.__actionAbout)

    def __initToolBar(self):
        self.__toolBarScene = self.addToolBar("Scene Tool")
        for action in self.__scene.actions():
            self.__toolBarScene.addAction(action)

    def __newProject(self):
        self.__project = data.project.Project()
        self.__initProject()

    def __saveProject(self):
        # todo, save proejct into file
        pass

    def __loadProject(self, projectFile):
        # todo, load project data from file
        self.__initProject()
        pass

    def __initProject(self):
        self.setWindowTitle(self.__project.name)
        self.__initScene()
        # todo, init bone tree

    def __initScene(self):
        # init bones graphics item
        pass

if __name__ == '__main__':
	import sys
	
	app = QApplication(sys.argv)
	
	screen = MainForm()
	screen.show()
	
	sys.exit(app.exec_())
