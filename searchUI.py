# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchUI.ui'
#
# Created: Sat Aug  3 08:28:23 2013
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.tableView, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.childRadioNone = QtGui.QRadioButton(self.groupBox_4)
        self.childRadioNone.setChecked(True)
        self.childRadioNone.setObjectName(_fromUtf8("childRadioNone"))
        self.verticalLayout_3.addWidget(self.childRadioNone)
        self.childRadioNo = QtGui.QRadioButton(self.groupBox_4)
        self.childRadioNo.setObjectName(_fromUtf8("childRadioNo"))
        self.verticalLayout_3.addWidget(self.childRadioNo)
        self.childRadioYes = QtGui.QRadioButton(self.groupBox_4)
        self.childRadioYes.setObjectName(_fromUtf8("childRadioYes"))
        self.verticalLayout_3.addWidget(self.childRadioYes)
        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.addGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.addGroupBox.setObjectName(_fromUtf8("addGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.addGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addRadioNone = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioNone.setChecked(True)
        self.addRadioNone.setObjectName(_fromUtf8("addRadioNone"))
        self.verticalLayout_2.addWidget(self.addRadioNone)
        self.addRadioP = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioP.setObjectName(_fromUtf8("addRadioP"))
        self.verticalLayout_2.addWidget(self.addRadioP)
        self.addRadioBF = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioBF.setObjectName(_fromUtf8("addRadioBF"))
        self.verticalLayout_2.addWidget(self.addRadioBF)
        self.addRadioTF = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioTF.setObjectName(_fromUtf8("addRadioTF"))
        self.verticalLayout_2.addWidget(self.addRadioTF)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addWidget(self.addGroupBox)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.solarRadioNone = QtGui.QRadioButton(self.groupBox_5)
        self.solarRadioNone.setChecked(True)
        self.solarRadioNone.setObjectName(_fromUtf8("solarRadioNone"))
        self.verticalLayout_4.addWidget(self.solarRadioNone)
        self.solarRadioNo = QtGui.QRadioButton(self.groupBox_5)
        self.solarRadioNo.setObjectName(_fromUtf8("solarRadioNo"))
        self.verticalLayout_4.addWidget(self.solarRadioNo)
        self.solarRadioYes = QtGui.QRadioButton(self.groupBox_5)
        self.solarRadioYes.setObjectName(_fromUtf8("solarRadioYes"))
        self.verticalLayout_4.addWidget(self.solarRadioYes)
        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.rSphereSpin = dotSpinBox(self.groupBox)
        self.rSphereSpin.setObjectName(_fromUtf8("rSphereSpin"))
        self.gridLayout.addWidget(self.rSphereSpin, 1, 0, 1, 1)
        self.rCylSpin = negativeZeroSpinBox(self.groupBox)
        self.rCylSpin.setObjectName(_fromUtf8("rCylSpin"))
        self.gridLayout.addWidget(self.rCylSpin, 1, 1, 1, 1)
        self.rAddSpin = dotSpinBox(self.groupBox)
        self.rAddSpin.setObjectName(_fromUtf8("rAddSpin"))
        self.gridLayout.addWidget(self.rAddSpin, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.rLinkCheckbox = QtGui.QCheckBox(self.groupBox)
        self.rLinkCheckbox.setObjectName(_fromUtf8("rLinkCheckbox"))
        self.gridLayout.addWidget(self.rLinkCheckbox, 2, 3, 1, 1)
        self.rAxisSpin = angleSpinBox(self.groupBox)
        self.rAxisSpin.setObjectName(_fromUtf8("rAxisSpin"))
        self.gridLayout.addWidget(self.rAxisSpin, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.lSphereSpin = dotSpinBox(self.groupBox_2)
        self.lSphereSpin.setObjectName(_fromUtf8("lSphereSpin"))
        self.gridLayout_2.addWidget(self.lSphereSpin, 1, 0, 1, 1)
        self.lCylSpin = negativeZeroSpinBox(self.groupBox_2)
        self.lCylSpin.setObjectName(_fromUtf8("lCylSpin"))
        self.gridLayout_2.addWidget(self.lCylSpin, 1, 1, 1, 1)
        self.lAddSpin = dotSpinBox(self.groupBox_2)
        self.lAddSpin.setObjectName(_fromUtf8("lAddSpin"))
        self.gridLayout_2.addWidget(self.lAddSpin, 1, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.lLinkCheckbox = QtGui.QCheckBox(self.groupBox_2)
        self.lLinkCheckbox.setObjectName(_fromUtf8("lLinkCheckbox"))
        self.gridLayout_2.addWidget(self.lLinkCheckbox, 2, 3, 1, 1)
        self.lAxisSpin = angleSpinBox(self.groupBox_2)
        self.lAxisSpin.setObjectName(_fromUtf8("lAxisSpin"))
        self.gridLayout_2.addWidget(self.lAxisSpin, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.searchAction = QtGui.QAction(MainWindow)
        self.searchAction.setObjectName(_fromUtf8("searchAction"))
        self.menuFichier.addAction(self.searchAction)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.exitAction)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chercher", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Monture", None))
        self.childRadioNone.setText(_translate("MainWindow", "Indifférent", None))
        self.childRadioNo.setText(_translate("MainWindow", "Adulte", None))
        self.childRadioYes.setText(_translate("MainWindow", "Enfant", None))
        self.addGroupBox.setTitle(_translate("MainWindow", "Addition", None))
        self.addRadioNone.setText(_translate("MainWindow", "Indifférent", None))
        self.addRadioP.setText(_translate("MainWindow", "Progressif", None))
        self.addRadioBF.setText(_translate("MainWindow", "Bifocal", None))
        self.addRadioTF.setText(_translate("MainWindow", "Trifocal", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Teinte", None))
        self.solarRadioNone.setText(_translate("MainWindow", "Indifférent", None))
        self.solarRadioNo.setText(_translate("MainWindow", "Non teinté (T1, T2)", None))
        self.solarRadioYes.setText(_translate("MainWindow", "Solaire (T3, T4)", None))
        self.searchButton.setText(_translate("MainWindow", "Chercher", None))
        self.groupBox.setTitle(_translate("MainWindow", "Œil Droit", None))
        self.label_2.setText(_translate("MainWindow", "Cylindre", None))
        self.label.setText(_translate("MainWindow", "Sphere", None))
        self.label_4.setText(_translate("MainWindow", "Addition", None))
        self.label_3.setText(_translate("MainWindow", "Axe", None))
        self.rLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Œil Gauche", None))
        self.label_5.setText(_translate("MainWindow", "Cylindre", None))
        self.label_6.setText(_translate("MainWindow", "Sphere", None))
        self.label_7.setText(_translate("MainWindow", "Addition", None))
        self.label_8.setText(_translate("MainWindow", "Axe", None))
        self.lLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.exitAction.setText(_translate("MainWindow", "Quitter", None))
        self.searchAction.setText(_translate("MainWindow", "Chercher", None))

from anglespinbox import angleSpinBox
from negativezerospinbox import negativeZeroSpinBox
from dotspinbox import dotSpinBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

