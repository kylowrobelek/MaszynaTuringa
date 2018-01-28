# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alfabet.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DodawanieAlfabetu(object):
    def setupUi(self, DodawanieAlfabetu):
        DodawanieAlfabetu.setObjectName("DodawanieAlfabetu")
        DodawanieAlfabetu.setFixedSize(354,114)
        self.addAlfaButton = QtWidgets.QPushButton(DodawanieAlfabetu)
        self.addAlfaButton.setGeometry(QtCore.QRect(200, 70, 113, 32))
        self.addAlfaButton.setObjectName("addAlfaButton")
        self.cancelAlfaButton = QtWidgets.QPushButton(DodawanieAlfabetu)
        self.cancelAlfaButton.setGeometry(QtCore.QRect(30, 70, 113, 32))
        self.cancelAlfaButton.setObjectName("cancelAlfaButton")
        self.labelInfoAlfabet = QtWidgets.QLabel(DodawanieAlfabetu)
        self.labelInfoAlfabet.setGeometry(QtCore.QRect(60, 10, 61, 21))
        self.labelInfoAlfabet.setObjectName("labelInfoAlfabet")
        self.alphabetInputEditor = QtWidgets.QLineEdit(DodawanieAlfabetu)
        self.alphabetInputEditor.setGeometry(QtCore.QRect(40, 40, 91, 21))
        self.alphabetInputEditor.setObjectName("alphabetInputEditor")
        self.blankSymbolEditor = QtWidgets.QLineEdit(DodawanieAlfabetu)
        self.blankSymbolEditor.setGeometry(QtCore.QRect(210, 40, 91, 21))
        self.blankSymbolEditor.setObjectName("blankSymbolEditor")
        self.labelBlankSybmol = QtWidgets.QLabel(DodawanieAlfabetu)
        self.labelBlankSybmol.setGeometry(QtCore.QRect(210, 10, 91, 20))
        self.labelBlankSybmol.setObjectName("labelBlankSybmol")

        self.retranslateUi(DodawanieAlfabetu)
        QtCore.QMetaObject.connectSlotsByName(DodawanieAlfabetu)

    def retranslateUi(self, DodawanieAlfabetu):
        _translate = QtCore.QCoreApplication.translate
        DodawanieAlfabetu.setWindowTitle(_translate("DodawanieAlfabetu", "Dodanie Alfabetu"))
        self.cancelAlfaButton.setText(_translate("DodawanieAlfabetu", "Cancel"))
        self.addAlfaButton.setText(_translate("DodawanieAlfabetu", "Dodaj"))
        self.labelInfoAlfabet.setText(_translate("DodawanieAlfabetu", "Symbole"))
        self.labelBlankSybmol.setText(_translate("DodawanieAlfabetu", "Symbol pusty"))



