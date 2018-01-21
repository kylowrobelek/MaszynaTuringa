#-*- coding: utf-8 -*-

import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
#from PyQt5.QtCore import QSize
from MainWindow import Ui_MaszynaTuringa
from Input import Ui_Input
import TransitionFunction
from Alfabet import Ui_DodawanieAlfabetu
import Turing


class Alfabet(QDialog):

    addedAlphabet = []
    blankSymbol = ''
    #flagIfAlpaAdded  = False

    def __init__(self):
        super(Alfabet, self).__init__()
        self.ui = Ui_DodawanieAlfabetu()
        self.ui.setupUi(self)
        self.ui.addAlfaButton.clicked.connect(self.addAlphabetBtn)
        self.ui.cancelAlfaButton.clicked.connect(self.cancelAlphabetBtn)

    def checkIfTextNotNone(self):
        if self.ui.alphabetInputEditor.text() is not u'':
            return True
        else:
            return False

    def unicodeToString(self, uniString):
        return uniString.encode('ascii', 'ignore')

    def splitString(self):
        if self.checkIfTextNotNone():
            self.blankSymbol = self.unicodeToString(self.ui.blankSymbolEditor.text())
            inputString = list(self.unicodeToString(self.ui.alphabetInputEditor.text()))
            inputString.append(self.blankSymbol)
            return inputString
        else:
            QMessageBox.about(self, "Błąd", "Alfabet musi być zdefiniowany!")

    @pyqtSlot()
    def addAlphabetBtn(self):
        self.addedAlphabet = self.splitString()
        self.close()
        self.clear()

    @pyqtSlot()
    def cancelAlphabetBtn(self):
        self.close()
        self.clear()

    def clear(self):
        self.ui.blankSymbolEditor.setText('')
        self.ui.alphabetInputEditor.setText('')

