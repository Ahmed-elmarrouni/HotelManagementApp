import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from VISITEUR import Ui_VISITEURMainWindow
from PyQt5.QtWidgets import QMessageBox


class VISITEUR(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VISITEURMainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    visiteur = VISITEUR()
    visiteur.show()
    sys.exit(app.exec_())
    

