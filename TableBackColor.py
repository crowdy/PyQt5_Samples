import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.setCentralWidget(self.table)
        data1 = [['行A','行B','行C','行D'],['行A','行B','行C','行D']]
        colcnt = len(data1[0])
        rowcnt = len(data1)


        self.table.setRowCount(4)

        for n in range(rowcnt):
            for m in range(colcnt):
                item1 = QTableWidgetItem(str(data1[n][m]))
                if n == 1:
                    item1.setBackground(QColor(Qt.yellow))
                self.table.setItem(n, m, item1)
        self.table.item(1, 0).setBackground(QColor(100, 10, 125))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())