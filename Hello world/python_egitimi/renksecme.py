import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

font = QFont("Century Gothic",20)

class pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400
        self.baslik = "Renk Seçimi"

        self.setAutoFillBackground(True)
        self.renkPaleti = self.palette()

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        arkaButon = QPushButton("Arkaplanı Boya",self)
        arkaButon.move(20,100)
        arkaButon.setFont(font)
        arkaButon.clicked.connect(self.arkayiBoya)

    def arkayiBoya(self):
        renk = QColorDialog.getColor()
        self.renkPaleti.setColor(self.backgroundRole(),renk)
        self.setPalette(self.renkPaleti)

uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())