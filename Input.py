# -*- coding: utf-8 -*-

# Input implementation generated from reading ui file 'Input.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_Input(object):
    def setupUi(self, Input):
        Input.setObjectName("Input")
        Input.resize(358, 158)
        self.addInputButton = QtWidgets.QPushButton(Input)
        self.addInputButton.setGeometry(QtCore.QRect(230, 110, 113, 32))
        self.addInputButton.setObjectName("addInputButton")
        self.inputEditor = QtWidgets.QLineEdit(Input)
        self.inputEditor.setGeometry(QtCore.QRect(30, 70, 301, 21))
        self.inputEditor.setObjectName("inputEditor")
        self.labelInfoInput = QtWidgets.QLabel(Input)
        self.labelInfoInput.setGeometry(QtCore.QRect(50, 30, 271, 16))
        self.labelInfoInput.setObjectName("labelInfoInput")
        self.cancelInputButton = QtWidgets.QPushButton(Input)
        self.cancelInputButton.setGeometry(QtCore.QRect(20, 110, 113, 32))
        self.cancelInputButton.setObjectName("cancelInputButton")

        self.retranslateUi(Input)
        QtCore.QMetaObject.connectSlotsByName(Input)


    def retranslateUi(self, Input):
        _translate = QtCore.QCoreApplication.translate
        Input.setWindowTitle(_translate("Input", "Wejście"))
        self.addInputButton.setText(_translate("Input", "Dodaj"))
        self.labelInfoInput.setText(_translate("Input", "Podaj tylko znaki zdefiniowane w alfabecie!"))
        self.cancelInputButton.setText(_translate("Input", "Cancel"))