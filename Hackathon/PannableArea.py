from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap


class PannableArea(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)
        # self.setStyleSheet("background: rgb(210,140,79);\nbackground: linear-gradient(0deg, rgba(210,140,79,1) 0%, rgba(250,200,134,1) 84%);")

        self.setObjectName("pannableArea")

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setMinimumRenderSize(100)

        self._view = QtWidgets.QGraphicsView(self.scene, self)
        self._view.setGeometry(self.parent().parent().frameGeometry())
        self._view.setStyleSheet("background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #FAC886 , stop: 0.84 #D28C4F);")
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
