import sys
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        mesajKutusu = QMessageBox.question(self,"Mesajımızın Başlığı","Python'ı Sevdin mi?",
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok | QMessageBox.Save, QMessageBox.Yes )
        if mesajKutusu == QMessageBox.Yes:
            print("Evet'e Tıkladın!")
        elif mesajKutusu == QMessageBox.No:
            print("Hayır'a Tıkladın!")
        elif mesajKutusu == QMessageBox.Save:
            print("Tamam kaydediyorum !")
        else:
            print("Ok'a tıkladın !")
uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())