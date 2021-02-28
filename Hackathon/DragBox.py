from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QDrag


class Draggable(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)
        self.held = False
        self.mousePos = None

    def passSize(self, x, y, width = 100, height = 100):
        self.width = width
        self.height = height

        self.setGeometry(x, y, self.width, self.height)
        self.setWindowTitle('Draggy Box')

    def mousePressEvent(self, event):
        self.held = True
        self.mousePos = event.localPos()  # Saves mouse click position for math

    def mouseMoveEvent(self, event):
        if self.held:
            self.setGeometry(event.windowPos().x() - self.mousePos.x(), event.windowPos().y() - self.mousePos.y(), self.width, self.height)

    def mouseReleaseEvent(self, event):
        self.held = False

class DragBox(QtWidgets.QTextEdit):
    def __init__(self, *args, x = 0, y = 0, width = 150, height = 150):
        super().__init__(*args)
        Draggable.passSize(self, x, y, width, height)

        self.setStyleSheet("""background-color: #ebbf55""")
        self.setWindowTitle('Draggy Box')