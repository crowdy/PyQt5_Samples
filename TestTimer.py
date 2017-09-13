import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestTimer(QWidget):

    def __init__(self, parent=None):

        super(TestTimer, self).__init__(parent)
        self.setWindowTitle('Digital Clock')
        timer = QTimer(self)

        timer.timeout.connect(self.updtTime)
        self.testTimeDisplay = QLCDNumber(self)
        self.testTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.testTimeDisplay.setDigitCount(8)
        self.testTimeDisplay.resize(500, 150)
        self.updtTime()
        timer.start(1000)

    def updtTime(self):

        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.testTimeDisplay.display(currentTime)

if __name__ == '__main__':

    myApp = QApplication(sys.argv)
    myWindow = TestTimer()
    myWindow.show()
    myApp.exec_()
    sys.exit()