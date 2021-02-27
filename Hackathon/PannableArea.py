from PyQt5 import QtCore, QtGui, QtWidgets

class PannableArea(QtWidgets.QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)

        self.setGeometry(self.parent().parent().frameGeometry())
        self.lower()

        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)

    def wheelEvent(self, event):
        self.scale(0.95,0.95)

