# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print.ui'
#
# Created: Wed Sep 25 11:21:58 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(281, 170)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.numRadio = QtGui.QRadioButton(self.groupBox)
        self.numRadio.setChecked(True)
        self.numRadio.setObjectName(_fromUtf8("numRadio"))
        self.verticalLayout.addWidget(self.numRadio)
        self.lRadio = QtGui.QRadioButton(self.groupBox)
        self.lRadio.setObjectName(_fromUtf8("lRadio"))
        self.verticalLayout.addWidget(self.lRadio)
        self.rRadio = QtGui.QRadioButton(self.groupBox)
        self.rRadio.setObjectName(_fromUtf8("rRadio"))
        self.verticalLayout.addWidget(self.rRadio)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.stockCheckBox = QtGui.QCheckBox(Dialog)
        self.stockCheckBox.setObjectName(_fromUtf8("stockCheckBox"))
        self.verticalLayout_2.addWidget(self.stockCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Impression", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Tri", None, QtGui.QApplication.UnicodeUTF8))
        self.numRadio.setText(QtGui.QApplication.translate("Dialog", "Trier par numéro", None, QtGui.QApplication.UnicodeUTF8))
        self.lRadio.setText(QtGui.QApplication.translate("Dialog", "Trier par Sphere de l\'OG", None, QtGui.QApplication.UnicodeUTF8))
        self.rRadio.setText(QtGui.QApplication.translate("Dialog", "Trier par Sphere de l\'OD", None, QtGui.QApplication.UnicodeUTF8))
        self.stockCheckBox.setText(QtGui.QApplication.translate("Dialog", "Imprimer uniquement les lunettes encore en stock", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

