#!/usr/bin/env python

import splash, method, last, fubi, downloader
from PyQt4 import QtCore, QtGui
import sys
import os

class Fubi(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = splash.Ui_MainWindow()
        self.ui.setupUi(self)

    def splashNext(self):
        self.method_dialog = method.Ui_Dialog()
        self.method_dialog.setupUi(self)

        #keep a list of dialogs also
        self.dialogs = [self.method_dialog]

        self.hideAll()
        self.method_dialog.show_()
        
    def hideAll(self):
        for dialog in gui.dialogs:
            dialog.hide()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Fubi()
    myapp.show()
    sys.exit(app.exec_())
