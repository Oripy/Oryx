# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Oct 13 09:58:11 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(633, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("glasses.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.searchButton.setFont(font)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout_2.addWidget(self.searchButton, 3, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        self.inventoryButton = QtGui.QPushButton(self.centralwidget)
        self.inventoryButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.inventoryButton.setFont(font)
        self.inventoryButton.setAutoDefault(True)
        self.inventoryButton.setObjectName(_fromUtf8("inventoryButton"))
        self.gridLayout_2.addWidget(self.inventoryButton, 3, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.passwordEdit = QtGui.QLineEdit(self.centralwidget)
        self.passwordEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEdit.setObjectName(_fromUtf8("passwordEdit"))
        self.horizontalLayout.addWidget(self.passwordEdit)
        self.passwordButton = QtGui.QPushButton(self.centralwidget)
        self.passwordButton.setDefault(True)
        self.passwordButton.setObjectName(_fromUtf8("passwordButton"))
        self.horizontalLayout.addWidget(self.passwordButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 5, 0, 1, 3)
        self.timerLabel = QtGui.QLabel(self.centralwidget)
        self.timerLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timerLabel.setObjectName(_fromUtf8("timerLabel"))
        self.gridLayout_2.addWidget(self.timerLabel, 5, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.passwordEdit, self.passwordButton)
        MainWindow.setTabOrder(self.passwordButton, self.inventoryButton)
        MainWindow.setTabOrder(self.inventoryButton, self.searchButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Oryx", None))
        self.searchButton.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Oryx Optical DBMS</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Eyeglasses Inventory for Humanitarian Purposes</span></p></body></html>", None))
        self.inventoryButton.setText(_translate("MainWindow", "Inventory", None))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "mot de passe", None))
        self.passwordButton.setText(_translate("MainWindow", "OK", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>an XL-ant software by <a href=\"mailto:pierre.maurier@gadz.org?subject=Support%20Oryx\"><span style=\" text-decoration: underline; color:#0000ff;\">Pierre Maurier</span></a></p></body></html>", None))
        self.timerLabel.setText(_translate("MainWindow", "00:00", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

