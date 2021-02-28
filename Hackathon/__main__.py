import sys
from PyQt5 import QtWidgets, QtGui

from Hackathon.DragBox import DragBox, Image
from Hackathon.MainUi import MainUi
from Hackathon.GoogleMap import DraggableMap
from Hackathon.TwineDraw import Pin, Twine
from Hackathon.temp import Example
from Resources.QT_UIs.Test import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainUi()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    icon = QtGui.QIcon('../Resources/Images/icon.png')
    MainWindow.setWindowIcon(icon)


    MainWindow.setWindowTitle("Gumshoe")

    ui.stickyNoteButton.clicked.connect(lambda: DragBox(ui.centralwidget, x = 200, y = 200))
    ui.mapButton.clicked.connect(lambda: DraggableMap(ui.centralwidget, x = 200, y = 200))
    ui.imageButton.clicked.connect(lambda: Pin(300,300, parent=ui.centralwidget).link(Pin(400,350, parent=ui.centralwidget), parent=ui.centralwidget))
    ui.pinButton.clicked.connect(lambda: Image(ui.centralwidget))

    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    # Runs main.
    main()