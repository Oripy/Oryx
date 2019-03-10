# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(281, 170)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.numRadio = QtWidgets.QRadioButton(self.groupBox)
        self.numRadio.setChecked(True)
        self.numRadio.setObjectName("numRadio")
        self.verticalLayout.addWidget(self.numRadio)
        self.rRadio = QtWidgets.QRadioButton(self.groupBox)
        self.rRadio.setObjectName("rRadio")
        self.verticalLayout.addWidget(self.rRadio)
        self.lRadio = QtWidgets.QRadioButton(self.groupBox)
        self.lRadio.setObjectName("lRadio")
        self.verticalLayout.addWidget(self.lRadio)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.stockCheckBox = QtWidgets.QCheckBox(Dialog)
        self.stockCheckBox.setObjectName("stockCheckBox")
        self.verticalLayout_2.addWidget(self.stockCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Impression"))
        self.groupBox.setTitle(_translate("Dialog", "Tri"))
        self.numRadio.setText(_translate("Dialog", "Trier par numéro"))
        self.rRadio.setText(_translate("Dialog", "Trier par Sphere de l\'OD"))
        self.lRadio.setText(_translate("Dialog", "Trier par Sphere de l\'OG"))
        self.stockCheckBox.setText(_translate("Dialog", "Imprimer uniquement les lunettes encore en stock"))


