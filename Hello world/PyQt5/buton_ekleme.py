import sys
from  PyQt5 import QtWidgets,QtGui

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Yazı ve resim ekleme")

font = QtGui.QFont("Times",15)
buttonfont = QtGui.QFont("Century Gothic",10)

yazi1 = QtWidgets.QLabel(pencere)
yazi1.setText("PyQt5 Öğreniyorum")
yazi1.move(200,100)
yazi1.setFont(font)

resim1 = QtWidgets.QLabel(pencere)
resim1.setPixmap(QtGui.QPixmap("resim.png"))
resim1.move(100,150)

yazi2 = QtWidgets.QLabel(pencere)
yazi2.setText("dwt.exe")
yazi2.move(250,500)
yazi2.setFont(font)

button = QtWidgets.QPushButton(pencere)
button.setText("Programa Giriş")
button.move(150,550)
button.setFont(buttonfont)

button2 = QtWidgets.QPushButton(pencere)
button2.setText("Çıkış")
button2.move(300,550)
button2.setFont(buttonfont)

pencere.setGeometry(100,100,600,600)
pencere.show()
sys.exit(uygulama.exec_())