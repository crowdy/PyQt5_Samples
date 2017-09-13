import sys
from PyQt5.QtWidgets import *

data = [['AAA', '東京', '東'],['BBB', '渋谷', '南西'],['CCC', '新宿', '西']]

class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        colcnt = len(data[0])
        rowcnt = len(data)
        self.tablewidget = QTableWidget(rowcnt, colcnt)

        #ヘッダー設定
        horHeaders = ['列1','列2','列3']
        self.tablewidget.setHorizontalHeaderLabels(horHeaders)
        verHeaders = ['行1','行2','行3']
        self.tablewidget.setVerticalHeaderLabels(verHeaders)

        #テーブルの中身作成
        for n in range(rowcnt):
            for m in range(colcnt):
                item = QTableWidgetItem(str(data[n][m]))
                self.tablewidget.setItem(n, m, item)

        #レイアウト
        layout = QHBoxLayout()
        layout.addWidget(self.tablewidget)
        self.setLayout(layout)
        self.setWindowTitle('tableサンプル')

def main():
    app = QApplication(sys.argv)
    widget = TableWindow()
    widget.show()
    widget.raise_()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()