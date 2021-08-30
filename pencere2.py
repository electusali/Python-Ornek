import sys
from PyQt5 import QtWidgets

def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    okay=QtWidgets.QPushButton('tamam')
    cancel=QtWidgets.QPushButton('iptal')
    okay1=QtWidgets.QPushButton('tamam1')
    cancel1=QtWidgets.QPushButton('iptal1')
    h_box=QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)

    h_box1=QtWidgets.QHBoxLayout()

    h_box1.addWidget(okay1)
    h_box1.addStretch()
    h_box1.addWidget(cancel1)


    v_box=QtWidgets.QVBoxLayout()
    v_box.addLayout(h_box)
    v_box.addStretch()
    v_box.addLayout(h_box1)

    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle('Ders')
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()
