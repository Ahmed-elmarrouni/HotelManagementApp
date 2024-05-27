import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from LOGIN import Ui_LOGINMainWindow
from PyQt5.QtWidgets import QMessageBox

from CHOOSE import Ui_CHOOSEMainWindow


class LOGIN(QtWidgets.QMainWindow):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CHOOSEMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_LOGINMainWindow()
        self.ui.setupUi(self)
        
        self.Singin_btn = self.ui.Singin_btn
        self.Signup_btn = self.ui.Signup_btn
        self.Email_input = self.ui.Email_input
        self.Password_input = self.ui.Password_input

        self.Singin_btn.clicked.connect(self.Singin_click)
        self.Signup_btn.clicked.connect(self.Signup_click)

    def Singin_click(self):
        User_dejafound = False

        file_data = open("UserandPassword.txt", "r")
        file_data = file_data.readlines()

        for i in range(len(file_data)):
            if file_data[i] == (self.Email_input.text()+"," + self.Password_input.text()+"\n"):
                User_dejafound = True

        if User_dejafound == True:
            self.openWindow()
        else:
            print("User Not Found")
            

    def Signup_click(self):
        with open("UserandPassword.txt", "a") as file_data:
            file_data.write(self.Email_input.text() + "," + self.Password_input.text() + "\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = LOGIN()
    login.show()
    sys.exit(app.exec_())
