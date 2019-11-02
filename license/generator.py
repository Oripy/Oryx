# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:34:38 2013

@author: pmaurier
"""

from PyQt5 import QtWidgets, uic

import os
# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Ui_MainWindow = uic.loadUiType(resource_path('generator.ui'))[0]
# from generatorUI import Ui_MainWindow

import hashlib
from codecs import encode

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)

        self.generateButton.clicked.connect(self.generate)
        self.inputEdit.returnPressed.connect(self.generate)

        self.copyButton.clicked.connect(self.copy)

    def generate(self):
        password = self.inputEdit.text()
        if password != '':
            coded_pass = hashlib.sha512(encode(encode(password,
                                               'rot13'),'utf-8')).hexdigest()[5:69]
            self.resultLabel.setText(coded_pass)

    def copy(self):
        coded_pass = self.resultLabel.text()
        if coded_pass != '':
            app.clipboard().setText(coded_pass)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
