from PySide6 import QtCore, QtWidgets, QtGui


class NiceButton(QtWidgets.QPushButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
