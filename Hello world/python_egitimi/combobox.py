import sys
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 200
        self.top = 150
        self.width = 500
        self.height = 500
        self.baslik = "ComboBox"

        self.arayuz()


    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        yatay = QHBoxLayout()

        self.kombobox = QComboBox()
        self.kombobox.addItem("Python    ")
        self.kombobox.addItem("C++")
        self.kombobox.addItem("C#")
        self.kombobox.addItem("Java")
        self.kombobox.addItems(["bir","iki","üç"])

        self.kombobox.currentIndexChanged.connect(self.secildi)

        yatay.addStretch()
        yatay.addWidget(self.kombobox)
        yatay.addStretch()
        self.setLayout(yatay)
        self.show()

        QTest.qWait(2000)
        self.kombobox.setCurrentIndex(2)

    def secildi(self):
        if(self.kombobox.currentText()=="Python    "):
            QMessageBox.question(self,"Uyarı","Tamam Oldu !",QMessageBox.Ok)
        else:
            QMessageBox.question(self, "Uyarı", "Hayır Bu Olmaz !", QMessageBox.Ok)

uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())
