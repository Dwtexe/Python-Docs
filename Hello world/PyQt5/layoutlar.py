import sys
from  PyQt5 import QtWidgets,QtGui

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Horizontal ve Vertical Box Layout")

yatay = QtWidgets.QHBoxLayout()
dikey = QtWidgets.QVBoxLayout()

button1 = QtWidgets.QPushButton("Giriş")
button2 = QtWidgets.QPushButton("Çıkış")

yatay.addStretch()
yatay.addWidget(button1)
yatay.addWidget(button2)

dikey.addStretch()
dikey.addLayout(yatay)


"""
yatay = QtWidgets.QHBoxLayout()

button1 = QtWidgets.QPushButton("Giriş")
button2 = QtWidgets.QPushButton("Çıkış")

yatay.addStretch()
yatay.addWidget(button1)
yatay.addStretch()
yatay.addWidget(button2)
yatay.addStretch()


dikey = QtWidgets.QVBoxLayout()

button1 = QtWidgets.QPushButton("Giriş")
button2 = QtWidgets.QPushButton("Çıkış")

dikey.addStretch()
dikey.addWidget(button1)
dikey.addStretch()
dikey.addWidget(button2)
dikey.addStretch()

pencere.setLayout(dikey)
"""

pencere.setLayout(dikey)
pencere.setGeometry(100,100,600,600)
pencere.show()
sys.exit(uygulama.exec_())