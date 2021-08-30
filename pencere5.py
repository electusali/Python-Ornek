import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget)
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.sayi1=0
        self.sayi2=0
        self.sayi3=0
        self.islem=''
    def init_ui(self):
        self.line_edit=QtWidgets.QLineEdit()
        self.arti=QtWidgets.QPushButton('+')
        self.eksi=QtWidgets.QPushButton('-')
        self.bolme=QtWidgets.QPushButton('/')
        self.carpma=QtWidgets.QPushButton('*')
        self.esit=QtWidgets.QPushButton('=')
        self.sonuc=QtWidgets.QLabel() 

        h_box=QtWidgets.QHBoxLayout()
        h_box.addWidget(self.arti)
        h_box.addWidget(self.eksi)
      
        h_box2=QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.bolme)
        h_box2.addWidget(self.carpma)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.line_edit)
        v_box.addWidget(h_box)
         v_box.addWidget(h_box2)
         v_box.addWidget(self.esit) 
         v_box.addStretch()
          v_box.addWidget(self.sonuc)
        v_box.addStretch()

        self.arti.clicked.connect(self.tikla)
        self.eksi.clicked.connect(self.tikla)
        self.bolme.clicked.connect(self.tikla)
        self.carpma.clicked.connect(self.tikla)
        self.esit.clicked.connect(self.tikla)
        self.setLayout(v_box)
        self.show()

        def tikla(self):
            gonderen=self.sender()

            if gonderen.text()='+':
                pass
            elif gonderen.text()='-'
                pass
            elif gonderen.text()='/'
                pass
            elif gonderen.text()='*'
                pass
            elif gonderen.text()='='
                pass



app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
pencere.setWindowTitle('hes mak')
sys.exit(app.exec_())
