# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5 import QtCore, QtGui, QtWidgets
from Input import Ui_Input
from Alfabet import Ui_DodawanieAlfabetu
import pudb

class Ui_MaszynaTuringa(object):
    maszyna = ''
    def setupUi(self, MaszynaTuringa):
        MaszynaTuringa.setObjectName("MaszynaTuringa")
        MaszynaTuringa.setFixedSize(609, 393)
        self.addState = QtWidgets.QPushButton(MaszynaTuringa)
        self.addState.setGeometry(QtCore.QRect(140, 100, 181, 32))
        self.addState.setObjectName("addState")
        self.addState.setEnabled(False)
        self.labelStateBegin = QtWidgets.QLabel(MaszynaTuringa)
        self.labelStateBegin.setGeometry(QtCore.QRect(190, 20, 111, 16))
        self.labelStateBegin.setObjectName("labelStateBegin")
        self.labelStateBegin.hide()
        self.labelStateFinish = QtWidgets.QLabel(MaszynaTuringa)
        self.labelStateFinish.setGeometry(QtCore.QRect(190, 20, 111, 16))
        self.labelStateFinish.setObjectName("labelStateFinish")
        self.labelStateFinish.hide()
        self.textStateBeginEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textStateBeginEditor.setGeometry(QtCore.QRect(200, 40, 81, 21))
        self.textStateBeginEditor.setObjectName("textStateBeginEditor")
        self.textStateBeginEditor.hide()
        self.textStateFinishEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textStateFinishEditor.setGeometry(QtCore.QRect(200, 40, 81, 21))
        self.textStateFinishEditor.setObjectName("textStateFinishEditor")
        self.textStateFinishEditor.hide()
        self.labelStateBefore = QtWidgets.QLabel(MaszynaTuringa)
        self.labelStateBefore.setGeometry(QtCore.QRect(50, 20, 71, 16))
        self.labelStateBefore.setObjectName("labelStateBefore")
        self.labelStateBefore.hide()
        self.labelStateAfter = QtWidgets.QLabel(MaszynaTuringa)
        self.labelStateAfter.setGeometry(QtCore.QRect(260, 20, 51, 16))
        self.labelStateAfter.setObjectName("labelStateAfter")
        self.labelStateAfter.hide()
        self.labelCharBefore = QtWidgets.QLabel(MaszynaTuringa)
        self.labelCharBefore.setGeometry(QtCore.QRect(150, 20, 71, 16))
        self.labelCharBefore.setObjectName("labelCharBefore")
        self.labelCharBefore.hide()
        self.labelCharAfter = QtWidgets.QLabel(MaszynaTuringa)
        self.labelCharAfter.setGeometry(QtCore.QRect(360, 20, 51, 16))
        self.labelCharAfter.setObjectName("labelCharAfter")
        self.labelCharAfter.hide()
        self.groupBoxMove = QtWidgets.QGroupBox(MaszynaTuringa)
        self.groupBoxMove.setGeometry(QtCore.QRect(470, 20, 120, 91))
        self.groupBoxMove.setFlat(True)
        self.groupBoxMove.setCheckable(False)
        self.groupBoxMove.setObjectName("groupBoxMove")
        self.moveToLeftButton = QtWidgets.QRadioButton(self.groupBoxMove)
        self.moveToLeftButton.setGeometry(QtCore.QRect(0, 30, 100, 20))
        self.moveToLeftButton.setObjectName("moveToLeftButton")
        self.moveToRightButton = QtWidgets.QRadioButton(self.groupBoxMove)
        self.moveToRightButton.setGeometry(QtCore.QRect(0, 50, 100, 20))
        self.moveToRightButton.setObjectName("moveToRightButton")
        self.moveToNoWhere = QtWidgets.QRadioButton(self.groupBoxMove)
        self.moveToNoWhere.setGeometry(QtCore.QRect(0, 70, 100, 20))
        self.moveToNoWhere.setObjectName("moveToNoWhere")
        self.textStateBeforeEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textStateBeforeEditor.setGeometry(QtCore.QRect(40, 40, 81, 21))
        self.textStateBeforeEditor.setObjectName("textStateBeforeEditor")
        self.textStateBeforeEditor.hide()
        self.textCharBeforeEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textCharBeforeEditor.setGeometry(QtCore.QRect(140, 40, 81, 21))
        self.textCharBeforeEditor.setObjectName("textCharBeforeEditor")
        self.textCharBeforeEditor.hide()
        self.textStateAfterEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textStateAfterEditor.setGeometry(QtCore.QRect(240, 40, 81, 21))
        self.textStateAfterEditor.setObjectName("textStateAfterEditor")
        self.textStateAfterEditor.hide()
        self.textCharAfterEditor = QtWidgets.QLineEdit(MaszynaTuringa)
        self.textCharAfterEditor.setGeometry(QtCore.QRect(340, 40, 81, 21))
        self.textCharAfterEditor.setObjectName("textCharAfterEditor")
        self.textCharAfterEditor.hide()
        self.resultLabel = QtWidgets.QLabel(MaszynaTuringa)
        self.resultLabel.setGeometry(QtCore.QRect(30, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.resultLabel.setFont(font)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.resultText = QtWidgets.QLabel(MaszynaTuringa)
        self.resultText.setGeometry(QtCore.QRect(110, 340, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.resultText.setFont(font)
        self.resultText.setText("")
        self.resultText.setTextFormat(QtCore.Qt.AutoText)
        self.resultText.setObjectName("resultText")
        self.addAlphabet = QtWidgets.QPushButton(MaszynaTuringa)
        self.addAlphabet.setGeometry(QtCore.QRect(460, 110, 121, 61))
        self.addAlphabet.setObjectName("addAlphabet")
        self.pushButton = QtWidgets.QPushButton(MaszynaTuringa)
        self.pushButton.setGeometry(QtCore.QRect(140, 170, 181, 81))
        self.pushButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.addInputButton = QtWidgets.QPushButton(MaszynaTuringa)
        self.addInputButton.setGeometry(QtCore.QRect(460, 160, 121, 61))
        self.addInputButton.setObjectName("addInputButton")
        self.addInputButton.setEnabled(False)
        self.groupBox = QtWidgets.QGroupBox(MaszynaTuringa)
        self.groupBox.setGeometry(QtCore.QRect(40, 70, 381, 21))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.beginStateRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.beginStateRadioButton.setGeometry(QtCore.QRect(10, 0, 131, 20))
        self.beginStateRadioButton.setObjectName("beginStateRadioButton")
        self.statesRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.statesRadioButton.setGeometry(QtCore.QRect(140, 0, 111, 20))
        self.statesRadioButton.setObjectName("statesRadioButton")
        self.finishStateRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.finishStateRadioButton.setGeometry(QtCore.QRect(260, 0, 111, 20))
        self.finishStateRadioButton.setObjectName("finishStateRadioButton")
        self.resetButton = QtWidgets.QPushButton(MaszynaTuringa)
        self.resetButton.setGeometry(QtCore.QRect(460, 210, 121, 61))
        self.resetButton.setObjectName("resetButton")
        self.importFromFileButton = QtWidgets.QPushButton(MaszynaTuringa)
        self.importFromFileButton.setGeometry(QtCore.QRect(140, 130, 181, 32))
        self.importFromFileButton.setObjectName("importFromFileButton")
        self.importFromFileButton.setEnabled(False)
        self.nextButton = QtWidgets.QPushButton(MaszynaTuringa)
        self.nextButton.setGeometry(QtCore.QRect(490, 340, 113, 32))
        self.nextButton.setObjectName("nextButton")



        self.groupBoxMove.toggled.connect(lambda: self.btnstate())
        self.beginStateRadioButton.toggled.connect(lambda: self.showFieldsBegin())
        self.statesRadioButton.toggled.connect(lambda: self.showFieldsStates())
        self.finishStateRadioButton.toggled.connect(lambda: self.showFieldsFinish())

        self.retranslateUi(MaszynaTuringa)
        QtCore.QMetaObject.connectSlotsByName(MaszynaTuringa)



    def retranslateUi(self, MaszynaTuringa):
        _translate = QtCore.QCoreApplication.translate
        MaszynaTuringa.setWindowTitle(_translate("MaszynaTuringa", "Maszyna Turinga"))
        self.addState.setText(_translate("MaszynaTuringa", "Dodaj Stan"))
        self.labelStateBegin.setText(_translate("MaszynaTuringa", "Stan początkowy"))
        self.labelStateFinish.setText(_translate("MaszynaTuringa", "Stan końcowy"))
        self.labelStateBefore.setText(_translate("MaszynaTuringa", "Stan Przed"))
        self.labelStateAfter.setText(_translate("MaszynaTuringa", "Stan Po"))
        self.labelCharBefore.setText(_translate("MaszynaTuringa", "Znak Przed"))
        self.labelCharAfter.setText(_translate("MaszynaTuringa", "Znak Po"))
        self.groupBoxMove.setTitle(_translate("MaszynaTuringa", "Przejście"))
        self.moveToLeftButton.setText(_translate("MaszynaTuringa", "W lewo"))
        self.moveToRightButton.setText(_translate("MaszynaTuringa", "W prawo"))
        self.moveToNoWhere.setText(_translate("MaszynaTuringa", "W miejscu"))
        self.addAlphabet.setText(_translate("MaszynaTuringa", "Dodaj Alfabet"))
        self.pushButton.setText(_translate("MaszynaTuringa", "Start!"))
        self.addInputButton.setText(_translate("MaszynaTuringa", "Dodaj Wejście"))
        self.beginStateRadioButton.setText(_translate("MaszynaTuringa", "Stan początkowy"))
        self.statesRadioButton.setText(_translate("MaszynaTuringa", "Reszta Stanów"))
        self.finishStateRadioButton.setText(_translate("MaszynaTuringa", "Stan Końcowy"))
        self.resetButton.setText(_translate("MaszynaTuringa", "Reset"))
        self.importFromFileButton.setText(_translate("MaszynaTuringa", "Importuj z pliku..."))
        self.nextButton.setText(_translate("MaszynaTuringa", "Następny"))

    def checkIfTextFieldNotNone(self):
        if self.textStateBeforeEditor.text() is not u'' and self.textStateAfterEditor.text() is not u'':
            return True
        else:
            return False

    def checkIfTextBeginNotNone(self):
        if self.textStateBeginEditor.text() is not u'':
            return True
        else:
            return False

    def checkIfTextFinishNotNone(self):
        if self.textStateFinishEditor.text() is not u'':
            return True
        else:
            return False

    def cleanText(self):
        self.textStateBeforeEditor.setText('')
        self.textCharBeforeEditor.setText('')
        self.textStateAfterEditor.setText('')
        self.textCharAfterEditor.setText('')
        self.textStateBeginEditor.setText('')
        self.textStateFinishEditor.setText('')
        self.moveToRightButton.setChecked(False)
        self.moveToLeftButton.setChecked(False)
        self.moveToNoWhere.setChecked(False)

    def btnstate(self):
        if self.moveToRightButton.isChecked() == True:
            return 'R'
        elif self.moveToLeftButton.isChecked() == True:
            return 'L'
        elif self.moveToNoWhere.isChecked() == True:
            return 'N'

    def hideStates(self):
        self.labelStateBefore.hide()
        self.textStateBeforeEditor.hide()
        self.labelCharBefore.hide()
        self.textCharBeforeEditor.hide()
        self.labelStateAfter.hide()
        self.textStateAfterEditor.hide()
        self.labelCharAfter.hide()
        self.textCharAfterEditor.hide()

    def hideBegin(self):
        self.labelStateBegin.hide()
        self.textStateBeginEditor.hide()

    def hideFinish(self):
        self.labelStateFinish.hide()
        self.textStateFinishEditor.hide()



    def showFieldsBegin(self):
        self.hideStates()
        self.hideFinish()
        if self.beginStateRadioButton.isChecked() == True:
            self.labelStateBegin.show()
            self.textStateBeginEditor.show()

    def showFieldsStates(self):
        self.hideBegin()
        self.hideFinish()
        if self.statesRadioButton.isChecked() == True:
            self.labelStateBefore.show()
            self.textStateBeforeEditor.show()
            self.labelCharBefore.show()
            self.textCharBeforeEditor.show()
            self.labelStateAfter.show()
            self.textStateAfterEditor.show()
            self.labelCharAfter.show()
            self.textCharAfterEditor.show()

    def showFieldsFinish(self):
        self.hideStates()
        self.hideBegin()
        if self.finishStateRadioButton.isChecked() == True:
            self.labelStateFinish.show()
            self.textStateFinishEditor.show()






