import typing

from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.PannableArea import PannableArea

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 300)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.findChild(PannableArea, "pannableArea").updateSize()
