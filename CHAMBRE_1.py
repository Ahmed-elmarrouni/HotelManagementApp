import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from CHAMBRE import Ui_CHAMBREMainWindow
from PyQt5.QtWidgets import QMessageBox


class CHAMBRE(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CHAMBREMainWindow()
        self.ui.setupUi(self)
        
        
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    chambre = CHAMBRE()
    chambre.show()
    sys.exit(app.exec_())
    

