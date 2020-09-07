import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.sekmeler = QTabWidget(self)
        self.sekme1 = QWidget()
        self.sekme2 = QWidget()
        self.sekmeler.setGeometry(20,20,250,250)

        self.sekmeler.addTab(self.sekme1,"Sekme 1")
        self.sekmeler.addTab(self.sekme2,"Sekme 2")

        dikey1 = QVBoxLayout(self)
        dugme1 = QPushButton("Birinci Sekmenin Butonu")
        dikey1.addWidget(dugme1)
        self.sekme1.setLayout(dikey1)

        dikey2 = QVBoxLayout(self)
        dugme2 = QPushButton("İkinci Sekmenin Butonu")
        dikey2.addWidget(dugme2)
        self.sekme2.setLayout(dikey2)



uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())