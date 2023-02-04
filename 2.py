from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SET_BOX")
        self.setFixedSize(500,500)
        self.setStyleSheet("background-color:cyan;")

        self.Checking = False
        self.grid = QGridLayout()
        self.h_lay = QHBoxLayout()
        self.h_str_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.msg = QMessageBox()
        self.msg.setWindowTitle("RESULT")

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn10 = QPushButton("10")
        self.btn11 = QPushButton("11")
        self.btn12 = QPushButton("12")
        self.btn13 = QPushButton("13")
        self.btn14 = QPushButton("14")
        self.btn15 = QPushButton("15")
        self.btn16 = QPushButton("")



        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12, self.btn13, self.btn14, self.btn15, self.btn16]
        index = 0

        self.mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]
        self.newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]

        
        self.str_style = """QPushButton {
            color:red;
            background-color:white;
            font: bold 30pt;}"""

        for i in range(4):
            for j in range(4):
                self.grid.addWidget(self.lst[index], i, j)
                self.lst[index].setFixedSize(96,70)
                self.lst[index].setStyleSheet(self.str_style)
                self.lst[index].setDisabled(True)
                index+=1

        self.reset_btn = QPushButton("RESET")
        self.reset_btn.clicked.connect(self.rest)
        self.reset_btn.setStyleSheet("background-color:gray; color:red")

        self.close_btn = QPushButton("CLOSE") 
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setStyleSheet("background-color:gray; color:red")

        self.start_btn = QPushButton("START")
        self.start_btn.clicked.connect(self.start)
        self.start_btn.setStyleSheet("background-color:gray; color:red")


        self.h_str_lay.addStretch()
        self.h_str_lay.addStretch()


        self.h_lay.addWidget(self.reset_btn)
        self.h_lay.addWidget(self.close_btn)
        self.h_lay.addWidget(self.start_btn)

        self.v_main_lay.addLayout(self.grid)
        self.v_main_lay.addLayout(self.h_str_lay)
        self.v_main_lay.addLayout(self.h_lay)
        
        self.setLayout(self.v_main_lay)   

        self.btn1.clicked.connect(self.Btn1_Check)
        self.btn2.clicked.connect(self.Btn2_Check)
        self.btn3.clicked.connect(self.Btn3_Check)
        self.btn4.clicked.connect(self.Btn4_Check)
        self.btn5.clicked.connect(self.Btn5_Check)
        self.btn6.clicked.connect(self.Btn6_Check)
        self.btn7.clicked.connect(self.Btn7_Check)
        self.btn8.clicked.connect(self.Btn8_Check)
        self.btn9.clicked.connect(self.Btn9_Check)
        self.btn10.clicked.connect(self.Btn10_Check)
        self.btn11.clicked.connect(self.Btn11_Check)
        self.btn12.clicked.connect(self.Btn12_Check)
        self.btn13.clicked.connect(self.Btn13_Check)
        self.btn14.clicked.connect(self.Btn14_Check)
        self.btn15.clicked.connect(self.Btn15_Check)
        self.btn16.clicked.connect(self.Btn16_Check)

        self.show()
         
    def Btn1_Check(self):
        if self.btn2.text() == "":
            self.btn2.setText(self.btn1.text())
            self.btn1.setText("")

        elif self.btn5.text() == "":
            self.btn5.setText(self.btn1.text())
            self.btn1.setText("")
        
        self.Result_Checking()

    
    def Btn2_Check(self):
        if self.btn1.text() == "":
            self.btn1.setText(self.btn2.text())
            self.btn2.setText("")

        elif self.btn3.text() == "":
            self.btn3.setText(self.btn2.text())
            self.btn2.setText("")
        
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn2.text())
            self.btn2.setText("")

        self.Result_Checking()


    def Btn3_Check(self):
        if self.btn2.text() == "":
            self.btn2.setText(self.btn3.text())
            self.btn3.setText("")

        elif self.btn4.text() == "":
            self.btn4.setText(self.btn3.text())
            self.btn3.setText("")
        
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn3.text())
            self.btn3.setText("")

        self.Result_Checking()


    def Btn4_Check(self):
        if self.btn3.text() == "":
            self.btn3.setText(self.btn4.text())
            self.btn4.setText("")

        elif self.btn8.text() == "":
            self.btn8.setText(self.btn4.text())
            self.btn4.setText("")
        
        self.Result_Checking()

    
    def Btn5_Check(self):
        if self.btn1.text() == "":
            self.btn1.setText(self.btn5.text())
            self.btn5.setText("")

        elif self.btn6.text() == "":
            self.btn6.setText(self.btn5.text())
            self.btn5.setText("")
        
        elif self.btn9.text() == "":
            self.btn9.setText(self.btn5.text())
            self.btn5.setText("")

        self.Result_Checking()

    
    def Btn6_Check(self):
        if self.btn2.text() == "":
            self.btn2.setText(self.btn6.text())
            self.btn6.setText("")

        elif self.btn5.text() == "":
            self.btn5.setText(self.btn6.text())
            self.btn6.setText("")
        
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn6.text())
            self.btn6.setText("")

        elif self.btn10.text() == "":
            self.btn10.setText(self.btn6.text())
            self.btn6.setText("")


        self.Result_Checking()


    def Btn7_Check(self):
        if self.btn3.text() == "":
            self.btn3.setText(self.btn7.text())
            self.btn7.setText("")

        elif self.btn6.text() == "":
            self.btn6.setText(self.btn7.text())
            self.btn7.setText("")
        
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn7.text())
            self.btn7.setText("")

        elif self.btn11.text() == "":
            self.btn11.setText(self.btn7.text())
            self.btn7.setText("")

        self.Result_Checking()


    def Btn8_Check(self):
        if self.btn4.text() == "":
            self.btn4.setText(self.btn8.text())
            self.btn8.setText("")

        elif self.btn7.text() == "":
            self.btn7.setText(self.btn8.text())
            self.btn8.setText("")

        elif self.btn12.text() == "":
            self.btn12.setText(self.btn8.text())
            self.btn8.setText("")

        self.Result_Checking()

    
    def Btn9_Check(self):
        if self.btn5.text() == "":
            self.btn5.setText(self.btn9.text())
            self.btn9.setText("")

        elif self.btn10.text() == "":
            self.btn10.setText(self.btn9.text())
            self.btn9.setText("")
        
        elif self.btn13.text() == "":
            self.btn13.setText(self.btn9.text())
            self.btn9.setText("")

        self.Result_Checking()

    
    def Btn10_Check(self):
        if self.btn6.text() == "":
            self.btn6.setText(self.btn10.text())
            self.btn10.setText("")

        elif self.btn9.text() == "":
            self.btn9.setText(self.btn10.text())
            self.btn10.setText("")
        
        elif self.btn11.text() == "":
            self.btn11.setText(self.btn10.text())
            self.btn10.setText("")

        elif self.btn14.text() == "":
            self.btn14.setText(self.btn10.text())
            self.btn10.setText("")


        self.Result_Checking()


    def Btn11_Check(self):
        if self.btn7.text() == "":
            self.btn7.setText(self.btn11.text())
            self.btn11.setText("")

        elif self.btn10.text() == "":
            self.btn10.setText(self.btn11.text())
            self.btn11.setText("")
        
        elif self.btn12.text() == "":
            self.btn12.setText(self.btn11.text())
            self.btn11.setText("")

        elif self.btn15.text() == "":
            self.btn15.setText(self.btn11.text())
            self.btn11.setText("")


        self.Result_Checking()

    
    def Btn12_Check(self):
        if self.btn8.text() == "":
            self.btn8.setText(self.btn12.text())
            self.btn12.setText("")

        elif self.btn11.text() == "":
            self.btn11.setText(self.btn12.text())
            self.btn12.setText("")
        
        elif self.btn16.text() == "":
            self.btn16.setText(self.btn12.text())
            self.btn12.setText("")

        self.Result_Checking()


    def Btn13_Check(self):
        if self.btn9.text() == "":
            self.btn9.setText(self.btn13.text())
            self.btn13.setText("")

        elif self.btn14.text() == "":
            self.btn14.setText(self.btn13.text())
            self.btn13.setText("")
        
        self.Result_Checking()


    def Btn14_Check(self):
        if self.btn10.text() == "":
            self.btn10.setText(self.btn14.text())
            self.btn14.setText("")

        elif self.btn13.text() == "":
            self.btn13.setText(self.btn14.text())
            self.btn14.setText("")
        
        elif self.btn15.text() == "":
            self.btn15.setText(self.btn14.text())
            self.btn14.setText("")

        self.Result_Checking()

    def Btn15_Check(self):
        if self.btn11.text() == "":
            self.btn11.setText(self.btn15.text())
            self.btn15.setText("")

        elif self.btn14.text() == "":
            self.btn14.setText(self.btn15.text())
            self.btn15.setText("")

        elif self.btn16.text() == "":
            self.btn16.setText(self.btn15.text())
            self.btn15.setText("")

        self.Result_Checking()

    
    def Btn16_Check(self):
        if self.btn12.text() == "":
            self.btn12.setText(self.btn16.text())
            self.btn16.setText("")

        elif self.btn15.text() == "":
            self.btn15.setText(self.btn16.text())
            self.btn16.setText("")
        
        self.Result_Checking()



    def Result_Checking(self):
        if self.Checking == True:
            self.Result_List = []
            for i in self.lst:
                for j in self.newlist:
                    if i.text() == " " or i.text() == str(j):
                        self.Result_List.append(i.text())
            
            if self.newlist == self.Result_Checking:
                print("You Are Winner ! ")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setText("You Are Winner !")
                self.msg.buttonClicked.connect(self.msg.close)
                self.msg.exec_()
            

    def start(self):

        self.Checking =True

        random.shuffle(self.mylist)
        for i in range(16):
            self.lst[i].setText(str(self.mylist[i]))
            self.lst[i].setDisabled(False)
    
    def rest(self):
        for i in range(16):
            self.lst[i].setText(str(self.newlist[i]))
            self.lst[i].setDisabled(True)



app = QApplication([])
win = Window()
app.exec_()