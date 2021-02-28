from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap


class PannableArea(QtWidgets.QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        # self.setStyleSheet("background: rgb(210,140,79);\nbackground: linear-gradient(0deg, rgba(210,140,79,1) 0%, rgba(250,200,134,1) 84%);")

        self.setObjectName("pannableArea")

        self.setGeometry(self.parent().parent().frameGeometry())
        self.setStyleSheet("background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #FAC886 , stop: 0.84 #D28C4F);")
        self.lower()

        self.originalX = 0
        self.originalY = 0
        self.moving = False

    def mousePressEvent(self, event):
        print("1")
        if event.button() == QtCore.Qt.MidButton:
            print("1.5")
            self.moving = True

    def mouseMoveEvent(self, event):
        print("2")
        if self.moving:
            print("2.5")

    def mouseReleaseEvent(self, event):
        print("3")
        if event.button() == QtCore.Qt.MidButton:
            self.moving = False

    def updateSize(self):
        geometry = self.parent().parent().geometry()
        geometry.setX(0)
        geometry.setY(0)
        print(geometry)
        self.setGeometry(geometry)
