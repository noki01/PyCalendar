from PyQt4 import QtCore, QtGui
import sys

class MainFrame(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        layout = QtGui.QVBoxLayout(self)
        scene = QtGui.QGraphicsScene()
        view = QtGui.QGraphicsView(scene)
        view.setRenderHint(QtGui.QPainter.Antialiasing, True)
        layout.addWidget(view)
        scene.addPixmap(QtGui.QPixmap("clockFrame.png"))

app = QtGui.QApplication(sys.argv)
frame = MainFrame()
frame.show()
sys.exit(app.exec_())
