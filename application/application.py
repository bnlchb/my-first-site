from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('MY APP')
main_win.resize(900,800)
main_win.move(500,100)
main_win.show()
label1=QLabel('click to fund me')
label2=QLabel('?')
button=QPushButton('Generate')

def show_winner():
    number=randint(100,5000)
    label2.setText(str(number)) 
    label1.setText("winer is :")


button.clicked.connect(show_winner)
#exemple
def exeemple():
    print('hello')
button.clicked.connect(exeemple)    


line=QVBoxLayout()

line.addWidget(label1,alignment=Qt.AlignCenter)
line.addWidget(label2,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)

main_win.setLayout(line)



app.exec_()
