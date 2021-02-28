from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QGraphicsItem, QLabel
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor, QWindow
from PyQt5.QtCore import Qt, QPoint, QEvent
from DragBox import Draggable
import sys


class Twine(QLabel):

    def __init__(self, point1 = QPoint(0,0), point3 = QPoint(50,50), parent=None):
        super().__init__(parent)
        self.point1 = point1
        self.point3 = point3

        self.getPoint2()

        self.dic = {1: self.point1, 2: self.point2, 3: self.point3}  # Record the three coordinates, which are the starting point, control point and end point
        self.count = 0
        self.initUI()
        print(self.dic[1])

    def __update__(self):
        self.getPoint2()

        self.dic = {1: self.point1, 2: self.point2,
                    3: self.point3}  # Record the three coordinates, which are the starting point, control point and end point
        self.count = 0
        self.initUI()
        print(self.dic[1])


    def getPoint2(self):
        self.point2 = QPoint((self.point1.x() + self.point3.x()) // 2, (self.point1.y() + self.point3.y()) // 2 + 50)

    def initUI(self):
        self.geometry = 0, 0, 9999, 9999
        self.setGeometry(*self.geometry)
        self.setWindowTitle("Twine")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.show()


    def paintEvent(self, e):
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor("#ea2528"))
        pen.setCapStyle(Qt.RoundCap)

        qp = QPainter(self)
        qp.setPen(pen)
        qp.begin(self)
        self.drawBezierCurve(qp)  # Draw Bezier curve
        qp.end()


    def drawBezierCurve(self, qp):
        self.clear()
        path = QPainterPath()
        path.moveTo(self.dic[1])
        path.cubicTo(self.dic[1], self.dic[2], self.dic[3])  # Draw Bezier curve needs to provide three points, starting point, control point and end point
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawPath(path)

class Pin(Draggable):

    def __init__(self, x = 0, y = 0, parent=None):
        super().__init__(parent)
        Draggable.passSize(self, x, y, 32, 32)

        self.setGeometry(x, y, 32, 32)
        self.setStyleSheet('background: url(../Resources/Images/pin.png)')

    def link(self, secondPin, parent=None):
        self.linkage = secondPin
        self.linkage.pos().setX(5)
        secondPin.linkage = self

        self.twine = Twine(self.pos(), self.linkage.pos(), parent)


    def onDrag(self):
        # self.twine.point1 = self.pos()
        # self.twine.point3 = self.linkage.pos()

        # self.twine.getPoint2()
        self.twine.update()
        self.twine.paintEvent()
