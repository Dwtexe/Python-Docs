import sys
from PyQt5 import QtWidgets,QtGui


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        dikey = QtWidgets.QVBoxLayout()

        font = QtGui.QFont("Century Gothic", 16)

        self.yazi = QtWidgets.QLabel("Resim Görüntüleyici")
        self.yazi.setFont(font)
        self.gozat = QtWidgets.QPushButton("Gözat...")
        self.kapat = QtWidgets.QPushButton("Kapat")
        self.resim = QtWidgets.QLabel()
        self.gozat.clicked.connect(self.resimac)
        self.kapat.clicked.connect(self.resmiKapat)

        dikey.addWidget(self.yazi)
        dikey.addStretch()
        dikey.addWidget(self.resim)
        dikey.addStretch()
        dikey.addWidget(self.gozat)
        dikey.addWidget(self.kapat)

        self.setLayout(dikey)
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Resim Görüntüleyici v1")
        self.show()
        self.kapat.close()

    def resimac(self):
        resimUrl = QtWidgets.QFileDialog.getOpenFileName(self,"Lütfen bir resim seçiniz")
        self.resim.setPixmap(QtGui.QPixmap(resimUrl[0]))
        self.kapat.show()

    def resmiKapat(self):
        self.resim.setPixmap(QtGui.QPixmap(""))
        self.kapat.close()


uygulama = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())