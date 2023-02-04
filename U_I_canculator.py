import os
os.system('cls')

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys

app = QApplication(sys.argv)
oyna = QWidget()



oyna.setWindowIcon(QIcon("C:\\Users\\ASUS\\Desktop\\python\\PyQt5\\1"))
oyna.setWindowTitle("Birinchi dastur")
# oyna.setGeometry(550,300, 450,250*2)
oyna.setFixedSize(400,600)


kiritish = QLineEdit(oyna)
kiritish.setFont(QFont("Calibri",30))
kiritish.setStyleSheet("color:white; background-color:black")
kiritish.move(1,200)

# kiritish.setFont(QFont("Times",15))

def OpenQovis():
    kiritish.setText(kiritish.text() + "(") 

def CloseQovis():
    kiritish.setText(kiritish.text() + ")")

def Clear():
    kiritish.setText("")

def One():
    kiritish.setText(kiritish.text() + "1")

def Result():
    kiritish.setText(str(eval(kiritish.text())))

def Plus():
    kiritish.setText(kiritish.text() + "+")

def percent():
    kiritish.setText(kiritish.text() + "%")

def minus():
    kiritish.setText(kiritish.text() + "-")

def rise():
    kiritish.setText(kiritish.text() + "*")



def Pencil():
    text = kiritish.text()
    text = text[:-1]
    kiritish.setText(text)

def two():
    kiritish.setText(kiritish.text() + "2")

def three():
    kiritish.setText(kiritish.text() + "3")
    
def four():
    kiritish.setText(kiritish.text() + "4")

def five():
    kiritish.setText(kiritish.text() + "5")

def olti():
    kiritish.setText(kiritish.text() + "6")

def seven():
    kiritish.setText(kiritish.text() + "7")

def eight():
    kiritish.setText(kiritish.text() + "8")

def nine():
    kiritish.setText(kiritish.text() + "9")

def zero(): 
    kiritish.setText(kiritish.text() + "0")

def delete():
    kiritish.setText(kiritish.text() + ".")


button1 = QPushButton("﹙", oyna)
button1.move(10, 320)
button1.setFont(QFont("Colcalos",18))
button1.setStyleSheet("color:white; background-color:gray")
button1.clicked.connect(OpenQovis)



button2 = QPushButton("﹚", oyna)
button2.move(105, 320)
button2.setFont(QFont("Colcalos",18))
button2.setStyleSheet("color:white; background-color:gray")
button2.clicked.connect(CloseQovis)




button3 = QPushButton("C", oyna)
button3.move(200, 320)
button3.setFont(QFont("Colcalos",18))
button3.setStyleSheet("color:white; background-color:gray")
button3.clicked.connect(Clear)


tugma1 = QPushButton("«", oyna)
tugma1.move(295, 320)
tugma1.setFont(QFont("Colcalos",18))
tugma1.setStyleSheet("color:white; background-color:gray")
tugma1.clicked.connect(Pencil)

button4 = QPushButton("7", oyna)
button4.move(10, 370)
button4.setFont(QFont("Colcalos",18))
button4.setStyleSheet("color:white; background-color:gray")
button4.clicked.connect(seven)

button5 = QPushButton("8", oyna)
button5.move(105, 370)
button5.setFont(QFont("Colcalos",18))
button5.setStyleSheet("color:white; background-color:gray")
button5.clicked.connect(eight)

button6 = QPushButton("9", oyna)
button6.move(200, 370)
button6.setFont(QFont("Colcalos",18))
button6.setStyleSheet("color:white; background-color:gray")
button6.clicked.connect(nine)

tugma2 = QPushButton("%", oyna)
tugma2.move(295, 370)
tugma2.setFont(QFont("Colcalos",18))
tugma2.setStyleSheet("color:white; background-color:gray")
tugma2.clicked.connect(percent)


button7 = QPushButton("4", oyna)
button7.move(10, 420)
button7.setFont(QFont("Colcalos",18))
button7.setStyleSheet("color:white; background-color:gray")
button7.clicked.connect(four)

button8 = QPushButton("5", oyna)
button8.move(105, 420)
button8.setFont(QFont("Colcalos",18))
button8.setStyleSheet("color:white; background-color:gray")
button8.clicked.connect(five)

button9 = QPushButton("6", oyna)
button9.move(200, 420)
button9.setFont(QFont("Colcalos",18))
button9.setStyleSheet("color:white; background-color:gray")
button9.clicked.connect(olti)

tugma3 = QPushButton("*", oyna)
tugma3.move(295, 420)
tugma3.setFont(QFont("Colcalos",18))
tugma3.setStyleSheet("color:white; background-color:gray")
tugma3.clicked.connect(rise)

button10 = QPushButton("1", oyna)
button10.move(10, 470)
button10.setFont(QFont("Colcalos",18))
button10.setStyleSheet("color:white; background-color:gray")
button10.clicked.connect(One)


tugma4 = QPushButton("2", oyna)
tugma4.move(105, 470)
tugma4.setFont(QFont("Colcalos",18))
tugma4.setStyleSheet("color:white; background-color:gray")
tugma4.clicked.connect(two)

tugma5 = QPushButton("3", oyna)
tugma5.move(200, 470)
tugma5.setFont(QFont("Colcalos",18))
tugma5.setStyleSheet("color:white; background-color:gray")
tugma5.clicked.connect(three)

tugma6 = QPushButton("-", oyna)
tugma6.move(295, 470)
tugma6.setFont(QFont("Colcalos",18))
tugma6.setStyleSheet("color:white; background-color:gray")
tugma6.clicked.connect(minus)

tugma7 = QPushButton("0", oyna)
tugma7.move(10, 520)
tugma7.setFont(QFont("Colcalos",18))
tugma7.setStyleSheet("color:white; background-color:gray")
tugma7.clicked.connect(zero)

tugma8 = QPushButton(".", oyna)
tugma8.move(105, 520)
tugma8.setFont(QFont("Colcalos",18))
tugma8.setStyleSheet("color:white; background-color:gray")
tugma8.clicked.connect(delete)

tugma9 = QPushButton("=", oyna)
tugma9.move(200, 520)
tugma9.setFont(QFont("Colcalos",18))
tugma9.setStyleSheet("color:white; background-color:gray")
tugma9.clicked.connect(Result)

tugma0 = QPushButton("+", oyna)
tugma0.move(295, 520)
tugma0.setFont(QFont("Colcalos",18))
tugma0.setStyleSheet("color:white; background-color:gray")
tugma0.clicked.connect(Plus)



oyna.show()
sys.exit(app.exec_())
