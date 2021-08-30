import sys 
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.say=0
    def init_ui():
        self.yazi_alani=QtWidgets.QLineEdit()
        self.buton1=QtWidgets.QPushButton('arttir')
        self.buton2=QtWidgets.QPushButton('azalt')
        self.yazi=QtWidgets.QLabel('')

        h_box=QtWidgets.QHBoxLayout()
        h_box.addWidget(buton1)
        h_box.addWidget(buton2)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(h_box)
        v_box.addStretch()
        v_box.addWidget(self.yazi)
        self.setLayout(h_box)
        self.buton1.clicked.connect(self.tikla)
        self.show()
     def tikla():
          veri=self.sender()
          if  veri.test=='Artir'
              self.say+=1
              self.yazi.setText(f'{str(self.sayi)}')
        else:
            self.say=1
              self.yazi.setText(f'{str(self.sayi)}')
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())