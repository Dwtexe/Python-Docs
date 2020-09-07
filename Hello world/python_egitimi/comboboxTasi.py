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
        self.baslik = "ComboBox'a Veri Taşıyalım"

        self.arayuz()
        self.show()


    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.baslik)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        self.yazi = QLabel("Listedekileri beğenmediyseniz kendiniz de ekleyebilirsiniz. Sadece tutup taşıyın !")
        yaziKutusu = QLineEdit()
        yaziKutusu.setDragEnabled(True)

        Kombo = kombo()

        dikey.addWidget(self.yazi)
        yatay.addWidget(yaziKutusu)
        yatay.addWidget(Kombo)

        yatay.addStretch()
        dikey.addLayout(yatay)
        dikey.addStretch()
        self.setLayout(dikey)

class kombo(QComboBox):

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)


    def dragEnterEvent(self,e):
        if (e.mimeData().hasText()):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self,e):
        self.addItem(e.mimeData().text())
        Pencere.yazi.setText(e.mimeData().text()+" başarıyla eklendi !")


uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())
