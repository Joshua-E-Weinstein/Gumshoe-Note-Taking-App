from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class GoogleMap(QtWidgets.QFrame):
    def __init__(self, *args):
        super().__init__(*args)

        # Style Sheet
        # self.setStyleSheet("""QWidget {
        # border: 20px solid black;
        # border-radius:10px;
        # background-color: rgb(255,255,255);
        # }""")


        verticalBox = QtWidgets.QVBoxLayout(self)

        self.webEngineView = QtWebEngineWidgets.QWebEngineView()
        self.loadPage()

        verticalBox.addWidget(self.webEngineView)

        self.setLayout(verticalBox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QWebEngineView')

    def loadPage(self):
        with open('../Resources/Html/GoogleMap.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

