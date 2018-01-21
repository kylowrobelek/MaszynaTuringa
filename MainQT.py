#-*- coding: utf-8 -*-

import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
import pudb
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
#from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit
#from PyQt5.QtCore import QSize
from MainWindow import Ui_MaszynaTuringa
from Input import Ui_Input
from InputQT import Input
from Turing import DefineTuring
from AlfabetQT import Alfabet
from TransitionFunction import TransitionFunction


class MainWindow(QDialog):

    transitionFunction = {}
    flagIfAdded = False
    initial_state = ''
    finalState = ''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MaszynaTuringa()
        self.ui.setupUi(self)
        self.transition = TransitionFunction()
        self.alfaWindow = Alfabet()
        self.inputWindow = Input()
        self.ui.addState.clicked.connect(self.addStates)
        self.ui.addInputButton.clicked.connect(self.showInputWindow)
        self.ui.addAlphabet.clicked.connect(self.showAlfaWindow)
        self.ui.pushButton.clicked.connect(self.performCounting)
        self.ui.resetButton.clicked.connect(self.resetAll)
        # self.turing = DefineTuring()


    def unicodeToString(self, uniString):
        return uniString.encode('ascii', 'ignore')

    def makeTransition(self):
        if self.ui.beginStateRadioButton.isChecked():
            if self.ui.checkIfTextBeginNotNone():
                self.initial_state = self.unicodeToString(self.ui.textStateBeginEditor.text())
            else:
                QMessageBox.about(self, "Błąd", "Podaj stan początkowy!")
        elif self.ui.statesRadioButton.isChecked():
            if self.ui.checkIfTextFieldNotNone():
                if self.ui.btnstate() is None:
                    QMessageBox.about(self, "Błąd", "Proszę podać kierunek przejścia!")
                else:
                    try:
                        self.transitionFunction = self.transition.qtTransition(self.ui.textStateBeforeEditor.text(), self.ui.textCharBeforeEditor.text(), self.ui.textStateAfterEditor.text(), self.ui.textCharAfterEditor.text(), self.ui.btnstate())
                    except:
                        QMessageBox.about(self, "Błąd", "Znak musi pokrywać się z alfabetem!")
            else:
                QMessageBox.about(self, "Błąd", "Podaj definicje wszystkich stanów!")
        elif self.ui.finishStateRadioButton.isChecked():
            if self.ui.checkIfTextFinishNotNone():
                self.finalState = self.unicodeToString(self.ui.textStateFinishEditor.text())
            else:
                QMessageBox.about(self, "Błąd", "Podaj stany końcowe!")

    def checkIfAllOk(self):
        if self.initial_state is not '' and len(self.transition.transition) is not 0 and self.finalState is not '':
            self.ui.pushButton.setEnabled(True)


    @pyqtSlot()
    def addStates(self):
        self.makeTransition()
        self.checkIfAllOk()
        self.ui.cleanText()

    @pyqtSlot()
    def showInputWindow(self):
        self.inputWindow.alphabet = self.alfaWindow.addedAlphabet
        self.transition.alphabet = self.alfaWindow.addedAlphabet
        self.inputWindow.show()
        self.ui.addState.setEnabled(True)

    @pyqtSlot()
    def showAlfaWindow(self):
        self.alfaWindow.show()
        self.ui.addInputButton.setEnabled(True)

    @pyqtSlot()
    def performCounting(self):
        self.turing = DefineTuring(tape=self.inputWindow.addInput, blank_symbol=self.alfaWindow.blankSymbol, initial_state=self.initial_state, finalState=self.finalState, transitionFunction=self.transition.transition)
        if self.checkIfFinalState():
            self.turing.performAction()
            self.ui.resultText.setText(self.turing.get_tape())
            self.ui.resultLabel.setText("Wynik:")
        else:
            QMessageBox.about(self, "Błąd", "Maszyna zdefiniowana niepoprawnie!")
    @pyqtSlot()
    def resetAll(self):
        self.inputWindow.addInput = ''
        self.alfaWindow.addedAlphabet = []
        self.alfaWindow.blankSymbol = ''
        self.initial_state = ''
        self.finalState = {}
        self.transition.transition = {}
        self.ui.resultText.setText('')
        self.ui.resultLabel.setText('')
        self.ui.pushButton.setEnabled(False)
        self.ui.addInputButton.setEnabled(False)
        self.ui.addState.setEnabled(False)

    def checkIfFinalState(self):
        for i in self.transition.transition.values():
            if not self.finalState in i:
                return False
            else:
                return True



