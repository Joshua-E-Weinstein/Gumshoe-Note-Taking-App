import sys
from PyQt5 import QtWidgets, QtGui

from Hackathon.DragBox import DragBox
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

    MainWindow.setWindowIcon(QtGui.QIcon('../Resources/Images/icon.png'))
    MainWindow.setWindowTitle("Gumshoe")

    # The container for movable widgets.
    pannableArea = ui.centralwidget

    # Google Map.
    googleMap = DraggableMap(ui.centralwidget)


    # Draggable thing.
    proxy = DragBox(ui.centralwidget)

    pin1 = Pin(300,300, parent=ui.centralwidget)
    pin2 = Pin(400,350, parent=ui.centralwidget)
    pin1.link(pin2, parent=ui.centralwidget)

    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    # Runs main.
    main()