import sys
from PyQt5.QtWidgets import QWidget, QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.chebox=QCheckBox('Py sev')
        self.yazi_alan=QLabel('')
        self.buton=QPushButton('tikla')
        
        v_box=QVBoxLayout()
        v_box.addWidget(self.chebox)
        v_box.addWidget(self.yazi_alan)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle('da')
       # self.buton.clicked.connect(lambda : self.click(self.chebox.isChecked(),self.yazi_alan))
        self.buton.clicked.connect(lambda : self.tikla(self.chebox.isChecked(),self.yazi_alan))
        self.show()

        def tikla(self,chebox,yazi_alan):
            if chebox:
                yazi_alan.setText('sev')
            else:
                yazi_alan.setText('sevmiyor')


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
