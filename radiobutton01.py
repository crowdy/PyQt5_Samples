import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FormTest(QDialog):
    def __init__(self, parent=None):
        super(FormTest, self).__init__(parent)

        radiobutton1 = QRadioButton("一")
        radiobutton1.setCheckable(True)
        radiobutton1.setFocusPolicy(Qt.NoFocus)

        radiobutton2 = QRadioButton("二")
        radiobutton2.setCheckable(True)
        radiobutton2.setFocusPolicy(Qt.NoFocus)

        radiobutton3 = QRadioButton("三")
        radiobutton3.setCheckable(True)
        radiobutton3.setFocusPolicy(Qt.NoFocus)

        radiobutton4 = QRadioButton("四")
        radiobutton4.setCheckable(True)
        radiobutton4.setFocusPolicy(Qt.NoFocus)

        radiobutton5 = QRadioButton("五")
        radiobutton5.setCheckable(True)
        radiobutton5.setFocusPolicy(Qt.NoFocus)

        self.group = QButtonGroup()
        self.group.addButton(radiobutton1,1)
        self.group.addButton(radiobutton2,2)
        self.group.addButton(radiobutton3,3)
        self.group.addButton(radiobutton4,4)
        self.group.addButton(radiobutton5,5)

        self.label = QLabel("ラジオボタンをクリックしてください")

        layout = QHBoxLayout()

        layout.addWidget(radiobutton1)
        layout.addWidget(radiobutton2)
        layout.addWidget(radiobutton3)
        layout.addWidget(radiobutton4)
        layout.addWidget(radiobutton5)

        Vlayout = QVBoxLayout()

        Vlayout.addWidget(self.label)
        Vlayout.addLayout(layout)

        self.setLayout(Vlayout)

        radiobutton1.clicked.connect(self.clicked)
        radiobutton2.clicked.connect(self.clicked)
        radiobutton3.clicked.connect(self.clicked)
        radiobutton4.clicked.connect(self.clicked)
        radiobutton5.clicked.connect(self.clicked)

    def clicked(self):
        radiobutton = self.sender()
        if radiobutton is None or not isinstance(radiobutton,QRadioButton):
            return
        self.label.setText("あなたは '%s' のラジオボタンをチェックしました" % radiobutton.text())

app = QApplication(sys.argv)
formtest = FormTest()
formtest.show()
app.exec_()