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

    def add_to_table_states(self, stateBefore, charBefore, stateAfter, charAfter, moveLeftRight):
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

    def clear_table(self):
        for i in reversed(range(self.ui.gridStateBefore.count())):
            self.ui.gridStateBefore.itemAt(i).widget().setParent(None)
            self.ui.gridCharBefore.itemAt(i).widget().setParent(None)
            self.ui.gridStateAfter.itemAt(i).widget().setParent(None)
            self.ui.gridCharAfter.itemAt(i).widget().setParent(None)
            self.ui.gridMove.itemAt(i).widget().setParent(None)