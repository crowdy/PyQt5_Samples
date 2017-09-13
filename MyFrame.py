from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyFrame(QGraphicsView):
    def __init__( self, parent = None ):
        super(MyFrame, self).__init__(parent)

        #シーン作成
        self.scene = QGraphicsScene(self)

        #シーンをセット
        self.scene.setSceneRect(0, 0, 500, 500)
        self.setScene(self.scene)

        #pen = QPen(QColor(Qt.green))

        #ブラシ（Brush）をセット
        brush = QBrush(Qt.red, Qt.CrossPattern)

        #楕円作成
        item = self.scene.addEllipse(30, 30, 50, 50, Qt.red, brush)
        #矩形作成
        item2 = self.scene.addRect(70, 70, 50, 50, Qt.green, QBrush(Qt.green, Qt.CrossPattern))

        #選択と移動を可能にする
        item.setFlag(QGraphicsItem.ItemIsSelectable)
        item.setFlag(QGraphicsItem.ItemIsMovable)

        #移動を可能にする
        item2.setFlag(QGraphicsItem.ItemIsMovable)

if ( __name__ == '__main__' ):
    app = QApplication([])
    f = MyFrame()
    f.show()
    app.exec_()