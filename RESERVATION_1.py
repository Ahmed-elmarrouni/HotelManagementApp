import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from RESERVATION import Ui_RESERVATIONMainWindow
from PyQt5.QtWidgets import QMessageBox


class RESERVATION(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RESERVATIONMainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    reservation = RESERVATION()
    reservation.show()
    sys.exit(app.exec_())
    

