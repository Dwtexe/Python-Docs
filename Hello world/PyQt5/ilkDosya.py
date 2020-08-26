import sys
from PyQt5 import QtWidgets

uygulama = QtWidgets.QApplication(sys.argv)

pencere = QtWidgets.QWidget()
pencere.setWindowTitle("Deneme")
pencere.show()

sys.exit(uygulama.exec_())