import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

baslikFont = QFont("Century Gothic",24)
butonFont = QFont("Verdana",13)
yaziFont = QFont("Century Gothic",12)

class pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.baslik = "Not Defteri V1"

        self.arayuz()
        self.genel()

        self.setGeometry(400,100,500,500)
        self.show()

    def arayuz(self):

        anaWidget = QWidget()

        self.setWindowTitle(self.baslik)

        dikey = QVBoxLayout()

        baslik = QLabel("Not Defteri V1")
        baslik.setAlignment(Qt.AlignHCenter)
        baslik.setFont(baslikFont)

        self.sekmeler = QTabWidget()

        self.sekmeler.currentChanged.connect(self.sekmeDegisti)
        self.sekmeler.setTabsClosable(True)
        self.sekmeler.setMovable(True)
        self.sekmeler.setTabShape(1)

        self.sekmeler.tabCloseRequested.connect(self.removeTab)

        dikey.addWidget(self.sekmeler)
        anaWidget.setLayout(dikey)
        self.setCentralWidget(anaWidget)


    def removeTab(self, index):
        baslik = self.sekmeler.tabText(index)
        if (baslik[-1:] == "*"):
            mesaj = QMessageBox.question(self, "Uyarı", "Dosyada değişiklik yaptınız. Kaydedilsin mi ?",
                                         QMessageBox.Yes | QMessageBox.No)

            if (mesaj == QMessageBox.Yes):
                yazi = self.sekmeler.widget(index).findChild(QTextEdit)
                yol = self.sekmeler.widget(index).findChild(QLabel)
                url = yol.text()
                icerik = yazi.toPlainText()

                if url=="":
                    dosyaUrl = QFileDialog.getSaveFileName(self, "Lütfen kaydedilecek yeri seçiniz", "",
                                                           "Metin Belgesi (*.txt)")
                    url = dosyaUrl[0]

                with open(url,"w",encoding="utf-8") as dosya:
                    dosya.write(icerik)

                self.statusBar.showMessage("Dosya başarıyla kaydedildi ve sekme kapatıldı !",3000)

        self.sekmeler.removeTab(index)

    def sekmeDegisti(self):
        self.statusBar.clearMessage()

    def genel(self):
        self.menu = self.menuBar()
        self.dosya = self.menu.addMenu("Dosya")
        self.gorunum = self.menu.addMenu("Görünüm")

        dosyaAc = QAction("Aç",self)
        dosyaAc.setShortcut("Ctrl+O")
        dosyaAc.triggered.connect(self.ac)
        self.dosya.addAction(dosyaAc)

        yeniDosya = QAction("Yeni Dosya",self)
        yeniDosya.setShortcut("Ctrl+N")
        yeniDosya.triggered.connect(self.yeniAc)
        self.dosya.addAction(yeniDosya)

        yaziTipi = QAction("Yazı Tipi",self)
        yaziTipi.setShortcut("Ctrl+F")
        yaziTipi.triggered.connect(self.yaziTipi)
        self.gorunum.addAction(yaziTipi)

        renk = QAction("Renkler",self)
        renk.setShortcut("Ctrl+R")
        renk.triggered.connect(self.renkler)
        self.gorunum.addAction(renk)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def ac(self):
        dosyaUrl = QFileDialog.getOpenFileName(self,"Lütfen bir metin belgesi seçiniz","","Metin Belgesi (*.txt)")
        isim = dosyaUrl[0].split("/")[-1:][0]

        Not(isim, dosyaUrl[0])

        sekmeSayisi = self.sekmeler.count()
        self.sekmeler.setCurrentIndex(sekmeSayisi-1)

    def yeniAc(self):
        Not("", "")

    def yaziTipi(self):
        global yaziFont
        yaziFont = QFontDialog.getFont()[0]
        sekmeSayisi = self.sekmeler.count()
        for i in range(sekmeSayisi):
            yazimiz = self.sekmeler.widget(i).findChild(QTextEdit)
            yazimiz.setFont(yaziFont)

    def renkler(self):
        self.renkPenceresi = QWidget()
        self.renkPenceresi.setWindowTitle("Renk Ayarları")

        yatay = QHBoxLayout()

        yaziButon = QPushButton("Yazı Rengi")
        yaziButon.setFont(butonFont)
        arkaButon = QPushButton("Arkaplan Rengi")
        arkaButon.setFont(butonFont)

        yatay.addWidget(yaziButon)
        yatay.addWidget(arkaButon)

        self.renkPenceresi.setLayout(yatay)
        self.renkPenceresi.move(500,190)
        self.renkPenceresi.show()

class Not(QWidget):
    def __init__(self,baslik,yol):
        super().__init__()
        if(baslik!=""):
            self.baslik = baslik
        else:
            self.baslik = "Yeni Dosya"

        self.yol = yol

        yoll = QLabel(self)
        yoll.setText(yol)
        yoll.close()

        self.yatay = QHBoxLayout()
        self.yazi = QTextEdit()

        if(baslik!="" and yol!=""):
            with open(yol, "r+",encoding="utf-8") as dosya:
                oku = dosya.read()
                self.yazi.append(oku)

        self.yazi.setStyleSheet("background-color:yellow")
        self.yazi.textChanged.connect(self.degisiklik)
        self.yazi.setFont(yaziFont)

        self.yatay.addWidget(self.yazi)
        self.setLayout(self.yatay)

        Pencere.sekmeler.addTab(self,self.baslik)

    def degisiklik(self):
        mevcut = Pencere.sekmeler.currentIndex()
        Pencere.sekmeler.setTabText(mevcut,self.baslik+"*")

        yaziStr = self.yazi.toPlainText()

        karakter = len(yaziStr)
        kelime = len(yaziStr.split())

        Pencere.statusBar.showMessage("Karakter: " + str(karakter)+" Kelime: "+str(kelime))


uygulama = QApplication(sys.argv)
Pencere = pencere()
Pencere.yeniAc()
sys.exit(uygulama.exec_())



