import sys 
from PyQt5 import QtWidgets

def tikla():
    print('butona tiklanfi')

def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle('tikla')

    btn=QtWidgets.QPushButton(pencere,text='tikla')
    btn.clicked.connect(tikla)

    btn.move(190,89)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()