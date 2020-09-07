import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.arayuz()
        self.show()

    def arayuz(self):

        self.tablo = QTableWidget(self)
        self.tablo.setRowCount(4)
        self.tablo.setColumnCount(3)
        self.tablo.setGeometry(10,10,500,300)

        self.tablo.setItem(0, 0, QTableWidgetItem("Birinci"))
        self.tablo.setItem(0, 1, QTableWidgetItem("İkinci"))
        self.tablo.setItem(0, 2, QTableWidgetItem("Üçüncü"))
        self.tablo.setItem(1, 0, QTableWidgetItem("Dördüncü"))
        self.tablo.setItem(1, 1, QTableWidgetItem("Beşinci"))
        self.tablo.setItem(1, 2, QTableWidgetItem("Altıncı"))
        self.tablo.setItem(2, 0, QTableWidgetItem("Yedinci"))
        self.tablo.setItem(2, 1, QTableWidgetItem("Sekizinci"))

        self.tablo.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tablo.doubleClicked.connect(self.karisma)


    def karisma(self):
        for tiklanan in self.tablo.selectedItems():
            print(tiklanan.text(),tiklanan.row(),tiklanan.column())
        mesajKutusu = QMessageBox.question(self, "Hata", "Tablo düzenlemeye açık değil !",QMessageBox.Ok)

uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())