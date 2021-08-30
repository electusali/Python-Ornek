import sys 
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani=QtWidgets.QLabel('Bana Tiklanmadi')
        self.buton=QtWidgets.QPushButton('tikla')
        self.sayi=0
    
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)

        self.buton.clicked.connect(self.tikla)

        self.show()    
    def tikla(self):
        self.sayi+=1
        self.yazi_alani.setText(f'bana  {str(self.sayi)}  kez tikladi')
app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())