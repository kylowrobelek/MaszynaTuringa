#-*- coding: utf-8 -*-

import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
#from PyQt5.QtCore import QSize
from MainWindow import Ui_MaszynaTuringa
import TransitionFunction
from Input import Ui_Input
import Turing


class Input(QDialog):

    addInput = ''
    alphabet = ''

    def __init__(self):
        super(Input, self).__init__()
        self.ui = Ui_Input()
        self.ui.setupUi(self)
        self.ui.addInputButton.clicked.connect(self.addInputBtn)
        self.ui.cancelInputButton.clicked.connect(self.cancelInputBtn)

    def checkIfTextNotNone(self):
        if self.ui.inputEditor.text() is not u'':
            return True
        else:
            return False



    def unicodeToString(self, uniString):
        return uniString.encode('ascii', 'ignore')

    def splitString(self):
        if self.checkIfTextNotNone():
            inputString = self.unicodeToString(self.ui.inputEditor.text())
            return inputString
        else:
            QMessageBox.about(self, "Błąd", "Podaj wejście!")

    @pyqtSlot()
    def addInputBtn(self):
        if self.checkIfInputOk():
            self.addInput = self.splitString()
            self.close()
            self.clear()
        else:
            QMessageBox.about(self, "Błąd", "Wejście musi pokrywać się z alfabetem!")

    @pyqtSlot()
    def cancelInputBtn(self):
        self.close()
        self.clear()


    def checkIfInputOk(self):
        for i in self.splitString():
            if i not in self.alphabet:
                return False
        return True

    def clear(self):
        self.ui.inputEditor.setText('')
