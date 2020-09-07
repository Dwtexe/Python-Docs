import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

font = QFont("Century Gothic",12)

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 250
        self.top = 100
        self.width = 300
        self.height = 300

        self.arayuz()
        self.show()

    def arayuz(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        dikey = QVBoxLayout()

        self.yazi = QLabel("Merhaba Dünya !")
        self.yazi.setAlignment(Qt.AlignHCenter)
        self.yazi.setFont(font)

        self.kaydirac = QSlider(Qt.Horizontal)
        self.kaydirac.setMinimum(10)
        self.kaydirac.setMaximum(100)
        self.kaydirac.setValue(30)
        self.kaydirac.setTickPosition(QSlider.TicksBelow)
        self.kaydirac.setTickInterval(5)

        self.kaydirac.valueChanged.connect(self.degerDegisti)
        self.kaydirac.sliderPressed.connect(self.dokundu)
        self.kaydirac.sliderMoved.connect(self.hareketEtti)
        self.kaydirac.sliderReleased.connect(self.birakti)

        self.aciklama = QLabel("Yazının boyutunu kaydıraçla değiştirebilirsin !")
        self.aciklama.setAlignment(Qt.AlignHCenter)

        dikey.addWidget(self.yazi)
        dikey.addWidget(self.kaydirac)
        dikey.addWidget(self.aciklama)
        dikey.setAlignment(Qt.AlignVCenter)

        self.setLayout(dikey)

    def degerDegisti(self):
        boyut = self.kaydirac.value()
        font = QFont("Century Gothic",boyut)
        self.yazi.setFont(font)

    def dokundu(self):
        self.aciklama.setText("Evet işte böyle, hadi hareket ettir!")
    def hareketEtti(self):
        self.aciklama.setText("Güzel gidiyorsun, devam !")
    def birakti(self):
        self.aciklama.setText("Tamam şimdilik yeterli, sonra devam edersin..")

uygulama = QApplication(sys.argv)
Pencere = pencere()
sys.exit(uygulama.exec_())