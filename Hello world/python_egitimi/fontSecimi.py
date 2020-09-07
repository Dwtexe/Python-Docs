import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.baslik = "Font Seçimi"

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        self.yazi = QLabel("Hoşgeldiniz !",self)
        self.yazi.move(50,50)
        self.yazi.resize(300,300)

        buton = QPushButton("Üstteki Yazının Fontunu Değiştir",self)
        buton.move(50,250)
        buton.clicked.connect(self.fontDegistir)

    def fontDegistir(self):
        font = QFontDialog.getFont()
        self.yazi.setFont(font[0])


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())
