# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CHAMBRE.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CHAMBREMainWindow(object):
    def setupUi(self, CHAMBREMainWindow):
        CHAMBREMainWindow.setObjectName("CHAMBREMainWindow")
        CHAMBREMainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        CHAMBREMainWindow.setFont(font)
        CHAMBREMainWindow.setStyleSheet("background-color: #0D2235;")
        self.centralwidget = QtWidgets.QWidget(CHAMBREMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 301, 491))
        font = QtGui.QFont()
        font.setPointSize(104)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:2px  solid rgb(46, 46, 255);\n"
"border-radius: 80px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:  rgb(69, 78, 255)")
        self.label_2.setObjectName("label_2")
        self.Number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Number_input.setGeometry(QtCore.QRect(342, 131, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Number_input.setFont(font)
        self.Number_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Number_input.setText("")
        self.Number_input.setObjectName("Number_input")
        self.Description_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Description_input.setGeometry(QtCore.QRect(340, 230, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Description_input.setFont(font)
        self.Description_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Description_input.setText("")
        self.Description_input.setObjectName("Description_input")
        self.Tarif_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Tarif_input.setGeometry(QtCore.QRect(340, 330, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Tarif_input.setFont(font)
        self.Tarif_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: white;\n"
"padding-bottom:7px;\n"
"color: rgb(255, 255, 255)")
        self.Tarif_input.setText("")
        self.Tarif_input.setObjectName("Tarif_input")
        self.Add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(340, 440, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Add_btn.setFont(font)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.Add_btn.setObjectName("Add_btn")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(600, 440, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.Delete_btn.setObjectName("Delete_btn")
        CHAMBREMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CHAMBREMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        CHAMBREMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CHAMBREMainWindow)
        self.statusbar.setObjectName("statusbar")
        CHAMBREMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CHAMBREMainWindow)
        QtCore.QMetaObject.connectSlotsByName(CHAMBREMainWindow)

    def retranslateUi(self, CHAMBREMainWindow):
        _translate = QtCore.QCoreApplication.translate
        CHAMBREMainWindow.setWindowTitle(_translate("CHAMBREMainWindow", "MainWindow"))
        self.label.setText(_translate("CHAMBREMainWindow", ""))
        self.label_2.setText(_translate("CHAMBREMainWindow", "GERER CHAMBRE"))
        self.Number_input.setPlaceholderText(_translate("CHAMBREMainWindow", "Number"))
        self.Description_input.setPlaceholderText(_translate("CHAMBREMainWindow", "Description"))
        self.Tarif_input.setPlaceholderText(_translate("CHAMBREMainWindow", "Tarif"))
        self.Add_btn.setText(_translate("CHAMBREMainWindow", "Add "))
        self.Delete_btn.setText(_translate("CHAMBREMainWindow", "Delete "))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     CHAMBREMainWindow = QtWidgets.QMainWindow()
#     ui = Ui_CHAMBREMainWindow()
#     ui.setupUi(CHAMBREMainWindow)
#     CHAMBREMainWindow.show()
#     sys.exit(app.exec_())
