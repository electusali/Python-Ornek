import sys
from PyQt5.QtWidgets import QWidget, QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QLineEdit,QCheckBox,QHBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazi=QLineEdit('hng dil sev')
        self.py=QRadioButton('python')
        self.java=QRadioButton('java')
        self.c=QRadioButton('c++')
        self.che1=QCheckBox('Bayan')
        self.che2=QCheckBox('erk')
        self.buton=QPushButton('Gonder')
        self.btn1=QPushButton('tamam')
        self.btn2=QPushButton('cikis')
        self.btn3=QPushButton('secim')

        h_box=QHBoxLayout()

        v_box=QVBoxLayout()
        v_box.addWidget(py)
        v_box.addWidget(java)
        v_box.addWidget(c)

        
        h_box.addLayout(v_box)

        h_box.addStretch()
        h_box.addWidget(che1)
        h_box.addWidget(che2)

        h_box.addWidget(btn)
        h_box.addWidget(btn)
        h_box.addWidget(btn2)
        h_box.addWidget(btn3)

        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
