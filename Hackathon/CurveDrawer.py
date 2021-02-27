from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtCore import Qt, QPoint
import sys


class Bezier(QWidget):

    def __init__(self, point1 = QPoint(200, 100), point2 = QPoint(350, 200), point3 = QPoint(500, 100)):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.dic = {1: self.point1, 2: self.point2, 3: self.point3}  # Record the three coordinates, which are the starting point, control point and end point
        self.count = 0
        self.initUI()
        print(self.dic[1])

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
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
        path = QPainterPath()
        path.moveTo(self.dic[1])
        path.cubicTo(self.dic[1], self.dic[2], self.dic[3])  # Draw Bezier curve needs to provide three points, starting point, control point and end point
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawPath(path)
