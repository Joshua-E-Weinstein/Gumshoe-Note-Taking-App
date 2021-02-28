from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.tool = 0
        self.setMinimumSize(500, 300)
        self.setStyleSheet("background-color: qlineargradient(x1: 0.5, y1: 0.5 x2: 0.5, y2: 1, stop: 0 #FAC886 , stop: 0.84 #D28C4F);")


