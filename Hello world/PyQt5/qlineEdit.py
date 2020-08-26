import sys
from PyQt5 import QtWidgets,QtTest

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.yazi = QtWidgets.QLabel("")
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("Onay kodunuzu giriniz: ")
        self.dugme1 = QtWidgets.QPushButton("Programa Giriş")
        self.dugme2 = QtWidgets.QPushButton("Programdan Çıkış")

        self.dugme1.clicked.connect(self.giris)
        self.dugme2.clicked.connect(self.cikis)

        dikey = QtWidgets.QVBoxLayout()

        dikey.addStretch()
        dikey.addWidget(self.yazi)
        dikey.addWidget(self.input)
        dikey.addWidget(self.dugme1)
        dikey.addWidget(self.dugme2)
        dikey.addStretch()

        self.setLayout(dikey)
        self.setGeometry(150,150,400,400)
        self.show()

    def giris(self):
        isim = self.input.text()
        if isim == "Selamican":
            self.yazi.setText("Hoşgeldin")
        else:
            self.yazi.setText("Yanlış kod")


    def cikis(self):
        self.yazi.setText("Programdan Çıkılıyor. Lütfen bekleyin...")
        QtTest.QTest.qWait(2000)
        self.close()
        self.dugme1.close()


uygulama = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(uygulama.exec_())

