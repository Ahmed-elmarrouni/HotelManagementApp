import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from CHOOSE import Ui_CHOOSEMainWindow
from PyQt5.QtWidgets import QMessageBox

from CHAMBRE import Ui_CHAMBREMainWindow
from VISITEUR import Ui_VISITEURMainWindow
from RESERVATION import Ui_RESERVATIONMainWindow


class CHOOSE(QtWidgets.QMainWindow):

    def openWindowA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CHAMBREMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VISITEURMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindowC(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RESERVATIONMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def __init__(self):
        super().__init__()
        self.ui = Ui_CHOOSEMainWindow()
        self.ui.setupUi(self)
        
        self.Chambre_btn = self.ui.Chambre_btn
        self.Visiteur_btn = self.ui.Visiteur_btn
        self.Reservation_btn = self.ui.Reservation_btn

        self.Chambre_btn.clicked.connect(self.Chambre_click)
        self.Visiteur_btn.clicked.connect(self.Visiteur_click)
        self.Reservation_btn.clicked.connect(self.Reservation_click)
        
    def Chambre_click(self):
        self.openWindowA()
   
    def Visiteur_click(self):
        self.openWindowB()
           
    def Reservation_click(self):
        self.openWindowC()
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    choose = CHOOSE()
    choose.show()
    sys.exit(app.exec_())
