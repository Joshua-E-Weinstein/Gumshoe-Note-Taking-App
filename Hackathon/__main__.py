import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap
from NiceButton import NiceButton
from Resources.QT_UIs.Test import Ui_MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow.show()


    sys.exit(app.exec_())

if __name__ == '__main__':

    # Runs main.
    main()