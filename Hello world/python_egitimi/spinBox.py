import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *

font = QFont("Century Gothic",20)

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 250
        self.top = 100
        self.width = 300
        self.height = 300

        self.arayuz()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.spinn = QSpinBox(self)
        self.spinn.move(50,50)

        self.spinn.valueChanged.connect(self.degerDegisti)

        self.spinn.setMinimum(10)
        self.spinn.setMaximum(100)
        self.spinn.setRange(30,70)
        self.spinn.setSingleStep(5)

        self.spinn.setSuffix(" TL")
        self.spinn.setPrefix("$ ")

        self.spinn.setFont(font)

        self.show()

        QTest.qWait(3000)
        self.spinn.setValue(50)

    def degerDegisti(self):
        print(self.spinn.value())


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())