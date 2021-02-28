import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.DragBox import Draggable, DragBox
from Hackathon.MainUi import MainUi
from Hackathon.PannableArea import PannableArea
from Hackathon.GoogleMap import GoogleMap
from Hackathon.Test import Example
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
    googleMap = pannableArea.scene.addWidget(GoogleMap())
    googleMap1 = pannableArea.scene.addWidget(GoogleMap())
    googleMap.moveBy(100,100)

    # Draggable thing.
    pannableArea.scene.addWidget(DragBox())

    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    # Runs main.
    main()