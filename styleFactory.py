from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class winStyle_test(QWidget):
    def __init__(self, parent=None):
        super(winStyle_test, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        horizontalLayout = QHBoxLayout()

        self.styleLabel = QLabel("Window Style:")
        self.styleComboBox = QComboBox()

        # QStyleFactoryからリストセット
        self.styleComboBox.addItems(QStyleFactory.keys())
        print(QStyleFactory.keys())

        # カレントのstyleを検索
        index = self.styleComboBox.findText(qApp.style().objectName(), Qt.MatchFixedString)

        # styleをセット
        self.styleComboBox.setCurrentIndex(index)

        # styleがchangeしたら
        self.styleComboBox.activated[str].connect(self.windStyleChanged)

        # windowのpalette
        self.useStylePaletteCheckBox = QCheckBox("&style standard palette")
        self.useStylePaletteCheckBox.setChecked(True)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)

        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        horizontalLayout.addWidget(self.useStylePaletteCheckBox)
        self.setLayout(horizontalLayout)

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)


    def windStyleChanged(self, style):
        qApp.setStyle(style)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = winStyle_test()
    QApplication.setPalette(QApplication.style().standardPalette())
    w.show()
    sys.exit(app.exec_())