import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

font = QFont("Century Gothic",14)

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 250
        self.top = 100
        self.width = 600
        self.height = 400
        self.baslik = "QTextEdit (Büyük Yazı)"

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setWindowTitle(self.baslik)

        self.buyukYazi = QTextEdit(self)
        self.buyukYazi.setAlignment(Qt.AlignHCenter)
        self.buyukYazi.setAcceptRichText(False)
        self.buyukYazi.setCursorWidth(2)

        self.buyukYazi.move(20,20)

        self.buyukYazi.textChanged.connect(self.yaziDegisti)

        self.yazi = QLabel("Yazdığınız Yazı Burada Görünecek",self)
        self.yazi.setGeometry(20,250,300,100)

    def yaziDegisti(self):
        icerik = self.buyukYazi.toPlainText()
        self.yazi.setText(icerik)




uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())