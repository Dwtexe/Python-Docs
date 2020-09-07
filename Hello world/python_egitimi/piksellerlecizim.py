import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.baslik = "Çizim ve Boyama"

        self.setAutoFillBackground(True)
        renkPaleti = self.palette()
        renkPaleti.setColor(self.backgroundRole(),Qt.yellow)
        self.setPalette(renkPaleti)

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        self.cizim = Boyama(self)
        self.cizim.resize(self.width,self.height)

class Boyama(QWidget):
    def paintEvent(self,event):
        qp = QPainter(self)
        qp.setPen(Qt.black)

        qp.drawPoint(10,10)

        boyut = self.size()

        for i in range(500):
            x = random.randint(1,boyut.width())
            y = random.randint(1,boyut.height())
            qp.drawPoint(x,y)


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())