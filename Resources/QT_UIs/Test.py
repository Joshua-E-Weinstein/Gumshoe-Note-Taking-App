# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/QT_UIs/Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 128, 32))
        self.frame.setStyleSheet("background-color: rgb(255,255,255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stickyNoteButton = QtWidgets.QPushButton(self.frame)
        self.stickyNoteButton.setGeometry(QtCore.QRect(0, 0, 32, 32))
        self.stickyNoteButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resources/Images/SmolNote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stickyNoteButton.setIcon(icon)
        self.stickyNoteButton.setIconSize(QtCore.QSize(30, 30))
        self.stickyNoteButton.setObjectName("stickyNoteButton")
        self.pinButton = QtWidgets.QPushButton(self.frame)
        self.pinButton.setGeometry(QtCore.QRect(32, 0, 32, 32))
        self.pinButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resources/Images/SmolImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pinButton.setIcon(icon1)
        self.pinButton.setIconSize(QtCore.QSize(30, 30))
        self.pinButton.setObjectName("pinButton")
        self.mapButton = QtWidgets.QPushButton(self.frame)
        self.mapButton.setGeometry(QtCore.QRect(64, 0, 32, 32))
        self.mapButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Resources/Images/MapSmol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mapButton.setIcon(icon2)
        self.mapButton.setIconSize(QtCore.QSize(30, 30))
        self.mapButton.setObjectName("mapButton")
        self.imageButton = QtWidgets.QPushButton(self.frame)
        self.imageButton.setGeometry(QtCore.QRect(96, 0, 32, 32))
        self.imageButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Resources/Images/TackSmol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageButton.setIcon(icon3)
        self.imageButton.setIconSize(QtCore.QSize(30, 30))
        self.imageButton.setObjectName("imageButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionwhy = QtWidgets.QAction(MainWindow)
        self.actionwhy.setObjectName("actionwhy")
        self.actiongo_away = QtWidgets.QAction(MainWindow)
        self.actiongo_away.setObjectName("actiongo_away")
        self.actionno_files = QtWidgets.QAction(MainWindow)
        self.actionno_files.setObjectName("actionno_files")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionnow = QtWidgets.QAction(MainWindow)
        self.actionnow.setObjectName("actionnow")
        self.actionfile_save = QtWidgets.QAction(MainWindow)
        self.actionfile_save.setObjectName("actionfile_save")
        self.actionfile_open = QtWidgets.QAction(MainWindow)
        self.actionfile_open.setObjectName("actionfile_open")
        self.actionfile = QtWidgets.QAction(MainWindow)
        self.actionfile.setObjectName("actionfile")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionwhy.setText(_translate("MainWindow", "Open"))
        self.actiongo_away.setText(_translate("MainWindow", "go away"))
        self.actionno_files.setText(_translate("MainWindow", "no files"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionnow.setText(_translate("MainWindow", "now"))
        self.actionfile_save.setText(_translate("MainWindow", "file save"))
        self.actionfile_open.setText(_translate("MainWindow", "file open"))
        self.actionfile.setText(_translate("MainWindow", "file?"))
