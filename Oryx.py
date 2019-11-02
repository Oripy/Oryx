# -*- coding: utf-8 -*-
"""
Created on Thu Oct 03 12:30:55 2013

@author: pmaurier
"""

from PyQt5 import QtCore, QtGui, QtWidgets, uic

from mainUI import Ui_MainWindow
# Ui_MainWindow = uic.loadUiType(os.path.join(basedir, "main.ui"))[0]

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

        self.inventoryButton.clicked.connect(self.inventory)
        self.searchButton.clicked.connect(self.search)

        self.inventory_win = inventory.MainWindow()
        self.search_win = search.MainWindow()

        self.passwordButton.clicked.connect(self.unlock)
        self.passwordEdit.returnPressed.connect(self.unlock)

        self.showPasswordCheckBox.stateChanged.connect(self.showHidePassword)

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
        self.inventory_win.showMaximized()
        self.inventory_win.activateWindow()

    def search(self):
        """ show the search window maximized """
        self.search_win.showMaximized()
        self.search_win.activateWindow()

    def unlock(self):
        """ Test the password and unlock if successful """
        password = self.passwordEdit.text()
        if password != '':
            coded_pass = hashlib.sha512(encode(encode(password,
                                               'rot13'),'utf-8')).hexdigest()[5:69]
#            print coded_pass, len(coded_pass)
            if coded_pass == 'd4253200d60b1008f1aad559cd3fac59352d7585516496f6f571fbb026b3e44a':
                self.searchButton.setEnabled(True)
                self.inventoryButton.setEnabled(True)
                self.passwordEdit.setPlaceholderText('Mot de passe principal')
            elif coded_pass == PASSWORD:
                self.time_remaining = passwords.value(coded_pass, 300*60*60)
                self.start_time = time.time()
                self.timer.start(10000)
                self.updateClock()
                if self.time_remaining > 0:
                    self.searchButton.setEnabled(True)
                    self.inventoryButton.setEnabled(True)
                    self.passwordEdit.setPlaceholderText('Mot de passe OK')
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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec_())
