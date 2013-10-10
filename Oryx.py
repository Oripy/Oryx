# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 12:30:55 2013

@author: pmaurier
"""

from PyQt4 import QtGui

from mainUI import Ui_MainWindow
import inventory
import search


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        
        self.setupUi(self)

        self.inventoryButton.clicked.connect(self.inventory)
        self.searchButton.clicked.connect(self.search)
        
        self.inventory_win = inventory.MainWindow()
        self.search_win = search.MainWindow()
        
    def inventory(self):
        """ show the inventory window maximized """
        self.inventory_win.showMaximized()
        self.inventory_win.activateWindow()
        
    def search(self):
        """ show the search window maximized """
        self.search_win.showMaximized()
        self.search_win.activateWindow()
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())