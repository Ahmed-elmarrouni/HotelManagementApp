# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LOGINMainWindow(object):
    def setupUi(self, LOGINMainWindow):
        LOGINMainWindow.setObjectName("LOGINMainWindow")
        LOGINMainWindow.resize(526, 600)
        LOGINMainWindow.setStyleSheet("background-color: rgb(151, 151, 168)")
        self.centralwidget = QtWidgets.QWidget(LOGINMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Email_input.setGeometry(QtCore.QRect(60, 150, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Email_input.setFont(font)
        self.Email_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Email_input.setText("")
        self.Email_input.setObjectName("Email_input")
        self.Password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_input.setGeometry(QtCore.QRect(60, 290, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Password_input.setFont(font)
        self.Password_input.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.Password_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Password_input.setText("")
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setObjectName("Password_input")
        self.Signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Signup_btn.setGeometry(QtCore.QRect(60, 430, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Signup_btn.setFont(font)
        self.Signup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Signup_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: blue\n"
"")
        self.Signup_btn.setObjectName("Signup_btn")
        self.Singin_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Singin_btn.setGeometry(QtCore.QRect(320, 430, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Singin_btn.setFont(font)
        self.Singin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Singin_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.Singin_btn.setObjectName("Singin_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        LOGINMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOGINMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 29))
        self.menubar.setObjectName("menubar")
        LOGINMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LOGINMainWindow)
        self.statusbar.setObjectName("statusbar")
        LOGINMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LOGINMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LOGINMainWindow)

    def retranslateUi(self, LOGINMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LOGINMainWindow.setWindowTitle(_translate("LOGINMainWindow", "MainWindow"))
        self.Email_input.setPlaceholderText(_translate("LOGINMainWindow", "Email                                   "))
        self.Password_input.setPlaceholderText(_translate("LOGINMainWindow", "Password                              "))
        self.Signup_btn.setText(_translate("LOGINMainWindow", "Sing up"))
        self.Singin_btn.setText(_translate("LOGINMainWindow", "Sing in"))
        self.label.setText(_translate("LOGINMainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGINMainWindow = QtWidgets.QMainWindow()
    ui = Ui_LOGINMainWindow()
    ui.setupUi(LOGINMainWindow)
    LOGINMainWindow.show()
    sys.exit(app.exec_())
