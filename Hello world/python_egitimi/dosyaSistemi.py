import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
from PyQt5.QtCore import *

font = QFont("Century Gothic",12)

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 250
        self.top = 100
        self.width = 600
        self.height = 300
        self.baslik = "Dosya Sistemi"

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.agac = QTreeView(self)
        self.agac.setModel(self.model)

        self.agac.setAnimated(True)
        self.agac.setIndentation(10)
        self.agac.setSortingEnabled(True)
        self.agac.move(30,30)
        self.agac.resize(500,200)




uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())