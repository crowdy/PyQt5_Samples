import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

data = [['AAA', '東京', '東'],['BBB', '渋谷', '南西'],['CCC', '新宿', '西'],['DDD', '日暮里', '北'],['EEE', '秋葉原', '北東']]
class tableTest01(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setdata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setdata(self):
        #ヘッダーを作成
        horHeaders = ['列1','列2','列3','列4','列5']
        self.setHorizontalHeaderLabels(horHeaders)
        #テーブルにデータをセット
        for n in range(len(self.data)):
            print("n=%d" % n)
            for m in range(len(self.data[n])):
                print("m=%d" % m)
                newitem = QTableWidgetItem(data[n][m])
                self.setItem(m, n, newitem)

def main():
    app = QApplication(sys.argv)
    table = tableTest01(data, 3, 5)
    table.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()