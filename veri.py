import sys
from PyQt5 import QtWidgets
class Pence():
    def Pencere():
        app=QtWidgets.QApplication(sys.argv)
        pencere=QtWidgets.QWidget()
        pencere.setWindowTitle('')
        pencere.show()
        sys.exit(app.exec_())
a=Pence
a.Pencere()