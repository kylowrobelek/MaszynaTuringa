import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLabel
from PyQt5.QtCore import pyqtSlot
from TransitionWindow import Ui_TransitionWindow

class TransitionWindow(QDialog):

    count = 0

    def __init__(self):
        super(TransitionWindow, self).__init__()
        self.ui = Ui_TransitionWindow()
        self.ui.setupUi(self)


    #def addToTableBeginState(self, beginState):
        #label = QLabel()
       #self.ui.


    def addToTableStates(self, stateBefore, charBefore, stateAfter, charAfter, moveLeftRight):
        labelStateBefore = QLabel(stateBefore)
        labelCharBefore = QLabel(charBefore)
        labelStateAfter = QLabel(stateAfter)
        labelCharAfter = QLabel(charAfter)
        labelMoveLeftRight = QLabel(moveLeftRight)

        self.ui.gridStateBefore.addWidget(labelStateBefore, self.count, 0)
        self.ui.gridCharBefore.addWidget(labelCharBefore, self.count, 0)
        self.ui.gridStateAfter.addWidget(labelStateAfter, self.count, 0)
        self.ui.gridCharAfter.addWidget(labelCharAfter, self.count, 0)
        self.ui.gridMove.addWidget(labelMoveLeftRight, self.count,0)

        self.count += 1





    #def addToTableFinishState(self, finishState):
