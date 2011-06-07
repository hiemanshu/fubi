#!/usr/bin/env python

import splash, method, last, fubi, downloader
from PyQt4 import QtCore, QtGui
import sys
import os

class Fubi(splash.Ui_MainWindow):
    def __init__(self, parent=None):
        splash.Ui_MainWindow.__init__(self, parent)
        self.setupUi()

	self.method_dialog = method.Ui_Dialog()
	self.method_dialog.setupUi(self)

	#keep a list of dialogs also
	self.dialogs = [self.method_dialog]

    def splashNext(self):
	self.hideAll()
        self.method_dialog.show_()

    def hideAll(self):
	for dialog in self.dialogs:
		dialog.hide()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Fubi()
    myapp.show()
    sys.exit(app.exec_())
