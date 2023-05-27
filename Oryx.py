# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 12:30:55 2013

@author: pmaurier
"""

from PyQt5 import QtCore, QtGui, QtWidgets, uic

import os, sys
import machineid
# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Ui_MainWindow = uic.loadUiType(resource_path('main.ui'))[0]
# from mainUI import Ui_MainWindow

import inventory
import search
import hashlib
from codecs import encode
import time

from config import PASSWORD

passwords = QtCore.QSettings("XL-ant", "Oryx")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)

        self.inventory_win = inventory.MainWindow()
        self.search_win = search.MainWindow()

        self.inventoryButton.clicked.connect(self.inventory)
        self.inventory_win.searchWindowButton.clicked.connect(self.search)
        self.searchButton.clicked.connect(self.search)
        self.search_win.inventoryWindowButton.clicked.connect(self.inventory)

        self.passwordButton.clicked.connect(self.unlock)
        self.passwordEdit.returnPressed.connect(self.unlock)

        self.showPasswordCheckBox.stateChanged.connect(self.showHidePassword)

        self.computerIDLabel.setText(str(machineid.hashed_id('oryx')[:10]))

        self.copyComputerIDButton.clicked.connect(self.copyComputerID)

        self.showHidePassword()

        self.start_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateClock)

    def closeEvent(self, event):
        """ Reimplementation of the closeEvent to close all windows """
        if self.inventory_win.close() and self.search_win.close():
            event.accept()
        else:
            event.ignore()

    def inventory(self):
        """ show the inventory window maximized """
        self.inventory_win.data = self.inventory_win.loadDataFromCsv()
        self.inventory_win.displayData(self.inventory_win.data)
        self.inventory_win.setWindowFlags(self.inventory_win.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
        self.inventory_win.showMaximized()
        self.inventory_win.activateWindow()
        self.inventory_win.setWindowFlags(self.inventory_win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

    def search(self):
        """ show the search window maximized """
        self.search_win.setWindowFlags(self.search_win.windowFlags() & QtCore.Qt.WindowStaysOnTopHint)
        self.search_win.showMaximized()
        self.search_win.activateWindow()
        self.search_win.setWindowFlags(self.search_win.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)

    def unlock(self):
        """ Test the password and unlock if successful """
        password = self.passwordEdit.text()
        if password != '':
            coded_pass = hashlib.sha512(encode(encode(f'''{password}{machineid.hashed_id('oryx')[:10]}''',
                                               'rot13'),'utf-8')).hexdigest()[5:69]
            coded_pass_master = hashlib.sha512(encode(encode(password,
                                               'rot13'),'utf-8')).hexdigest()[5:69]
            if coded_pass_master == 'd4253200d60b1008f1aad559cd3fac59352d7585516496f6f571fbb026b3e44a':
                self.searchButton.setEnabled(True)
                self.inventoryButton.setEnabled(True)
                self.passwordEdit.setPlaceholderText('Mot de passe principal')
            elif coded_pass == PASSWORD:
                self.time_remaining = int(passwords.value(coded_pass, 333*60*60))
                self.start_time = time.time()
                self.timer.start(10000)
                self.updateClock()
                if self.time_remaining > 0:
                    self.searchButton.setEnabled(True)
                    self.inventoryButton.setEnabled(True)
                    self.passwordEdit.setPlaceholderText('Mot de passe OK')
                    t = self.time_remaining
                    hours = t // 3600
                    minutes = (t - hours * 3600) // 60
                    self.timerLabel.setText('%d:%02d' % (hours, minutes))
                else:
                    self.passwordEdit.setPlaceholderText('Temps écoulé')
            else:
                self.timer.stop()
                self.searchButton.setEnabled(False)
                self.inventoryButton.setEnabled(False)
                self.passwordEdit.setFocus()
                self.passwordEdit.setPlaceholderText('Mauvais mot de passe')
            self.passwordEdit.setText('')

    def updateClock(self):
        """ Updates the display of time remaining
            and updates the stored value """
        time_now = time.time()
        delta = int(time_now - self.start_time)
        if delta > 0:
            t = self.time_remaining - delta
            hours = t // 3600
            minutes = (t - hours * 3600) // 60
            self.timerLabel.setText('%d:%02d' % (hours, minutes))
            self.time_remaining = t
            self.start_time = time_now
            passwords.setValue(PASSWORD, t)

    def showHidePassword(self):
        """ Show or hide password depending on the state of the checkbox """
        if self.showPasswordCheckBox.isChecked():
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def copyComputerID(self):
        cb = QtWidgets.QApplication.clipboard()
        cb.setText(self.computerIDLabel.text())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())
