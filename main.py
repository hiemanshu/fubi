#!/usr/bin/env python

import last, wizard 
from PyQt4 import QtCore, QtGui
import sys
import os

class Fubi(QtGui.QWizard):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = wizard.Ui_Wizard()
        self.ui.setupUi(self)
        self.postSetup()

    def postSetup(self):
        print 'yeah Blah Blah'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Fubi()
    myapp.show()
    sys.exit(app.exec_())
