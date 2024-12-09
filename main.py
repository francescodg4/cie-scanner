import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setScene(QtWidgets.QGraphicsScene())
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(0x00, 0x09, 0x4B)))

        # place image
        self.image = QtGui.QImage("image.jpg")

        self.scene().addItem(
            QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
        )

    def wheelEvent(self, event):
        zoom_in = 1.25
        zoom_out = 1 / zoom_in

        if event.angleDelta().y() > 0:
            zoom_factor = zoom_in
        else:
            zoom_factor = zoom_out

        self.centerOn(self.mapToScene(event.pos()))
        self.scale(zoom_factor, zoom_factor)

    def mousePressEvent(self, event):
        self.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setDragMode(QtWidgets.QGraphicsView.DragMode.NoDrag)
        return super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.fitInView(self.sceneRect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        return super().mouseDoubleClickEvent(event)

    def sizeHint(self):
        return QtCore.QSize(800, 600)


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(GraphicsView())


def main():
    app = QtWidgets.QApplication(sys.argv)

    app.setApplicationName("Application")

    main_widget = MainWidget()
    main_widget.setWindowTitle(app.applicationName())
    main_widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
