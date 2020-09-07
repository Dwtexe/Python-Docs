import sys
from PyQt5.QtWidgets import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.baslik = "Yazıları Tutup Taşıma"

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        yazi = QLineEdit("Taşınabilecek bir yazı !!",self)
        yazi.move(50,50)
        yazi.setDragEnabled(True)

        ikinci = Tasinabilen("Buraya Taşıyabilirsin",self)
        ikinci.move(50,150)
        ikinci.resize(100,20)

class Tasinabilen(QLabel):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
            e.accept()
    def dropEvent(self,e):
        self.setText(e.mimeData().text())


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())

