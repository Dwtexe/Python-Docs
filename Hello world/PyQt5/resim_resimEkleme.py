import sys
from  PyQt5 import QtWidgets,QtGui

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Yazı ve resim ekleme")

font = QtGui.QFont("Times",15)

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

pencere.setGeometry(100,100,600,600)
pencere.show()
sys.exit(uygulama.exec_())