import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setScene(QtWidgets.QGraphicsScene())
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(0x00, 0x09, 0x4B)))

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


class HandleGraphicsItem(QtWidgets.QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()
        self.setRect(-5, -5, 10, 10)

    def mousePressEvent(self, event):
        print("MousePressed")
        return super().mousePressEvent(event)


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.view = GraphicsView()

        self.setCentralWidget(self.view)

        self.view.setSceneRect(0, 0, 800, 600)

        item = self.view.scene().addEllipse(QtCore.QRectF(100, 100, 150, 100))

        # item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        brect = self.view.scene().addRect(item.boundingRect())
        brect.setPen(QtGui.QPen(QtGui.QColor(0x00, 0xFF, 0x00)))

        # item.setPen(QtGui.QPen(QtCore.Qt.PenStyle.NoPen))
        # item.setBrush(QtGui.QColor(0xFF, 0x00, 0x00))

        handle = HandleGraphicsItem()
        handle.moveBy(100, 100)

        self.view.scene().addItem(handle)

        handle.setPen(QtGui.QPen(QtCore.Qt.PenStyle.NoPen))
        handle.setBrush(QtGui.QColor(0xFF, 0x00, 0x00))

        brect.setParentItem(item)
        # handle.setParentItem(item)


def main():
    app = QtWidgets.QApplication(sys.argv)

    app.setApplicationName("Application")

    main_widget = MainWidget()
    main_widget.setWindowTitle(app.applicationName())
    main_widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
