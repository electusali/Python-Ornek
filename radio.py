import sys
from PyQt5.QtWidgets import QWidget, QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazi=QLabel('hng dil sev')
        self.java=QRadioButton('java')
        self.py=QRadioButton('py')
        self.ph=QRadioButton('ph')
        self.yazi_alani=QLabel('')
        self.buton=QPushButton('Gonder')

        v_box=QVBoxLayout()
        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.py)
        v_box.addWidget(self.ph)
        v_box.addWidget(self.buton)


        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.tikla(self.chebox.isChecked(),self.yazi_alan))


