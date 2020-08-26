import sys
from PyQt5 import QtWidgets,QtTest


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        dikey = QtWidgets.QVBoxLayout()

        self.yazi = QtWidgets.QLabel("")
        self.input = QtWidgets.QLineEdit()
        self.input.setPlaceholderText("Kullanıcı Adınız")
        self.input2 = QtWidgets.QLineEdit()
        self.input2.setPlaceholderText("Şifreniz")
        self.hatirla = QtWidgets.QCheckBox("Beni Hatırla")

        self.dugme = QtWidgets.QPushButton("Giriş Yap")
        self.dugme.clicked.connect(self.giris)

        dikey.addWidget(self.yazi)
        dikey.addWidget(self.input)
        dikey.addWidget(self.input2)
        dikey.addWidget(self.hatirla)
        dikey.addWidget(self.dugme)


        self.setLayout(dikey)
        self.show()

    def giris(self):
        if(self.hatirla.isChecked()):
            self.yazi.setText("Tamam seni hatırlicam!")
        else:
            self.yazi.setText("Hayır seni unutucam!")


uygulama = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())