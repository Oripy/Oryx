# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:52:58 2013

@author: pmaurier
"""

import os, sys
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets, uic

# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Ui_MainWindow = uic.loadUiType(resource_path('inventory.ui'))[0]
# from inventoryUI import Ui_MainWindow

from printlist import createpdf

import os

from config import *
from formatting import *
from datafilehandling import *

# Create the data file if it doesn't exists
open(FILENAME, 'a').close()

# Create autosaves dir if it doesn't exists
if not os.path.exists(AUTOSAVE_DIR):
    os.makedirs(AUTOSAVE_DIR)

# Constant for the sorting role in the Standard Items
SORT_ROLE = QtCore.Qt.UserRole + 1

###########################################

############## Main Window ################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)
        self.initUI()

        self.current_num = self.eyeglassesNum.value()
        self.modif = False

        # Data Structure (Name, formating function, get function,
        #                 set function, default value)
        self.data_structure = [
            ['Num', lambda n: str(int(n)), self.eyeglassesNum.value,
             self.eyeglassesNum.setValue, 1],
            ['OD Sph', formatSph, self.rSphereSpin.value,
              self.rSphereSpin.setValue, DEFAULT_SPHERE],
            ['OD Cyl', formatCyl, self.rCylSpin.value,
             self.rCylSpin.setValue, DEFAULT_CYL],
            ['OD Axe', formatAxis, self.rAxisSpin.value,
             self.rAxisSpin.setValue, DEFAULT_AXIS],
            ['OD Add', formatSph, self.rAddSpin.value,
             self.rAddSpin.setValue, DEFAULT_ADD],
            ['OG Sph', formatSph, self.lSphereSpin.value,
             self.lSphereSpin.setValue, DEFAULT_SPHERE],
            ['OG Cyl', formatCyl, self.lCylSpin.value,
             self.lCylSpin.setValue, DEFAULT_CYL],
            ['OG Axe', formatAxis, self.lAxisSpin.value,
             self.lAxisSpin.setValue, DEFAULT_AXIS],
            ['OG Add', formatSph, self.lAddSpin.value,
             self.lAddSpin.setValue, DEFAULT_ADD],
            ['Foyer', formatType, self.getAddType, self.setAddType, 0],
            ['Mont', formatFrame, self.getFrame, self.setFrame, 0],
            ['Teinte', formatSun, self.getSolar, self.setSolar, 0],
            ['Com', lambda n: str(n),
             self.getComment, self.setComment, ''],
            ['Statut', formatStock, lambda: 1, lambda n: n, 1],
            ['Date Mvmt', formatDate, self.getDateMvmt, 
             self.setDateMvmt, date.today()],
            ]

        self.data = dict()
        self.model = QtGui.QStandardItemModel(self)

        self.data = self.loadDataFromCsv()

        self.displayData(self.data)
        self.new()

    def initUI(self):
        """ create actions and default values of the interface """
        # List actions and create the menubar
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        self.saveAction.triggered.connect(self.save)
        self.deleteAction.triggered.connect(self.delete)
        self.newAction.triggered.connect(self.new)
        self.backupAction.triggered.connect(backup)
        self.restoreAction.triggered.connect(self.restoreAndShow)
        self.printAction.triggered.connect(lambda: createpdf(self.model))
        self.printButton.clicked.connect(lambda: createpdf(self.model))

        # Numbering/Actions panel
        self.eyeglassesNum.valueChanged.connect(self.eyeglassesNumModified)

        self.current_num = self.eyeglassesNum.value()
        self.eyeglassesNum.noWarn = False

        self.saveButton.clicked.connect(self.saveAction.trigger)
        self.deleteButton.clicked.connect(self.deleteAction.trigger)
        self.newButton.clicked.connect(self.newAction.trigger)
        self.backupButton.clicked.connect(self.backupAction.trigger)
        self.restoreButton.clicked.connect(self.restoreAction.trigger)

        # Right Eye
        # Correction
        self.rSphereSpin.setMaximum(MAX_SPHERE)
        self.rSphereSpin.setMinimum(MIN_SPHERE)
        self.rSphereSpin.setSingleStep(STEP_SPHERE)
        self.rSphereSpin.setValue(DEFAULT_SPHERE)
        self.rSphereSpin.valueChanged.connect(self.modified)

        self.rCylSpin.setMaximum(MAX_CYL)
        self.rCylSpin.setMinimum(MIN_CYL)
        self.rCylSpin.setSingleStep(STEP_CYL)
        self.rCylSpin.setValue(DEFAULT_CYL)
        self.rCylSpin.valueChanged.connect(self.modified)

        self.rLabelCylPos.setVisible(False)
        self.rLabelCylPos.setPalette(RED_PALETTE)

        self.rAxisSpin.setMaximum(MAX_AXIS)
        self.rAxisSpin.setMinimum(MIN_AXIS)
        self.rAxisSpin.setSingleStep(STEP_AXIS)
        self.rAxisSpin.setValue(DEFAULT_AXIS)
        self.rAxisSpin.valueChanged.connect(self.modified)

        self.r90Button.clicked.connect(self.r90Action)
        self.rFineCheckbox.stateChanged.connect(self.rFineChanged)

        self.rAddSpin.setMaximum(MAX_ADD)
        self.rAddSpin.setMinimum(MIN_ADD)
        self.rAddSpin.setSingleStep(STEP_ADD)
        self.rAddSpin.setValue(DEFAULT_ADD)
        self.rAddSpin.valueChanged.connect(self.enableAddition)

        self.rLinkCheckbox.stateChanged.connect(self.linkChanged)

        self.rCopyButton.clicked.connect(self.copyRtoL)

        # Left Eye
        # Correction
        self.lSphereSpin.setMaximum(MAX_SPHERE)
        self.lSphereSpin.setMinimum(MIN_SPHERE)
        self.lSphereSpin.setSingleStep(STEP_SPHERE)
        self.lSphereSpin.setValue(DEFAULT_SPHERE)
        self.lSphereSpin.valueChanged.connect(self.modified)

        self.lCylSpin.setMaximum(MAX_CYL)
        self.lCylSpin.setMinimum(MIN_CYL)
        self.lCylSpin.setSingleStep(STEP_CYL)
        self.lCylSpin.setValue(DEFAULT_CYL)
        self.lCylSpin.valueChanged.connect(self.modified)

        self.lLabelCylPos.setVisible(False)
        self.lLabelCylPos.setPalette(RED_PALETTE)

        self.lAxisSpin.setMaximum(MAX_AXIS)
        self.lAxisSpin.setMinimum(MIN_AXIS)
        self.lAxisSpin.setSingleStep(STEP_AXIS)
        self.lAxisSpin.setValue(DEFAULT_AXIS)
        self.lAxisSpin.valueChanged.connect(self.modified)

        self.l90Button.clicked.connect(self.l90Action)
        self.lFineCheckbox.stateChanged.connect(self.lFineChanged)

        self.lAddSpin.setMaximum(MAX_ADD)
        self.lAddSpin.setMinimum(MIN_ADD)
        self.lAddSpin.setSingleStep(STEP_ADD)
        self.lAddSpin.setValue(DEFAULT_ADD)
        self.lAddSpin.valueChanged.connect(self.enableAddition)

        self.lLinkCheckbox.stateChanged.connect(self.linkChanged)

        # Addition
        self.addRadioP.toggled.connect(self.modified)
        self.addRadioBF.toggled.connect(self.modified)

        # Comments
        self.commentEdit.textChanged.connect(self.modified)

        # Solar
        self.solarRadioNo.toggled.connect(self.modified)
        self.solarRadioYes.toggled.connect(self.modified)

        # Frame
        self.childRadioNo.toggled.connect(self.modified)
        self.childRadioYes.toggled.connect(self.modified)
        self.childRadioHalf.toggled.connect(self.modified)

        # Table
        self.tableView.doubleClicked.connect(self.selectLine)
        self.tableView.setSortingEnabled(True)

    def loadDataFromCsv(self):
        out = loadCsv()
        for key in out:
            for j in range(len(self.data_structure)):
                if j > len(out[key]):
                    out[key].append(0)
        return out

    def closeEvent(self, event):
        """ Reimplementation of the closeEvent
            to warn the user about potential dataloss """
        if self.warnModified() != 'Canceled':
            event.accept()
        else:
            event.ignore()

    def enableAddition(self):
        """ Enable the right addition group
            when addition value is different from 0.00 """
        if (self.rAddSpin.value() == 0) and (self.lAddSpin.value() == 0):
            self.addGroupBox.setDisabled(True)
        else:
            self.addGroupBox.setDisabled(False)

        value = self.sender().value()
        if self.rLinkCheckbox.isChecked() and self.rAddSpin.value() != self.lAddSpin.value():
            if self.sender() == self.rAddSpin:
                self.lAddSpin.setValue(value)
            elif self.sender() == self.lAddSpin:
                self.rAddSpin.setValue(value)
        self.modified()

    def linkChanged(self):
        """ Link the state of the two checkboxes """
        state = self.sender().isChecked()
        self.lLinkCheckbox.setChecked(state)
        self.rLinkCheckbox.setChecked(state)

    def r90Action(self):
        if self.r90Button.text() == "90°":
            self.rAxisSpin.setValue(90)
            self.r90Button.setText("180°")
        else:
            self.rAxisSpin.setValue(180)
            self.r90Button.setText("90°")

    def l90Action(self):
        if self.l90Button.text() == "90°":
            self.lAxisSpin.setValue(90)
            self.l90Button.setText("180°")
        else:
            self.lAxisSpin.setValue(180)
            self.l90Button.setText("90°")

    def rFineChanged(self):
        if self.rFineCheckbox.isChecked():
            self.rAxisSpin.setSingleStep(1)
            self.rAxisSpin.setMinimum(1)
        else:
            self.rAxisSpin.setMinimum(MIN_AXIS)
            self.rAxisSpin.setSingleStep(5)
            self.rAxisSpin.setValue(self.rAxisSpin.value()-self.rAxisSpin.value()%5)

    def lFineChanged(self):
        if self.lFineCheckbox.isChecked():
            self.lAxisSpin.setSingleStep(1)
            self.lAxisSpin.setMinimum(1)
        else:
            self.lAxisSpin.setMinimum(MIN_AXIS)
            self.lAxisSpin.setSingleStep(5)
            self.lAxisSpin.setValue(self.lAxisSpin.value()-self.lAxisSpin.value()%5)

    def copyRtoL(self):
        if (self.rFineCheckbox.isChecked()):
            self.lFineCheckbox.setChecked(True)
        if self.lSphereSpin.value() != self.rSphereSpin.value():
            self.lSphereSpin.setValue(self.rSphereSpin.value())
            self.lSphereSpin.setStyleSheet("background-color: lightgrey")
        if self.lCylSpin.value() != self.rCylSpin.value():
            self.lCylSpin.setValue(self.rCylSpin.value())
            self.lCylSpin.setStyleSheet("background-color: lightgrey")
        if self.lAxisSpin.value() != self.rAxisSpin.value():
            self.lAxisSpin.setValue(self.rAxisSpin.value())
            self.lAxisSpin.setStyleSheet("background-color: lightgrey")
        if self.lAddSpin.value() != self.rAddSpin.value():
            self.lAddSpin.setValue(self.rAddSpin.value())
            self.lAddSpin.setStyleSheet("background-color: lightgrey")

    def modified(self):
        """ Action when a value is modified """
        self.setStatus('Modified')
        self.sender().setStyleSheet("")
        self.modif = True

        self.rLabelCylPos.setVisible(self.rCylSpin.value() > 0)
        self.lLabelCylPos.setVisible(self.lCylSpin.value() > 0)

    def getFirstNewNumber(self):
        """ returns the next available number
            (starting with the current number) """
        n = self.current_num
        while n in self.data:
            n += 1
        return n

    def new(self):
        """ set the number to the smallest available eyeglasses number """
        n = self.getFirstNewNumber()
        if n != self.current_num:
            self.eyeglassesNum.setValue(n)
            self.rSphereSpin.setFocus()
            self.rSphereSpin.selectAll()
        else:
            self.warnModified()

    def getAddType(self):
        """ returns the code corresponding to the selected radio button
            0 means section is disabled
            1 means Progressive
            2 means Bifocal
        """
        if (self.rAddSpin.value() != 0) or (self.lAddSpin.value() != 0):
            if self.addRadioP.isChecked():
                return 1
            elif self.addRadioBF.isChecked():
                return 2
        else:
            return 0

    def setAddType(self, value):
        """ selects the radio button corresponding to the input code
            0 or 1 selects Progressive
            2 selects Bifocal
        """
        if value == 2:
            self.addRadioBF.setChecked(True)
        else:
            self.addRadioP.setChecked((True))

    def getSolar(self):
        """ returns the code corresponding to the selected radio button
            0 means normal lenses
            1 means solar lenses
        """
        return int(self.solarRadioYes.isChecked())

    def setSolar(self, value):
        """ selects the radio button corresponding to the input code
            0 selects normal lenses
            1 selects solar lenses
        """
        if value == 1:
            self.solarRadioYes.setChecked(True)
        else:
            self.solarRadioNo.setChecked(True)

    def getDateMvmt(self):
        return date.today()

    def setDateMvmt(self, value):
        pass

    def getFrame(self):
        """ returns the code corresponding to the selected radio button
            0 means adult frame
            1 means child frame
            2 means half-lenses
        """
        if self.childRadioYes.isChecked():
            return 1
        elif self.childRadioNo.isChecked():
            return 0
        else:
            return 2

    def setFrame(self, value):
        """ selects the radio button corresponding to the input code
            0 selects adult frame
            1 selects child frame
            2 selects half-lenses
        """
        if value == 1:
            self.childRadioYes.setChecked(True)
        elif value == 0:
            self.childRadioNo.setChecked(True)
        else:
            self.childRadioHalf.setChecked(True)

    def getComment(self):
        """ returns the comment formated to suitable codec """
        return self.commentEdit.toPlainText()

    def setComment(self, value):
        """ write the input value to the comment field """
        self.commentEdit.setPlainText(str(value))

    def convert(self):
        """ convert the data entered if cylinder is positive """
        if self.data_structure[2][2]() > 0:
            self.data_structure[1][3](
                    self.data_structure[1][2]() + self.data_structure[2][2]())
            self.data_structure[2][3](-self.data_structure[2][2]())
            self.data_structure[3][3]((self.data_structure[3][2]() + 90) % 180)

        if self.data_structure[6][2]() > 0:
            self.data_structure[5][3](
                    self.data_structure[5][2]() + self.data_structure[6][2]())
            self.data_structure[6][3](-self.data_structure[6][2]())
            self.data_structure[7][3]((self.data_structure[7][2]() + 90) % 180)

    def save(self):
        """ Save the modifications and write it to the CSV file """
        self.convert()

        item = [QtGui.QStandardItem(str(self.current_num))] \
               + [QtGui.QStandardItem( \
                   self.data_structure[i][1](self.data_structure[i][2]()) \
                   ) for i in range(len(self.data_structure))[1:]]

        # For each item, add the data value to allow correct sorting
        for i, item_data in enumerate(item):
            item_data.setData(self.data_structure[i][2](), SORT_ROLE)

        if self.data_structure[2][2]() == 0:
            item[3].setData(u'000°', QtCore.Qt.DisplayRole)
            item[3].setData(0, SORT_ROLE)

        if self.data_structure[6][2]() == 0:
            item[7].setData(u'000°', QtCore.Qt.DisplayRole)
            item[7].setData(0, SORT_ROLE)

        item[0].setBackground(QtGui.QColor(UNIT_COLORS[int(str(self.current_num)[-1])]))

        item[1].setBackground(RIGHT_COLOR)
        item[2].setBackground(RIGHT_COLOR)
        item[3].setBackground(RIGHT_COLOR)
        item[4].setBackground(RIGHT_COLOR)

        item[5].setBackground(LEFT_COLOR)
        item[6].setBackground(LEFT_COLOR)
        item[7].setBackground(LEFT_COLOR)
        item[8].setBackground(LEFT_COLOR)
        if not self.current_num in self.data and self.modif:
            # Add a line to the table if the current item do not exists
            # (and has been modified)
            self.model.appendRow(item)
        else:
            # Alter the existing line
            rows = self.model.findItems(str(self.current_num))
            if len(rows) == 1:
                row = rows[0].row()
                for column, elem in enumerate(item):
                    self.model.setItem(row, column, elem)
            else:
                print("Error when trying to update the TableView")
        if self.modif:
            self.data = self.loadDataFromCsv()
            self.data[self.current_num] = [self.data_structure[i][2]()
                          for i in range(len(self.data_structure))[1:]]
            if self.data[self.current_num][1] == 0:
                self.data[self.current_num][2] = 0
            if self.data[self.current_num][5] == 0:
                self.data[self.current_num][6] = 0
            writeCsv(self.data)
            autoSave(self.data)
            self.setStatus('Saved')
            self.modif = False
        self.scrollTo(self.current_num)

        self.new()

        self.model.setSortRole(SORT_ROLE)
        self.tableView.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def delete(self):
        """ Delete given entry and write the modification to the CSV file """
        text = (u'Les lunettes numéro '+str(self.current_num)+' '
                u'vont être retirées de l\'inventaire.\n'
                u'\n'
                u'Souhaitez-vous continuer ?')
        question = QtWidgets.QMessageBox.warning(self,
            u'Supprimer les données ?',
            text,
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)

        if question == QtWidgets.QMessageBox.Yes:
            if self.current_num in self.data:
                rows = self.model.findItems(str(self.current_num))
                if len(rows) == 1:
                    self.model.takeRow(rows[0].row())
                else:
                    print("Error when trying to find the right row to delete")
                self.data = self.loadDataFromCsv()
                self.data.pop(self.current_num)
                writeCsv(self.data)
                self.setStatus('New')
                self.modif = False
                self.reset()

    def loadData(self):
        """ Load data from the self.data variable
            and display it in the form """
        self.rLinkCheckbox.setChecked(False)
        if self.current_num in self.data:
            self.rFineCheckbox.setChecked(self.data[self.current_num][3] % 5 != 0)
            self.lFineCheckbox.setChecked(self.data[self.current_num][7] % 5 != 0)
            for i, element in enumerate(self.data_structure[1:]):
                element[3](self.data[self.current_num][i])
            self.modif = False
            self.setStatus('Saved')
        else:
            self.reset()

        if self.rAddSpin.value() == self.lAddSpin.value():
            self.rLinkCheckbox.setChecked(True)

        self.scrollTo(self.current_num)

    def scrollTo(self, number):
        """ scrolls and selects the line corresponding to the input number """
        items = self.model.findItems(str(number))
        if len(items) != 0:
            self.tableView.scrollTo(items[0].index())
            self.tableView.selectRow(items[0].index().row())
        else:
            self.tableView.scrollToBottom()

    def selectLine(self):
        """ change the eyeglasses number to the selected line in the table """
        row = self.tableView.selectionModel().currentIndex().row()
        self.eyeglassesNum.setValue(int(self.model.item(row, 0).text()))

    def reset(self):
        """ Reset the values in the form to the default values """
        self.rFineCheckbox.setChecked(False)
        self.lFineCheckbox.setChecked(False)
        for element in self.data_structure[1:]:
            element[3](element[4])
        self.modif = False

        self.setStatus('New')

    def setStatus(self, value):
        """ Display the current status (Saved/Modified/New)
            with different colors """
        if value == 'Saved':
            self.status.setText(u'Enregistré')
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.green)
            self.status.setPalette(palette)
        elif value == 'Modified':
            self.status.setText(u'Modifié')
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
            self.status.setPalette(palette)
        elif value == 'New':
            self.status.setText(u'Nouveau')
            palette = QtGui.QPalette()
            palette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.blue)
            self.status.setPalette(palette)

    def eyeglassesNumModified(self):
        """ Event when num is modified """
        self.eyeglassesNum.setStyleSheet("QSpinBox { background-color: "+QtGui.QColor(UNIT_COLORS[int(str(self.eyeglassesNum.value())[-1])]).name()+"; }")
        self.warnModified()

    def warnModified(self):
        """ Warn the user that unsaved data will be lost if unsaved """
        if not(self.eyeglassesNum.noWarn):
            if self.modif:
                text = (u'Les lunettes '+str(self.current_num)+' '
                        u'n\'ont pas été enregistrées.\n'
                        u'Abandonner les changements ?')
                question = QtWidgets.QMessageBox.warning(self,
                    u'Lunettes Modifiées !',
                    text,
                    QtWidgets.QMessageBox.Yes,
                    QtWidgets.QMessageBox.No)

                if question == QtWidgets.QMessageBox.Yes:
                    self.current_num = self.eyeglassesNum.value()
                    self.loadData()
                    return 'Discarded'
                else:
                    if self.sender() != None:
                        self.eyeglassesNum.noWarn = True
                    self.eyeglassesNum.setValue(self.current_num)
                    return 'Canceled'
            else:
                self.current_num = self.eyeglassesNum.value()
                self.loadData()
        else:
            self.eyeglassesNum.noWarn = False
            return 'Saved'

    def restoreAndShow(self):
        """ Restore data from file and displays it in the table """
        restored_data = restore()
        if restored_data != []:
            self.data = restored_data
            self.displayData(self.data)

    def displayData(self, data):
        """ Displays data in the table """
        self.model.clear()
        labels = [self.data_structure[i][0] for i in range(len(self.data_structure))]
        labels.insert(1, "Boite")
        self.model.setHorizontalHeaderLabels(labels)

        for key, values in data.items():
            row = [key] + values

            items = [QtGui.QStandardItem(self.data_structure[i][1](row[i]))
                         for i in range(len(self.data_structure))]

            # For each item, add the data value to allow correct sorting
            for i, item in enumerate(items):
                item.setData(getData(row[i]), SORT_ROLE)
            items[0].setBackground(QtGui.QColor(UNIT_COLORS[int(str(row[0])[-1])]))

            items[1].setBackground(RIGHT_COLOR)
            items[2].setBackground(RIGHT_COLOR)
            items[3].setBackground(RIGHT_COLOR)
            items[4].setBackground(RIGHT_COLOR)

            items[5].setBackground(LEFT_COLOR)
            items[6].setBackground(LEFT_COLOR)
            items[7].setBackground(LEFT_COLOR)
            items[8].setBackground(LEFT_COLOR)

            items[13].setBackground(STATUS_COLOR[int(row[13])])

            box = int(row[0])//NBR_PER_BOX
            box_letter = chr(65+box//6)
            box_number = box % 6 + 1
            box_label = f'''{box_letter}{box_number}'''
            items.insert(1, QtGui.QStandardItem(box_label))

            self.model.appendRow(items)

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.horizontalHeader().moveSection(14, 2)
        self.model.setSortRole(SORT_ROLE)
        self.tableView.sortByColumn(0, QtCore.Qt.AscendingOrder)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.searchWindowButton.hide()
    mainWin.show()
    sys.exit(app.exec_())
