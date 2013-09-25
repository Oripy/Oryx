# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created: Thu Sep 26 20:12:23 2013
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
        MainWindow.resize(788, 636)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setSpacing(6)
        self.mainLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.numberingLayout = QtGui.QHBoxLayout()
        self.numberingLayout.setObjectName(_fromUtf8("numberingLayout"))
        self.eyeglassesNum = QtGui.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eyeglassesNum.setFont(font)
        self.eyeglassesNum.setMinimum(1)
        self.eyeglassesNum.setMaximum(1000000)
        self.eyeglassesNum.setProperty("value", 1)
        self.eyeglassesNum.setObjectName(_fromUtf8("eyeglassesNum"))
        self.numberingLayout.addWidget(self.eyeglassesNum)
        self.status = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName(_fromUtf8("status"))
        self.numberingLayout.addWidget(self.status)
        self.newButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.newButton.setFont(font)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.numberingLayout.addWidget(self.newButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.numberingLayout.addWidget(self.saveButton)
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.numberingLayout.addWidget(self.deleteButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.numberingLayout.addItem(spacerItem)
        self.backupButton = QtGui.QPushButton(self.centralwidget)
        self.backupButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.backupButton.setObjectName(_fromUtf8("backupButton"))
        self.numberingLayout.addWidget(self.backupButton)
        self.restoreButton = QtGui.QPushButton(self.centralwidget)
        self.restoreButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        self.numberingLayout.addWidget(self.restoreButton)
        self.mainLayout.addLayout(self.numberingLayout)
        self.eyesLayout = QtGui.QHBoxLayout()
        self.eyesLayout.setObjectName(_fromUtf8("eyesLayout"))
        self.rightEyeGroupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rightEyeGroupBox.setFont(font)
        self.rightEyeGroupBox.setObjectName(_fromUtf8("rightEyeGroupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.rightEyeGroupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.rightEyeLayout = QtGui.QGridLayout()
        self.rightEyeLayout.setObjectName(_fromUtf8("rightEyeLayout"))
        self.label_2 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rightEyeLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.rightEyeLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.rightEyeLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.rAxisSpin = angleSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rAxisSpin.setFont(font)
        self.rAxisSpin.setWrapping(True)
        self.rAxisSpin.setMinimum(5)
        self.rAxisSpin.setMaximum(180)
        self.rAxisSpin.setSingleStep(5)
        self.rAxisSpin.setProperty("value", 180)
        self.rAxisSpin.setObjectName(_fromUtf8("rAxisSpin"))
        self.rightEyeLayout.addWidget(self.rAxisSpin, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.rightEyeLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.rLinkCheckbox = QtGui.QCheckBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rLinkCheckbox.setFont(font)
        self.rLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rLinkCheckbox.setObjectName(_fromUtf8("rLinkCheckbox"))
        self.rightEyeLayout.addWidget(self.rLinkCheckbox, 2, 3, 1, 1)
        self.rAddSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rAddSpin.setFont(font)
        self.rAddSpin.setObjectName(_fromUtf8("rAddSpin"))
        self.rightEyeLayout.addWidget(self.rAddSpin, 1, 3, 1, 1)
        self.rCylSpin = negativeZeroSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rCylSpin.setFont(font)
        self.rCylSpin.setObjectName(_fromUtf8("rCylSpin"))
        self.rightEyeLayout.addWidget(self.rCylSpin, 1, 1, 1, 1)
        self.rSphereSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rSphereSpin.setFont(font)
        self.rSphereSpin.setObjectName(_fromUtf8("rSphereSpin"))
        self.rightEyeLayout.addWidget(self.rSphereSpin, 1, 0, 1, 1)
        self.rLabelCylPos = QtGui.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rLabelCylPos.setFont(font)
        self.rLabelCylPos.setObjectName(_fromUtf8("rLabelCylPos"))
        self.rightEyeLayout.addWidget(self.rLabelCylPos, 2, 1, 1, 1)
        self.gridLayout_7.addLayout(self.rightEyeLayout, 0, 0, 1, 1)
        self.eyesLayout.addWidget(self.rightEyeGroupBox)
        self.leftEyeGroupBox = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftEyeGroupBox.setFont(font)
        self.leftEyeGroupBox.setObjectName(_fromUtf8("leftEyeGroupBox"))
        self.gridLayout_8 = QtGui.QGridLayout(self.leftEyeGroupBox)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.leftEyeLayout = QtGui.QGridLayout()
        self.leftEyeLayout.setObjectName(_fromUtf8("leftEyeLayout"))
        self.label_8 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.leftEyeLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.leftEyeLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.leftEyeLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.lAxisSpin = angleSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAxisSpin.setFont(font)
        self.lAxisSpin.setWrapping(True)
        self.lAxisSpin.setMinimum(5)
        self.lAxisSpin.setMaximum(180)
        self.lAxisSpin.setSingleStep(5)
        self.lAxisSpin.setProperty("value", 180)
        self.lAxisSpin.setObjectName(_fromUtf8("lAxisSpin"))
        self.leftEyeLayout.addWidget(self.lAxisSpin, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.leftEyeLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.lLinkCheckbox = QtGui.QCheckBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lLinkCheckbox.setFont(font)
        self.lLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lLinkCheckbox.setObjectName(_fromUtf8("lLinkCheckbox"))
        self.leftEyeLayout.addWidget(self.lLinkCheckbox, 2, 3, 1, 1)
        self.lSphereSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lSphereSpin.setFont(font)
        self.lSphereSpin.setObjectName(_fromUtf8("lSphereSpin"))
        self.leftEyeLayout.addWidget(self.lSphereSpin, 1, 0, 1, 1)
        self.lCylSpin = negativeZeroSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lCylSpin.setFont(font)
        self.lCylSpin.setObjectName(_fromUtf8("lCylSpin"))
        self.leftEyeLayout.addWidget(self.lCylSpin, 1, 1, 1, 1)
        self.lAddSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAddSpin.setFont(font)
        self.lAddSpin.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.lAddSpin.setObjectName(_fromUtf8("lAddSpin"))
        self.leftEyeLayout.addWidget(self.lAddSpin, 1, 3, 1, 1)
        self.lLabelCylPos = QtGui.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lLabelCylPos.setFont(font)
        self.lLabelCylPos.setObjectName(_fromUtf8("lLabelCylPos"))
        self.leftEyeLayout.addWidget(self.lLabelCylPos, 2, 1, 1, 1)
        self.gridLayout_8.addLayout(self.leftEyeLayout, 0, 0, 1, 1)
        self.eyesLayout.addWidget(self.leftEyeGroupBox)
        self.mainLayout.addLayout(self.eyesLayout)
        self.otherLayout = QtGui.QHBoxLayout()
        self.otherLayout.setObjectName(_fromUtf8("otherLayout"))
        self.optionsLayout = QtGui.QVBoxLayout()
        self.optionsLayout.setObjectName(_fromUtf8("optionsLayout"))
        self.addGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.addGroupBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addGroupBox.sizePolicy().hasHeightForWidth())
        self.addGroupBox.setSizePolicy(sizePolicy)
        self.addGroupBox.setObjectName(_fromUtf8("addGroupBox"))
        self.gridLayout_9 = QtGui.QGridLayout(self.addGroupBox)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.addLayout = QtGui.QVBoxLayout()
        self.addLayout.setObjectName(_fromUtf8("addLayout"))
        self.addRadioP = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioP.setChecked(True)
        self.addRadioP.setObjectName(_fromUtf8("addRadioP"))
        self.addLayout.addWidget(self.addRadioP)
        self.addRadioBF = QtGui.QRadioButton(self.addGroupBox)
        self.addRadioBF.setObjectName(_fromUtf8("addRadioBF"))
        self.addLayout.addWidget(self.addRadioBF)
        self.gridLayout_9.addLayout(self.addLayout, 1, 0, 1, 1)
        self.optionsLayout.addWidget(self.addGroupBox)
        self.childGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.childGroupBox.sizePolicy().hasHeightForWidth())
        self.childGroupBox.setSizePolicy(sizePolicy)
        self.childGroupBox.setObjectName(_fromUtf8("childGroupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.childGroupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.childRadioYes = QtGui.QRadioButton(self.childGroupBox)
        self.childRadioYes.setObjectName(_fromUtf8("childRadioYes"))
        self.gridLayout_5.addWidget(self.childRadioYes, 4, 0, 1, 1)
        self.childRadioNo = QtGui.QRadioButton(self.childGroupBox)
        self.childRadioNo.setChecked(True)
        self.childRadioNo.setObjectName(_fromUtf8("childRadioNo"))
        self.gridLayout_5.addWidget(self.childRadioNo, 3, 0, 1, 1)
        self.childRadioHalf = QtGui.QRadioButton(self.childGroupBox)
        self.childRadioHalf.setObjectName(_fromUtf8("childRadioHalf"))
        self.gridLayout_5.addWidget(self.childRadioHalf, 5, 0, 1, 1)
        self.optionsLayout.addWidget(self.childGroupBox)
        self.solarGroupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solarGroupBox.sizePolicy().hasHeightForWidth())
        self.solarGroupBox.setSizePolicy(sizePolicy)
        self.solarGroupBox.setObjectName(_fromUtf8("solarGroupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.solarGroupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.solarRadioNo = QtGui.QRadioButton(self.solarGroupBox)
        self.solarRadioNo.setChecked(True)
        self.solarRadioNo.setObjectName(_fromUtf8("solarRadioNo"))
        self.gridLayout_6.addWidget(self.solarRadioNo, 0, 0, 1, 1)
        self.solarRadioYes = QtGui.QRadioButton(self.solarGroupBox)
        self.solarRadioYes.setObjectName(_fromUtf8("solarRadioYes"))
        self.gridLayout_6.addWidget(self.solarRadioYes, 1, 0, 1, 1)
        self.optionsLayout.addWidget(self.solarGroupBox)
        self.otherLayout.addLayout(self.optionsLayout)
        self.commentLayout = QtGui.QVBoxLayout()
        self.commentLayout.setObjectName(_fromUtf8("commentLayout"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.commentLayout.addWidget(self.label_10)
        self.commentEdit = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentEdit.sizePolicy().hasHeightForWidth())
        self.commentEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.commentEdit.setFont(font)
        self.commentEdit.setTabChangesFocus(True)
        self.commentEdit.setBackgroundVisible(False)
        self.commentEdit.setObjectName(_fromUtf8("commentEdit"))
        self.commentLayout.addWidget(self.commentEdit)
        self.otherLayout.addLayout(self.commentLayout)
        self.mainLayout.addLayout(self.otherLayout)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.mainLayout.addWidget(self.tableView)
        self.gridLayout_3.addLayout(self.mainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.newAction = QtGui.QAction(MainWindow)
        self.newAction.setObjectName(_fromUtf8("newAction"))
        self.saveAction = QtGui.QAction(MainWindow)
        self.saveAction.setObjectName(_fromUtf8("saveAction"))
        self.exitAction = QtGui.QAction(MainWindow)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.backupAction = QtGui.QAction(MainWindow)
        self.backupAction.setObjectName(_fromUtf8("backupAction"))
        self.restoreAction = QtGui.QAction(MainWindow)
        self.restoreAction.setObjectName(_fromUtf8("restoreAction"))
        self.deleteAction = QtGui.QAction(MainWindow)
        self.deleteAction.setObjectName(_fromUtf8("deleteAction"))
        self.printAction = QtGui.QAction(MainWindow)
        self.printAction.setObjectName(_fromUtf8("printAction"))
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.deleteAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.backupAction)
        self.fileMenu.addAction(self.restoreAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.printAction)
        self.fileMenu.addAction(self.exitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.newButton, self.eyeglassesNum)
        MainWindow.setTabOrder(self.eyeglassesNum, self.rSphereSpin)
        MainWindow.setTabOrder(self.rSphereSpin, self.rCylSpin)
        MainWindow.setTabOrder(self.rCylSpin, self.rAxisSpin)
        MainWindow.setTabOrder(self.rAxisSpin, self.rAddSpin)
        MainWindow.setTabOrder(self.rAddSpin, self.lSphereSpin)
        MainWindow.setTabOrder(self.lSphereSpin, self.lCylSpin)
        MainWindow.setTabOrder(self.lCylSpin, self.lAxisSpin)
        MainWindow.setTabOrder(self.lAxisSpin, self.lAddSpin)
        MainWindow.setTabOrder(self.lAddSpin, self.addRadioP)
        MainWindow.setTabOrder(self.addRadioP, self.addRadioBF)
        MainWindow.setTabOrder(self.addRadioBF, self.childRadioNo)
        MainWindow.setTabOrder(self.childRadioNo, self.childRadioYes)
        MainWindow.setTabOrder(self.childRadioYes, self.childRadioHalf)
        MainWindow.setTabOrder(self.childRadioHalf, self.solarRadioNo)
        MainWindow.setTabOrder(self.solarRadioNo, self.solarRadioYes)
        MainWindow.setTabOrder(self.solarRadioYes, self.commentEdit)
        MainWindow.setTabOrder(self.commentEdit, self.saveButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Oryx Optical DBSM - Inventory", None))
        self.status.setText(_translate("MainWindow", "Empty", None))
        self.newButton.setText(_translate("MainWindow", "Nouvelle paire", None))
        self.saveButton.setText(_translate("MainWindow", "Enregistrer", None))
        self.deleteButton.setText(_translate("MainWindow", "Supprimer", None))
        self.backupButton.setText(_translate("MainWindow", "Backup", None))
        self.restoreButton.setText(_translate("MainWindow", "Restaurer", None))
        self.rightEyeGroupBox.setTitle(_translate("MainWindow", "OD (Œil Droit)", None))
        self.label_2.setText(_translate("MainWindow", "Sphere", None))
        self.label_5.setText(_translate("MainWindow", "Addition", None))
        self.label_4.setText(_translate("MainWindow", "Axe", None))
        self.label_3.setText(_translate("MainWindow", "Cylindre", None))
        self.rLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.rLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Sauvegarde", None))
        self.rLabelCylPos.setText(_translate("MainWindow", "Cylindre positif", None))
        self.leftEyeGroupBox.setTitle(_translate("MainWindow", "OG (Œil Gauche)", None))
        self.label_8.setText(_translate("MainWindow", "Axe", None))
        self.label_9.setText(_translate("MainWindow", "Cylindre", None))
        self.label_6.setText(_translate("MainWindow", "Sphere", None))
        self.label_7.setText(_translate("MainWindow", "Addition", None))
        self.lLinkCheckbox.setText(_translate("MainWindow", "Lié", None))
        self.lLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Sauvegarde", None))
        self.lLabelCylPos.setText(_translate("MainWindow", "Cylindre positif", None))
        self.addGroupBox.setTitle(_translate("MainWindow", "Multifocal", None))
        self.addRadioP.setText(_translate("MainWindow", "Progressif", None))
        self.addRadioBF.setText(_translate("MainWindow", "Bifocal", None))
        self.childGroupBox.setTitle(_translate("MainWindow", "Monture", None))
        self.childRadioYes.setText(_translate("MainWindow", "Enfant", None))
        self.childRadioNo.setText(_translate("MainWindow", "Adulte", None))
        self.childRadioHalf.setText(_translate("MainWindow", "Demi-lune", None))
        self.solarGroupBox.setTitle(_translate("MainWindow", "Teinte", None))
        self.solarRadioNo.setText(_translate("MainWindow", "Non teinté (ou T1, T2)", None))
        self.solarRadioYes.setText(_translate("MainWindow", "Teinté (Photochromique ou T3, T4)", None))
        self.label_10.setText(_translate("MainWindow", "Commentaire :", None))
        self.fileMenu.setTitle(_translate("MainWindow", "Fichier", None))
        self.newAction.setText(_translate("MainWindow", "Nouveau", None))
        self.newAction.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.saveAction.setText(_translate("MainWindow", "Sauvegarder", None))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.exitAction.setText(_translate("MainWindow", "Quitter", None))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.backupAction.setText(_translate("MainWindow", "Backup", None))
        self.backupAction.setToolTip(_translate("MainWindow", "Sauvegarde la base de donnée dans un fichier externe", None))
        self.backupAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+B", None))
        self.restoreAction.setText(_translate("MainWindow", "Restaurer", None))
        self.restoreAction.setToolTip(_translate("MainWindow", "Charge un Backup. Attention, les données actuellement affichées sont détruites !", None))
        self.restoreAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+R", None))
        self.deleteAction.setText(_translate("MainWindow", "Supprimer", None))
        self.deleteAction.setToolTip(_translate("MainWindow", "Supprimer les lunettes sélectionnées", None))
        self.deleteAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+D", None))
        self.printAction.setText(_translate("MainWindow", "Imprimer...", None))
        self.printAction.setToolTip(_translate("MainWindow", "Crée un fichier PDF contenant la liste des lunettes triées", None))

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

