from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QDrag

class Draggable(QtWidgets.QFrame):
    def __init__(self, *args, x = 300, y = 300):
        super().__init__(*args)

        self.held = False
        self.width = 100
        self.height = 150

        self.setStyleSheet("""background-color: #ebbf55""")
        self.setGeometry(x, y, self.width, self.height)
        self.setWindowTitle('Draggy Box')

    def mousePressEvent(self, event):
        self.held = True

    def mouseMoveEvent(self, event):
        if self.held:
            self.setGeometry(event.windowPos().x() - self.width//2, event.windowPos().y(), self.width, self.height)

    def mouseReleaseEvent(self, event):
        self.held = False

class DragBox(QtWidgets.QTextEdit, Draggable):
    def __init__(self, *args, x = 0, y = 0):
        super().__init__(*args)

        self.setStyleSheet("""background-color: #ebbf55""")
        self.setGeometry(x, y, self.width, self.height)
        self.setWindowTitle('Draggy Box')