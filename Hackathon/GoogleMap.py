from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from DragBox import Draggable

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

    def passSize(self, x, y, width=100, height=100):
        self.width = width
        self.height = height
        self.setGeometry(x, y, self.width, self.height)

    def loadPage(self):
        with open('../Resources/Html/GoogleMap.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

class DraggableMap(GoogleMap, Draggable):
    def __init__(self, *args, x=0, y=0, width=350, height=250):
        super().__init__(*args)
        Draggable.passSize(self, x, y, width, height)
        GoogleMap.passSize(self, x, y, width, height)

        self.setStyleSheet("""background-color: #FFFFFF""")
        self.setWindowTitle('Draggy Map')