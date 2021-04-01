from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


class Draggable(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)
        self.held = False
        self.mousePos = None

    def passSize(self, x, y, width=100, height=100):
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
            self.onDrag()

    def onDrag(self):
        pass

    def mouseReleaseEvent(self, event):
        self.held = False


class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, *args):
        super().__init__(*args)

        self.image = QFileDialog().getOpenFileName()[0]
        self.pixmap = QPixmap(self.image)
        self.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(),self.pixmap.height())
        print(self.pixmap.size())
        print(self.size())

    def passSize(self, x, y, width=100, height=100):
        self.width = self.pixmap.width()
        self.height = self.pixmap.height()

        self.setWindowTitle('Draggy Box')

    def mousePressEvent(self, event):
        self.held = True
        self.mousePos = event.localPos()  # Saves mouse click position for math

    def mouseMoveEvent(self, event):
        if self.held:
            self.setGeometry(event.windowPos().x() - self.mousePos.x(), event.windowPos().y() - self.mousePos.y(), self.width, self.height)

    def mouseReleaseEvent(self, event):
        self.held = False


class DragBox(QtWidgets.QTextEdit, Draggable):
    def __init__(self, *args, x = 0, y = 0, width = 150, height = 150):
        super().__init__(*args)
        Draggable.passSize(self, x, y, width, height)
        self.show()

        self.setStyleSheet("border: 0;\nfont: 16px 'Comic Sans MS';\nbackground-color: #fff699")
        self.setWindowTitle('Draggy Box')


class Image(DraggableLabel):
    def __init__(self, *args, x = 0, y = 0, width = 150, height = 150):
        super().__init__(*args)
        DraggableLabel.passSize(self, x, y, width, height)
        self.show()
