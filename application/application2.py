from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('MY APP')
main_win.resize(900,800)
main_win.move(500,100)
main_win.show()
label1=QLabel('Welcome to the Health status detection program!')
label2=QLabel('This application allows you to use the Rufier test to make an initial diagnosis of your health.')
label3=QLabel('line.addWidget(label2,alignment=Qt.AlignLeft)')
label1=QLabel('Welcome to the Health status detection program!')
button=QPushButton('Generate')





#exemple
   


line=QVBoxLayout()

line.addWidget(label1,alignment=Qt.AlignLeft)
line.addWidget(label2,alignment=Qt.AlignLeft)
line.addWidget(label3,alignment=Qt.AlignLeft)
line.addWidget(button,alignment=Qt.AlignCenter)

main_win.setLayout(line)



app.exec_()
