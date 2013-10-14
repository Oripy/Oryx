# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 10:34:38 2013

@author: pmaurier
"""

from PyQt4 import QtGui

from generatorUI import Ui_MainWindow
import hashlib
from codecs import encode

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
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
            coded_pass = hashlib.sha512(encode(password,
                                               'rot13')).hexdigest()[5:69]
            self.resultLabel.setText(coded_pass)
    
    def copy(self):
        coded_pass = self.resultLabel.text()
        if coded_pass != '':
            app.clipboard().setText(coded_pass)
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())