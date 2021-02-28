import typing

from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.PannableArea import PannableArea

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.findChild(PannableArea, "pannableArea").updateSize()
