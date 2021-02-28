import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsProxyWidget, QGraphicsWidget, QGraphicsObject

global view
global scaleLabel

def scaleScene(event):
    delta = 1.0015**event.angleDelta().y()
    view.scale(delta, delta)
    scaleLabel.setPlainText("scale: %.2f"%view.transform().m11())
    view.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create main widget
    w = QWidget()
    w.resize(800, 600)
    layout = QVBoxLayout()
    w.setLayout(layout)
    w.setWindowTitle('Example')
    w.show()
    # rescale view on mouse wheel, notice how when view.transform().m11() is not 1,
    # dragging the subwindow is not smooth on the first mouse move event
    w.wheelEvent = scaleScene

    # create scene and view
    scene = QGraphicsScene()
    scaleLabel = scene.addText("scale: 1")
    view = QGraphicsView(scene)
    layout.addWidget(view)
    view.show();

    # create item in which the proxy lives
    item = QGraphicsWidget()
    scene.addItem(item)
    item.setFlag(PyQt5.QtWidgets.QGraphicsItem.ItemIgnoresTransformations)
    item.setAcceptHoverEvents(True)

    # create proxy with window and dummy content
    proxy = QGraphicsProxyWidget(item, Qt.Window)
    button = QPushButton('dummy')
    proxy.setWidget(button)

    # start app
    sys.exit(app.exec_())