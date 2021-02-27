from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtCore import Qt, QPoint
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.point1 = QPoint()
        self.point2 = QPoint()
        self.point3 = QPoint()
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


    def mousePressEvent(self, event):  # Rewrite mouse press event
        if event.button() == Qt.LeftButton:
            self.count += 1
            self.dic[self.count] = event.pos()  # Get the coordinates of the current click

        if self.count == 3:
            self.count = 0
            self.update()  # Update function for triggering drawing events

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())