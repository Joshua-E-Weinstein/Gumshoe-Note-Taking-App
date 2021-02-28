import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.DragBox import Draggable, DragBox
from Hackathon.MainUi import MainUi
from Hackathon.PannableArea import PannableArea
from Hackathon.GoogleMap import GoogleMap
from Hackathon.Test import Twine
from Hackathon.TwineDraw import Pin
from NiceButton import NiceButton
from Resources.QT_UIs.Test import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainUi()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # The container for movable widgets.
    pannableArea = PannableArea(ui.centralwidget)

    # Google Map.
    googleMap = GoogleMap(pannableArea)


    # Draggable thing.
    proxy = DragBox(pannableArea)

    pin1 = Pin(300,300, parent=pannableArea)
    pin2 = Pin(400,350, parent=pannableArea)
    pin1.link(pin2)

    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    # Runs main.
    main()