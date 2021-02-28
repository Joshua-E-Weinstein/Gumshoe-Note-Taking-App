from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap


class PannableArea(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)

        self.setObjectName("pannableArea")

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setMinimumRenderSize(100)

        self._view = QtWidgets.QGraphicsView(self.scene, self)

        self._view.setGeometry(self.parent().parent().frameGeometry())
        self.lower()

        self._zoom = 1

    def wheelEvent(self, event):
        degrees = event.angleDelta().y()

        if degrees > 0:
            if self._zoom <= 1.5:
                self._zoom *= 1.05
        elif self._zoom >= 0.65:
            self._zoom /= 1.05

        self.updateView()

    def updateView(self):
        self._view.setTransform(QtGui.QTransform().scale(self._zoom, self._zoom))

    def updateSize(self):
        geometry = self.parent().parent().geometry()
        geometry.setX(0)
        geometry.setY(0)
        print(geometry)
        self.setGeometry(geometry)
        self._view.setGeometry(geometry)

    def zoom(self):
        return self._zoom
