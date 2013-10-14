# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator.ui'
#
# Created: Mon Oct 14 10:53:58 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 80))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inputEdit = QtGui.QLineEdit(self.centralwidget)
        self.inputEdit.setObjectName(_fromUtf8("inputEdit"))
        self.gridLayout.addWidget(self.inputEdit, 0, 0, 1, 1)
        self.generateButton = QtGui.QPushButton(self.centralwidget)
        self.generateButton.setDefault(True)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.gridLayout.addWidget(self.generateButton, 0, 1, 1, 1)
        self.resultLabel = QtGui.QLabel(self.centralwidget)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.gridLayout.addWidget(self.resultLabel, 1, 0, 1, 1)
        self.copyButton = QtGui.QPushButton(self.centralwidget)
        self.copyButton.setAutoDefault(True)
        self.copyButton.setObjectName(_fromUtf8("copyButton"))
        self.gridLayout.addWidget(self.copyButton, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Oryx license generator", None, QtGui.QApplication.UnicodeUTF8))
        self.inputEdit.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "mot de passe", None, QtGui.QApplication.UnicodeUTF8))
        self.generateButton.setText(QtGui.QApplication.translate("MainWindow", "Générer", None, QtGui.QApplication.UnicodeUTF8))
        self.copyButton.setText(QtGui.QApplication.translate("MainWindow", "Copier", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

