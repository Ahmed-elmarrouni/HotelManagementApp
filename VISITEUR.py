# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VISITEUR.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VISITEURMainWindow(object):
    def setupUi(self, VISITEURMainWindow):
        VISITEURMainWindow.setObjectName("VISITEURMainWindow")
        VISITEURMainWindow.resize(800, 707)
        VISITEURMainWindow.setStyleSheet("background-color: #6C2A6A")
        self.centralwidget = QtWidgets.QWidget(VISITEURMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Number_input.setGeometry(QtCore.QRect(322, 80, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Number_input.setFont(font)
        self.Number_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Number_input.setText("")
        self.Number_input.setObjectName("Number_input")
        self.Add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(320, 580, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Add_btn.setFont(font)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.Add_btn.setObjectName("Add_btn")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(580, 580, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.Delete_btn.setObjectName("Delete_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 100, 221, 231))
        font = QtGui.QFont()
        font.setPointSize(104)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.Surname_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Surname_input.setGeometry(QtCore.QRect(320, 160, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Surname_input.setFont(font)
        self.Surname_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Surname_input.setText("")
        self.Surname_input.setObjectName("Surname_input")
        self.FirstNameinput = QtWidgets.QLineEdit(self.centralwidget)
        self.FirstNameinput.setGeometry(QtCore.QRect(320, 240, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.FirstNameinput.setFont(font)
        self.FirstNameinput.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.FirstNameinput.setText("")
        self.FirstNameinput.setObjectName("FirstNameinput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 0, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgb(255, 37, 252)")
        self.label_2.setObjectName("label_2")
        self.Telephone_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Telephone_input.setGeometry(QtCore.QRect(320, 320, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Telephone_input.setFont(font)
        self.Telephone_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Telephone_input.setText("")
        self.Telephone_input.setObjectName("Telephone_input")
        self.City_input = QtWidgets.QLineEdit(self.centralwidget)
        self.City_input.setGeometry(QtCore.QRect(320, 400, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.City_input.setFont(font)
        self.City_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.City_input.setText("")
        self.City_input.setObjectName("City_input")
        self.Email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_input.setGeometry(QtCore.QRect(320, 480, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Email_input.setFont(font)
        self.Email_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Email_input.setText("")
        self.Email_input.setObjectName("Email_input")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 231, 231))
        font = QtGui.QFont()
        font.setPointSize(104)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 271, 561))
        self.label_3.setStyleSheet("border:2px  solid  rgb(255, 37, 252);\n"
"border-radius: 80px;\n"
"background-color:None")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        VISITEURMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VISITEURMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        VISITEURMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VISITEURMainWindow)
        self.statusbar.setObjectName("statusbar")
        VISITEURMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VISITEURMainWindow)
        QtCore.QMetaObject.connectSlotsByName(VISITEURMainWindow)

    def retranslateUi(self, VISITEURMainWindow):
        _translate = QtCore.QCoreApplication.translate
        VISITEURMainWindow.setWindowTitle(_translate("VISITEURMainWindow", "MainWindow"))
        self.Number_input.setPlaceholderText(_translate("VISITEURMainWindow", "Number                                "))
        self.Add_btn.setText(_translate("VISITEURMainWindow", "Add "))
        self.Delete_btn.setText(_translate("VISITEURMainWindow", "Delete "))
        self.label.setText(_translate("VISITEURMainWindow", ""))
        self.Surname_input.setPlaceholderText(_translate("VISITEURMainWindow", "Surname                              "))
        self.FirstNameinput.setPlaceholderText(_translate("VISITEURMainWindow", "First Name                            "))
        self.label_2.setText(_translate("VISITEURMainWindow", "GERER VISITEUR"))
        self.Telephone_input.setPlaceholderText(_translate("VISITEURMainWindow", " Telephone                           "))
        self.City_input.setPlaceholderText(_translate("VISITEURMainWindow", "City                                      "))
        self.Email_input.setPlaceholderText(_translate("VISITEURMainWindow", "Email                                   "))
        self.label_4.setText(_translate("VISITEURMainWindow", ""))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     VISITEURMainWindow = QtWidgets.QMainWindow()
#     ui = Ui_VISITEURMainWindow()
#     ui.setupUi(VISITEURMainWindow)
#     VISITEURMainWindow.show()
#     sys.exit(app.exec_())
