import sys
from PyQt5.QtWidgets import *

class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()

        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzen = menubar.addMenu("Düzen")
        gorunum = menubar.addMenu("Görünüm")
        yardim = menubar.addMenu("Yardım")

        dosyaAc = QAction("Dosya Aç",self)
        dosyaAc.setShortcut("Ctrl+O")
        dosya.addAction(dosyaAc)

        yeniDosya = QAction("Yeni Dosya",self)
        yeniDosya.setShortcut("Ctrl+N")
        dosya.addAction(yeniDosya)

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(cikis)
        cikis.triggered.connect(cikisPenceresi)

        gerial = QAction("Geri Al",self)
        gerial.setShortcut("Ctrl+Z")
        duzen.addAction(gerial)

        bul = duzen.addMenu("Bul")
        bul1 = QAction("Bul",self)
        bul1.setShortcut("Ctrl+F")
        bul.addAction(bul1)
        bul2 = QAction("Değiştir",self)
        bul2.setShortcut("Ctrl+H")
        bul.addAction(bul2)

        self.show()
        self.setWindowTitle("Menü Olayları")
        self.setGeometry(200,200,400,400)

class cikisPenceresi(QDialog):
    def __init__(self):
        super().__init__()

        dikey = QVBoxLayout()
        yazi = QLabel("Programdan Çıkmak İstediğinize Emin Misiniz?")

        buton = QPushButton("Evet!")
        buton2 = QPushButton("Hayır!")

        buton.clicked.connect(self.kesinCikis)
        buton2.clicked.connect(self.hayir)

        dikey.addWidget(yazi)
        dikey.addWidget(buton)
        dikey.addWidget(buton2)

        self.setLayout(dikey)
        self.setWindowTitle("Çıkmak mı istedin?")
        self.exec_()

    def kesinCikis(self):
        qApp.quit()
    def hayir(self):
        self.close()


uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())