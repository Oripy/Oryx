# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(807, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("glasses.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName("mainLayout")
        self.eyesLayout = QtWidgets.QHBoxLayout()
        self.eyesLayout.setObjectName("eyesLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.eyesLayout.addItem(spacerItem)
        self.rightEyeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rightEyeGroupBox.setFont(font)
        self.rightEyeGroupBox.setObjectName("rightEyeGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.rightEyeGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.rightEyeLayout = QtWidgets.QGridLayout()
        self.rightEyeLayout.setObjectName("rightEyeLayout")
        self.label_2 = QtWidgets.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.rightEyeLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.rightEyeLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
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
        self.rAxisSpin.setObjectName("rAxisSpin")
        self.rightEyeLayout.addWidget(self.rAxisSpin, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.rightEyeLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.rLinkCheckbox = QtWidgets.QCheckBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rLinkCheckbox.setFont(font)
        self.rLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rLinkCheckbox.setChecked(True)
        self.rLinkCheckbox.setObjectName("rLinkCheckbox")
        self.rightEyeLayout.addWidget(self.rLinkCheckbox, 2, 3, 1, 1)
        self.rAddSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rAddSpin.setFont(font)
        self.rAddSpin.setObjectName("rAddSpin")
        self.rightEyeLayout.addWidget(self.rAddSpin, 1, 3, 1, 1)
        self.rCylSpin = negativeZeroSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rCylSpin.setFont(font)
        self.rCylSpin.setObjectName("rCylSpin")
        self.rightEyeLayout.addWidget(self.rCylSpin, 1, 1, 1, 1)
        self.rSphereSpin = dotSpinBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rSphereSpin.setFont(font)
        self.rSphereSpin.setObjectName("rSphereSpin")
        self.rightEyeLayout.addWidget(self.rSphereSpin, 1, 0, 1, 1)
        self.rLabelCylPos = QtWidgets.QLabel(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.rLabelCylPos.setFont(font)
        self.rLabelCylPos.setObjectName("rLabelCylPos")
        self.rightEyeLayout.addWidget(self.rLabelCylPos, 2, 1, 1, 1)
        self.gridLayout_7.addLayout(self.rightEyeLayout, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rMasterRadio = QtWidgets.QRadioButton(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rMasterRadio.setFont(font)
        self.rMasterRadio.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rMasterRadio.setChecked(True)
        self.rMasterRadio.setObjectName("rMasterRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rMasterRadio)
        self.horizontalLayout_7.addWidget(self.rMasterRadio)
        self.rIndifCheckBox = QtWidgets.QCheckBox(self.rightEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rIndifCheckBox.setFont(font)
        self.rIndifCheckBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rIndifCheckBox.setObjectName("rIndifCheckBox")
        self.horizontalLayout_7.addWidget(self.rIndifCheckBox)
        self.gridLayout_7.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.eyesLayout.addWidget(self.rightEyeGroupBox)
        self.leftEyeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leftEyeGroupBox.setFont(font)
        self.leftEyeGroupBox.setObjectName("leftEyeGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.leftEyeGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.leftEyeLayout = QtWidgets.QGridLayout()
        self.leftEyeLayout.setObjectName("leftEyeLayout")
        self.lCylSpin = negativeZeroSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lCylSpin.setFont(font)
        self.lCylSpin.setObjectName("lCylSpin")
        self.leftEyeLayout.addWidget(self.lCylSpin, 1, 1, 1, 1)
        self.lAddSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAddSpin.setFont(font)
        self.lAddSpin.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.lAddSpin.setObjectName("lAddSpin")
        self.leftEyeLayout.addWidget(self.lAddSpin, 1, 3, 1, 1)
        self.lLinkCheckbox = QtWidgets.QCheckBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lLinkCheckbox.setFont(font)
        self.lLinkCheckbox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lLinkCheckbox.setChecked(True)
        self.lLinkCheckbox.setObjectName("lLinkCheckbox")
        self.leftEyeLayout.addWidget(self.lLinkCheckbox, 2, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.leftEyeLayout.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.leftEyeLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.leftEyeLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.leftEyeLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.lSphereSpin = dotSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lSphereSpin.setFont(font)
        self.lSphereSpin.setObjectName("lSphereSpin")
        self.leftEyeLayout.addWidget(self.lSphereSpin, 1, 0, 1, 1)
        self.lAxisSpin = angleSpinBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lAxisSpin.setFont(font)
        self.lAxisSpin.setWrapping(True)
        self.lAxisSpin.setMinimum(5)
        self.lAxisSpin.setMaximum(180)
        self.lAxisSpin.setSingleStep(5)
        self.lAxisSpin.setProperty("value", 180)
        self.lAxisSpin.setObjectName("lAxisSpin")
        self.leftEyeLayout.addWidget(self.lAxisSpin, 1, 2, 1, 1)
        self.lLabelCylPos = QtWidgets.QLabel(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lLabelCylPos.setFont(font)
        self.lLabelCylPos.setObjectName("lLabelCylPos")
        self.leftEyeLayout.addWidget(self.lLabelCylPos, 2, 1, 1, 1)
        self.gridLayout_8.addLayout(self.leftEyeLayout, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lMasterRadio = QtWidgets.QRadioButton(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lMasterRadio.setFont(font)
        self.lMasterRadio.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lMasterRadio.setObjectName("lMasterRadio")
        self.buttonGroup.addButton(self.lMasterRadio)
        self.horizontalLayout_8.addWidget(self.lMasterRadio)
        self.lIndifCheckBox = QtWidgets.QCheckBox(self.leftEyeGroupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lIndifCheckBox.setFont(font)
        self.lIndifCheckBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lIndifCheckBox.setObjectName("lIndifCheckBox")
        self.horizontalLayout_8.addWidget(self.lIndifCheckBox)
        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.eyesLayout.addWidget(self.leftEyeGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.eyesLayout.addItem(spacerItem1)
        self.mainLayout.addLayout(self.eyesLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.childGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.childGroupBox.sizePolicy().hasHeightForWidth())
        self.childGroupBox.setSizePolicy(sizePolicy)
        self.childGroupBox.setObjectName("childGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.childGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.childRadioNo = QtWidgets.QRadioButton(self.childGroupBox)
        self.childRadioNo.setChecked(True)
        self.childRadioNo.setObjectName("childRadioNo")
        self.horizontalLayout_2.addWidget(self.childRadioNo)
        self.childRadioHalf = QtWidgets.QRadioButton(self.childGroupBox)
        self.childRadioHalf.setObjectName("childRadioHalf")
        self.horizontalLayout_2.addWidget(self.childRadioHalf)
        self.childRadioYes = QtWidgets.QRadioButton(self.childGroupBox)
        self.childRadioYes.setObjectName("childRadioYes")
        self.horizontalLayout_2.addWidget(self.childRadioYes)
        self.horizontalLayout.addWidget(self.childGroupBox)
        self.solarGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solarGroupBox.sizePolicy().hasHeightForWidth())
        self.solarGroupBox.setSizePolicy(sizePolicy)
        self.solarGroupBox.setObjectName("solarGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.solarGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.solarRadioNo = QtWidgets.QRadioButton(self.solarGroupBox)
        self.solarRadioNo.setChecked(True)
        self.solarRadioNo.setObjectName("solarRadioNo")
        self.horizontalLayout_3.addWidget(self.solarRadioNo)
        self.solarRadioYes = QtWidgets.QRadioButton(self.solarGroupBox)
        self.solarRadioYes.setObjectName("solarRadioYes")
        self.horizontalLayout_3.addWidget(self.solarRadioYes)
        self.horizontalLayout.addWidget(self.solarGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.numberingLayout = QtWidgets.QHBoxLayout()
        self.numberingLayout.setObjectName("numberingLayout")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.resetButton.setFont(font)
        self.resetButton.setObjectName("resetButton")
        self.numberingLayout.addWidget(self.resetButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.numberingLayout.addItem(spacerItem4)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.searchButton.setFont(font)
        self.searchButton.setAutoDefault(True)
        self.searchButton.setObjectName("searchButton")
        self.numberingLayout.addWidget(self.searchButton)
        self.distantSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.distantSearchButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.distantSearchButton.setFont(font)
        self.distantSearchButton.setAutoDefault(True)
        self.distantSearchButton.setObjectName("distantSearchButton")
        self.numberingLayout.addWidget(self.distantSearchButton)
        self.nearSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.nearSearchButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nearSearchButton.setFont(font)
        self.nearSearchButton.setAutoDefault(True)
        self.nearSearchButton.setObjectName("nearSearchButton")
        self.numberingLayout.addWidget(self.nearSearchButton)
        self.mainLayout.addLayout(self.numberingLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.mainLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setStretchLastSection(False)
        self.mainLayout.addWidget(self.tableView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.commentEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commentEdit.sizePolicy().hasHeightForWidth())
        self.commentEdit.setSizePolicy(sizePolicy)
        self.commentEdit.setMaximumSize(QtCore.QSize(16777215, 120))
        self.commentEdit.setReadOnly(True)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout.addWidget(self.commentEdit, 0, 3, 5, 2)
        self.eyeglassesNum = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eyeglassesNum.setFont(font)
        self.eyeglassesNum.setMinimum(1)
        self.eyeglassesNum.setMaximum(1000000)
        self.eyeglassesNum.setProperty("value", 1)
        self.eyeglassesNum.setObjectName("eyeglassesNum")
        self.gridLayout.addWidget(self.eyeglassesNum, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lSphereLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSphereLabel.sizePolicy().hasHeightForWidth())
        self.lSphereLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lSphereLabel.setFont(font)
        self.lSphereLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lSphereLabel.setObjectName("lSphereLabel")
        self.horizontalLayout_5.addWidget(self.lSphereLabel)
        self.lCylLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lCylLabel.sizePolicy().hasHeightForWidth())
        self.lCylLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lCylLabel.setFont(font)
        self.lCylLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lCylLabel.setObjectName("lCylLabel")
        self.horizontalLayout_5.addWidget(self.lCylLabel)
        self.lAxisLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lAxisLabel.sizePolicy().hasHeightForWidth())
        self.lAxisLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lAxisLabel.setFont(font)
        self.lAxisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lAxisLabel.setObjectName("lAxisLabel")
        self.horizontalLayout_5.addWidget(self.lAxisLabel)
        self.lAddLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lAddLabel.sizePolicy().hasHeightForWidth())
        self.lAddLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lAddLabel.setFont(font)
        self.lAddLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lAddLabel.setObjectName("lAddLabel")
        self.horizontalLayout_5.addWidget(self.lAddLabel)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setEnabled(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 4, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 4, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rSphereLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rSphereLabel.sizePolicy().hasHeightForWidth())
        self.rSphereLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rSphereLabel.setFont(font)
        self.rSphereLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rSphereLabel.setObjectName("rSphereLabel")
        self.horizontalLayout_4.addWidget(self.rSphereLabel)
        self.rCylLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rCylLabel.sizePolicy().hasHeightForWidth())
        self.rCylLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rCylLabel.setFont(font)
        self.rCylLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rCylLabel.setObjectName("rCylLabel")
        self.horizontalLayout_4.addWidget(self.rCylLabel)
        self.rAxisLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rAxisLabel.sizePolicy().hasHeightForWidth())
        self.rAxisLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rAxisLabel.setFont(font)
        self.rAxisLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rAxisLabel.setObjectName("rAxisLabel")
        self.horizontalLayout_4.addWidget(self.rAxisLabel)
        self.rAddLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rAddLabel.sizePolicy().hasHeightForWidth())
        self.rAddLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rAddLabel.setFont(font)
        self.rAddLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rAddLabel.setObjectName("rAddLabel")
        self.horizontalLayout_4.addWidget(self.rAddLabel)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frameLabel.setFont(font)
        self.frameLabel.setText("")
        self.frameLabel.setObjectName("frameLabel")
        self.horizontalLayout_6.addWidget(self.frameLabel)
        self.solarLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solarLabel.setFont(font)
        self.solarLabel.setText("")
        self.solarLabel.setObjectName("solarLabel")
        self.horizontalLayout_6.addWidget(self.solarLabel)
        self.addLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addLabel.setFont(font)
        self.addLabel.setText("")
        self.addLabel.setObjectName("addLabel")
        self.horizontalLayout_6.addWidget(self.addLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 2, 1)
        self.mainLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.mainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        MainWindow.setMenuBar(self.menubar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.searchAction = QtWidgets.QAction(MainWindow)
        self.searchAction.setObjectName("searchAction")
        self.resetAction = QtWidgets.QAction(MainWindow)
        self.resetAction.setObjectName("resetAction")
        self.distantSearchAction = QtWidgets.QAction(MainWindow)
        self.distantSearchAction.setObjectName("distantSearchAction")
        self.nearSearchAction = QtWidgets.QAction(MainWindow)
        self.nearSearchAction.setObjectName("nearSearchAction")
        self.fileMenu.addAction(self.searchAction)
        self.fileMenu.addAction(self.distantSearchAction)
        self.fileMenu.addAction(self.nearSearchAction)
        self.fileMenu.addAction(self.resetAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.rSphereSpin, self.rCylSpin)
        MainWindow.setTabOrder(self.rCylSpin, self.rAxisSpin)
        MainWindow.setTabOrder(self.rAxisSpin, self.rAddSpin)
        MainWindow.setTabOrder(self.rAddSpin, self.lSphereSpin)
        MainWindow.setTabOrder(self.lSphereSpin, self.lCylSpin)
        MainWindow.setTabOrder(self.lCylSpin, self.lAxisSpin)
        MainWindow.setTabOrder(self.lAxisSpin, self.lAddSpin)
        MainWindow.setTabOrder(self.lAddSpin, self.childRadioNo)
        MainWindow.setTabOrder(self.childRadioNo, self.childRadioHalf)
        MainWindow.setTabOrder(self.childRadioHalf, self.childRadioYes)
        MainWindow.setTabOrder(self.childRadioYes, self.solarRadioNo)
        MainWindow.setTabOrder(self.solarRadioNo, self.solarRadioYes)
        MainWindow.setTabOrder(self.solarRadioYes, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.distantSearchButton)
        MainWindow.setTabOrder(self.distantSearchButton, self.nearSearchButton)
        MainWindow.setTabOrder(self.nearSearchButton, self.tableView)
        MainWindow.setTabOrder(self.tableView, self.resetButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Oryx Optical DBSM - Search"))
        self.rightEyeGroupBox.setTitle(_translate("MainWindow", "OD (Œil Droit)"))
        self.label_2.setText(_translate("MainWindow", "Sphere"))
        self.label_5.setText(_translate("MainWindow", "Addition"))
        self.label_4.setText(_translate("MainWindow", "Axe"))
        self.label_3.setText(_translate("MainWindow", "Cylindre"))
        self.rLinkCheckbox.setText(_translate("MainWindow", "Lié"))
        self.rLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Recherche"))
        self.rLabelCylPos.setText(_translate("MainWindow", "Cylindre positif"))
        self.rMasterRadio.setText(_translate("MainWindow", "Œil droit préférentiel"))
        self.rIndifCheckBox.setText(_translate("MainWindow", "Valeurs indifférentes"))
        self.leftEyeGroupBox.setTitle(_translate("MainWindow", "OG (Œil Gauche)"))
        self.lLinkCheckbox.setText(_translate("MainWindow", "Lié"))
        self.label_8.setText(_translate("MainWindow", "Axe"))
        self.label_6.setText(_translate("MainWindow", "Sphere"))
        self.label_9.setText(_translate("MainWindow", "Cylindre"))
        self.label_7.setText(_translate("MainWindow", "Addition"))
        self.lLabelCylPos.setToolTip(_translate("MainWindow", "Le cylindre indiqué est positif, une conversion sera effectuée lors de la Recherche"))
        self.lLabelCylPos.setText(_translate("MainWindow", "Cylindre positif"))
        self.lMasterRadio.setText(_translate("MainWindow", "Œil gauche préférentiel"))
        self.lIndifCheckBox.setText(_translate("MainWindow", "Valeurs indifférentes"))
        self.childGroupBox.setTitle(_translate("MainWindow", "Monture"))
        self.childRadioNo.setText(_translate("MainWindow", "Adulte"))
        self.childRadioHalf.setText(_translate("MainWindow", "Demi-lunes"))
        self.childRadioYes.setText(_translate("MainWindow", "Enfant"))
        self.solarGroupBox.setTitle(_translate("MainWindow", "Teinte"))
        self.solarRadioNo.setText(_translate("MainWindow", "Non teintés (ou T1, T2)"))
        self.solarRadioYes.setText(_translate("MainWindow", "Teintés (Photochromiques ou T3, T4)"))
        self.resetButton.setText(_translate("MainWindow", "Remise à zéro"))
        self.searchButton.setText(_translate("MainWindow", "Rechercher"))
        self.distantSearchButton.setText(_translate("MainWindow", "Vision de loin"))
        self.nearSearchButton.setText(_translate("MainWindow", "Vision de près"))
        self.label.setText(_translate("MainWindow", "Résultat de la recherche"))
        self.label_11.setText(_translate("MainWindow", "OD (Œil Droit)"))
        self.label_12.setText(_translate("MainWindow", "OG (Œil Gauche)"))
        self.label_10.setText(_translate("MainWindow", "Lunettes numéro :"))
        self.lSphereLabel.setText(_translate("MainWindow", "0.00"))
        self.lCylLabel.setText(_translate("MainWindow", "(-0.00)"))
        self.lAxisLabel.setText(_translate("MainWindow", "180°"))
        self.lAddLabel.setText(_translate("MainWindow", "0.00"))
        self.removeButton.setText(_translate("MainWindow", "Sortir du Stock"))
        self.addButton.setText(_translate("MainWindow", "Remettre en Stock"))
        self.rSphereLabel.setText(_translate("MainWindow", "0.00"))
        self.rCylLabel.setText(_translate("MainWindow", "(-0.00)"))
        self.rAxisLabel.setText(_translate("MainWindow", "180°"))
        self.rAddLabel.setText(_translate("MainWindow", "0.00"))
        self.fileMenu.setTitle(_translate("MainWindow", "Fichier"))
        self.exitAction.setText(_translate("MainWindow", "Quitter"))
        self.exitAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.searchAction.setText(_translate("MainWindow", "Rechercher"))
        self.searchAction.setToolTip(_translate("MainWindow", "Lance la recherche"))
        self.searchAction.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.resetAction.setText(_translate("MainWindow", "Remise à zéro"))
        self.resetAction.setToolTip(_translate("MainWindow", "Remise à zéro du formulaire de recherche"))
        self.resetAction.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.distantSearchAction.setText(_translate("MainWindow", "Rechercher vision de loin"))
        self.distantSearchAction.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.nearSearchAction.setText(_translate("MainWindow", "Rechercher vision de près"))
        self.nearSearchAction.setShortcut(_translate("MainWindow", "Ctrl+P"))


from anglespinbox import angleSpinBox
from dotspinbox import dotSpinBox
from negativezerospinbox import negativeZeroSpinBox
