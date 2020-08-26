import sys
from PyQt5 import QtWidgets,QtTest

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.yazi = QtWidgets.QLabel("Hoşgeldiniz")
        self.button1 = QtWidgets.QPushButton("Giriş")
        self.button2 = QtWidgets.QPushButton("Çıkış")

        self.button1.clicked.connect(self.giris)
        self.button2.clicked.connect(self.cikis)

        dikey = QtWidgets.QVBoxLayout()
        yatay = QtWidgets.QHBoxLayout()


        yatay.addStretch()
        dikey.addStretch()
        dikey.addWidget(self.yazi)
        dikey.addWidget(self.button1)
        dikey.addWidget(self.button2)
        dikey.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()



        self.setLayout(yatay)
        self.setGeometry(150,150,400,400)
        self.show()

    def giris(self):
        self.yazi.setText("Program Açılıyor. Lütfen bekleyin...")
        QtTest.QTest.qWait(2000)
        self.yazi.setText("Açıldı !!")
    def cikis(self):
        self.yazi.setText("Programdan Çıkılıyor. Lütfen bekleyin...")
        QtTest.QTest.qWait(2000)
        self.close()

uygulama = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(uygulama.exec_())