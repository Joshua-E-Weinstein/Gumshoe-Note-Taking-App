from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap


class PannableArea(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setMinimumRenderSize(100)

        self._view = QtWidgets.QGraphicsView(self.scene, self)

        self.setGeometry(self.parent().parent().frameGeometry())
        self.lower()

        self._zoom = 1

    def wheelEvent(self, event):
        degrees = event.angleDelta().y()
        print(self.size())

        if degrees > 0:
            self._zoom *= 1.05
        else:
            self._zoom /= 1.05

        print(self._zoom)
        self.updateView()

    def updateView(self):
        self._view.setTransform(QtGui.QTransform().scale(self._zoom, self._zoom))