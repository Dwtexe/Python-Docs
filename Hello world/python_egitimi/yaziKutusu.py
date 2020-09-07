import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

font = QFont("Arial",20)

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Yazı Kutusu"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 400

        self.icerik()
        self.show()

    def icerik(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #Yazı Kutusunu Oluşturalım
        self.yazikutusu = QLineEdit(self)
        self.yazikutusu.move(30,30)
        self.yazikutusu.resize(280, 40)
        self.yazikutusu.setFont(font)

        self.yazikutusu.textChanged.connect(self.yazidegisti)
        self.yazikutusu.editingFinished.connect(self.bitti)
        self.yazikutusu.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        dugme = QPushButton("Yazıyı Göster",self)
        dugme.move(30,80)
        dugme.setFont(font)

        dugme.clicked.connect(self.yaziyiGoster)

    def yaziyiGoster(self):
        print("ok")
        yazi = self.yazikutusu.text()

        mesajKutusu = QMessageBox.question(self, "Mesaj Başlığı", "Sen şunu yazdın: "+yazi, QMessageBox.Ok)
        self.yazikutusu.setText("")

    def yazidegisti(self):
        print("Yazı üzerinde değişiklik yapıldı")

    def bitti(self):
        print("Yazma bitti!")

uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())