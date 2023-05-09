# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:52:58 2013

@author: pmaurier
"""

from PyQt5 import QtCore, QtGui, QtWidgets, uic

import os, sys
from datetime import date
# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Ui_MainWindow = uic.loadUiType(resource_path('search.ui'))[0]
# from searchUI import Ui_MainWindow

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

######## Score related functions #########

def scoringFunction(delta, minimum, maximum):
    """ returns a score shaped by a polynomial function """
    if delta >= 0:
        return max(-(delta/maximum)**SCORE_SHAPE_PARAM + 1, 0)
    else:
        return max(-(delta/minimum)**SCORE_SHAPE_PARAM + 1, 0)

def eye_score(data, target):
    """ returns the score for one glass based on each parameter score """
    s = score_sphere(data, target)
    c = score_cyl(data, target)
    a = score_axis(data, target)
    p = score_add(data, target)
    score = s**SPHERE_COEF * c**CYL_COEF * a**AXIS_COEF * p**ADD_COEF
#    print s, c, a, p
    return score

def sphericalEquivalentRefraction(data, target):
    """ returns the Spherical Equivalent Refraction Sphere parameter
        using a different cylinder """
    delta_cyl =  data[1] - target[1]
#    print data, target, target[0] - delta_cyl/2 + (delta_cyl/2 % .25)
    return target[0] - delta_cyl/2 + (delta_cyl/2 % .25)

def score_sphere(data, target):
    """ returns the score related to the sphere """
    if (data[0] < 0 and target[0] > 0) or (data[0] > 0 and target[0] < 0):
        return 0
    delta_sph = data[0] - sphericalEquivalentRefraction(data, target)
    if data[0] >= 0:
        score = scoringFunction(delta_sph, SPHERE_DELTA_MIN, SPHERE_DELTA_MAX)
    else:
        score = scoringFunction(delta_sph, -SPHERE_DELTA_MAX,
                                -SPHERE_DELTA_MIN)
    return score

def score_cyl(data, target):
    """ returns the score related to the cylinder """
    delta_cyl =  data[1] - target[1]
    return scoringFunction(delta_cyl, CYL_DELTA_MIN, CYL_DELTA_MAX)

def score_axis(data, target):
    """ returns the score related to the axis """
    # if no cylinder correction, axis is not taken into account
    if (data[1] == 0) or (target[1] == 0):
        return 1
    tolerance = PARAM_AXIS_TOL2 * target[1]**2 + \
                PARAM_AXIS_TOL1 * target[1] + PARAM_AXIS_TOL0
    tolerance = tolerance - (tolerance % 5) + \
                (5 if (tolerance % 5) >= 2.5 else 0)

    delta_axis = (data[2] - target[2])
    delta_axis = abs((delta_axis + 90) % 180 - 90)
    return scoringFunction(delta_axis, -tolerance, tolerance)

def score_add(data, target):
    """ returns the score related to the addition """
    # if the search is without addition, returns a null score
    if target[3] == 0 and data[3] != 0:
        return 0
    delta_add = target[3] - data[3]
    return scoringFunction(delta_add, -ADD_DELTA_MAX, target[3]+0.25)

###########################################


############## Main Window ################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()

        self.setupUi(self)
        self.initUI()

        # Data Structure [Name, formating function, get function,
        #                 set function, default value, display stock function]
        self.data_structure = [
            ['Num', lambda n: str(int(n)), lambda: 1,
             lambda n: n, 1, self.eyeglassesNum.setValue],
            ['OD Sph', formatSph, self.rSphereSpin.value,
             self.rSphereSpin.setValue, DEFAULT_SPHERE, self.setRSphere],
            ['OD Cyl', formatCyl, self.rCylSpin.value,
             self.rCylSpin.setValue, DEFAULT_CYL, self.setRCyl],
            ['OD Axe', formatAxis, self.rAxisSpin.value,
             self.rAxisSpin.setValue, DEFAULT_AXIS, self.setRAxis],
            ['OD Add', formatSph, self.rAddSpin.value,
             self.rAddSpin.setValue, DEFAULT_ADD, self.setRAdd],
            ['OG Sph', formatSph, self.lSphereSpin.value,
             self.lSphereSpin.setValue, DEFAULT_SPHERE, self.setLSphere],
            ['OG Cyl', formatCyl, self.lCylSpin.value,
             self.lCylSpin.setValue, DEFAULT_CYL, self.setLCyl],
            ['OG Axe', formatAxis, self.lAxisSpin.value,
             self.lAxisSpin.setValue, DEFAULT_AXIS, self.setLAxis],
            ['OG Add', formatSph, self.lAddSpin.value,
             self.lAddSpin.setValue, DEFAULT_ADD, self.setLAdd],
            ['Foyer', formatType, lambda: 0,
             lambda n: n, 0, self.setAddType],
            ['Mont', formatFrame, self.getFrame,
             self.setFrame, -1, self.setFrameLabel],
            ['Teinte', formatSun, self.getSolar,
             self.setSolar, -1, self.setSolarLabel],
            ['Com.', lambda n: str(n),
             lambda: '', lambda n: n, '', self.setComment],
            ]

        self.data = dict()
        self.model = QtGui.QStandardItemModel(self)
        self.tableView.setModel(self.model)

        self.data = self.loadDataFromCsv()
        self.loadData(self.eyeglassesNum.value())
        self.tableView.sortByColumn(1, QtCore.Qt.AscendingOrder)
        self.rLinkCheckbox.setChecked(True)

    def initUI(self):
        """ create actions and default values of the interface """
        self.exitAction.triggered.connect(QtWidgets.qApp.quit)
        self.searchAction.triggered.connect(self.search)
        self.distantSearchAction.triggered.connect(self.distSearch)
        self.nearSearchAction.triggered.connect(self.nearSearch)
        self.resetAction.triggered.connect(self.reset)

        self.searchButton.clicked.connect(self.searchAction.trigger)
        self.distantSearchButton.clicked.connect(
                self.distantSearchAction.trigger)
        self.nearSearchButton.clicked.connect(self.nearSearchAction.trigger)
        self.resetButton.clicked.connect(self.resetAction.trigger)
        self.addButton.clicked.connect(self.addToStock)
        self.removeButton.clicked.connect(self.removeFromStock)
        self.givenButton.clicked.connect(self.givenFromStock)
        self.lostButton.clicked.connect(self.lostFromStock)

        # Right Eye
        self.rMasterRadio.toggled.connect(self.modified)

        self.rIndifCheckBox.stateChanged.connect(self.rIndifChanged)

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
        self.lMasterRadio.toggled.connect(self.modified)

        self.lIndifCheckBox.stateChanged.connect(self.lIndifChanged)

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

        self.eyeglassesNum.valueChanged.connect(self.loadData)

        # Solar
        self.solarRadioNo.toggled.connect(self.modified)
        self.solarRadioYes.toggled.connect(self.modified)

        # Frame
        self.childRadioNo.toggled.connect(self.modified)
        self.childRadioYes.toggled.connect(self.modified)
        self.childRadioHalf.toggled.connect(self.modified)

        # Table
        self.tableView.clicked.connect(self.selectLine)

    def loadDataFromCsv(self):
        out = loadCsv()
        for key in out:
            for j in range(len(self.data_structure)):
                if j > len(out[key]):
                    out[key].append(0)
        return out

    def addToStock(self):
        """ Place the selected glasses back in stock """
        self.data = self.loadDataFromCsv()
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 0:
            self.data[num][12] = 1

        self.data[num][13] = date.today()

        self.addButton.setDisabled(True)
        self.removeButton.setDisabled(False)
        self.givenButton.setDisabled(False)
        self.lostButton.setDisabled(False)

        writeCsv(self.data)

    def removeFromStock(self):
        """ Mark the selected glasses as out of stock """
        self.data = self.loadDataFromCsv()
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 1:
            self.data[num][12] = 0

        self.data[num][13] = date.today()

        self.addButton.setDisabled(False)
        self.removeButton.setDisabled(True)
        self.givenButton.setDisabled(True)
        self.lostButton.setDisabled(True)

        autoSave(self.data)
        writeCsv(self.data)
    
    def givenFromStock(self):
        """ Mark the selected glasses as given from stock """
        self.data = self.loadDataFromCsv()
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 1:
            self.data[num][12] = 2

        self.data[num][13] = date.today()

        self.addButton.setDisabled(False)
        self.removeButton.setDisabled(True)
        self.givenButton.setDisabled(True)
        self.lostButton.setDisabled(True)

        autoSave(self.data)
        writeCsv(self.data)
    
    def lostFromStock(self):
        """ Mark the selected glasses as lost from stock """
        self.data = self.loadDataFromCsv()
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 1:
            self.data[num][12] = 3

        self.addButton.setDisabled(False)
        self.removeButton.setDisabled(True)
        self.givenButton.setDisabled(True)
        self.lostButton.setDisabled(True)

        autoSave(self.data) 
        writeCsv(self.data)

    def search(self):
        """ basic search function """
        self.convert()
        # Fetch query from form
        query = [self.data_structure[i][2]()
                    for i in range(len(self.data_structure))[1:]]

        self.abstractSearch(query)

    def nearSearch(self):
        """ search function for near sight glasses
            do a basic search but add Addition to each Sphere
            also removes all progressive and double focal glasses
            from results """
        self.convert()
        # Fetch query from form
        query = [self.data_structure[i][2]()
                    for i in range(len(self.data_structure))[1:]]
        query[0] += query[3]
        query[4] += query[7]
        query[3] = 0
        query[7] = 0

        self.abstractSearch(query, True)

    def distSearch(self):
        """ search function for distant sight glasses
            do a basic search but take 0 as addition
            also removes all progressive and double focal glasses
            from results """
        self.convert()
        # Fetch query from form
        query = [self.data_structure[i][2]()
                    for i in range(len(self.data_structure))[1:]]
        query[3] = 0
        query[7] = 0

        self.abstractSearch(query, True)

    def abstractSearch(self, query, no_add = False):
        """ abstract search function that actually do the search mecanism """
        # Get database from file
        self.data = self.loadDataFromCsv()
        new_data = dict()

        for num, value in self.data.items():
            score = self.score(value, query)
            if value[12] == 1 and score != 0 and \
               ((not no_add) or value[8] == 0):
                new_data[num] = [score]+value

        self.displayData([[y[0]]+[x]+y[1:] for x, y in new_data.items()])

    def displayData(self, data):
        """ display the search results in the tableview """
        self.model.clear()
        labels = [u'Score'] + [self.data_structure[i][0]
                for i in range(len(self.data_structure))] 
        labels.insert(2, "Boite")
        self.model.setHorizontalHeaderLabels(labels)

        frame = self.getFrame()
        solar = self.getSolar()

        for row in data:
            items = [QtGui.QStandardItem("{0:.2f}%".format(row[0]))]+[
                     QtGui.QStandardItem(self.data_structure[i][1](row[i+1]))
                         for i in range(len(self.data_structure))]

            # For each item, add the data value to allow correct sorting
            for i, item in enumerate(items):
                item.setData(getData(row[i]), SORT_ROLE)

            items[0].setBackground(percentcolor(row[0]))

            items[1].setBackground(QtGui.QColor(UNIT_COLORS[int(str(row[1])[-1])]))

            items[2].setBackground(RIGHT_COLOR)
            items[3].setBackground(RIGHT_COLOR)
            items[4].setBackground(RIGHT_COLOR)
            items[5].setBackground(RIGHT_COLOR)

            items[6].setBackground(LEFT_COLOR)
            items[7].setBackground(LEFT_COLOR)
            items[8].setBackground(LEFT_COLOR)
            items[9].setBackground(LEFT_COLOR)

            box = int(row[1])//NBR_PER_BOX
            box_letter = chr(65+box//4)
            box_number = box % 4 + 1
            box_label = f'''{box_letter}{box_number}'''
            items.insert(2, QtGui.QStandardItem(box_label))

            if row[11] != frame:
                items[11].setBackground(RED_COLOR)

            if row[12] != solar:
                items[12].setBackground(RED_COLOR)

            self.model.appendRow(items)

        self.model.setSortRole(SORT_ROLE)
        self.tableView.sortByColumn(0, QtCore.Qt.DescendingOrder)
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(False)

    def score(self, data, target):
        """ Scoring function, taking into account the selected checkboxes """
        coef_left, coef_right = self.getMasterEyeCoef()
        if not self.lIndifCheckBox.isChecked():
            left_score = eye_score(data[4:8], target[4:8])
        else:
            left_score = 1
        if not self.rIndifCheckBox.isChecked():
            right_score = eye_score(data[0:4], target[0:4])
        else:
            right_score = 1

        return 100 * left_score**coef_left * right_score**coef_right

    def enableAddition(self):
        """ Change the state of both spinboxes in case the link is checked """
        if (self.rAddSpin.value() == 0) and (self.lAddSpin.value() == 0):
            self.addGroupBox.setDisabled(True)
        else:
            self.addGroupBox.setDisabled(False)

        if (self.rAddSpin.value() == 0) and (self.lAddSpin.value() == 0):
            self.nearSearchButton.setDisabled(True)
            self.distantSearchButton.setDisabled(True)
        else:
            self.nearSearchButton.setDisabled(False)
            self.distantSearchButton.setDisabled(False)
        value = self.sender().value()
        if self.rLinkCheckbox.isChecked():
            self.rAddSpin.setValue(value)
            self.lAddSpin.setValue(value)
        self.modified()

    def linkChanged(self):
        """ Link the state of the two checkboxes """
        state = self.sender().isChecked()
        self.lLinkCheckbox.setChecked(state)
        self.rLinkCheckbox.setChecked(state)

    def lIndifChanged(self):
        """ Activate/deactivate the spinboxes """
        state = self.sender().isChecked()
        self.lSphereSpin.setDisabled(state)
        self.lCylSpin.setDisabled(state)
        self.lAxisSpin.setDisabled(state)
        self.lAddSpin.setDisabled(state)
        self.lMasterRadio.setDisabled(state)
        if state:
            self.rMasterRadio.setChecked(state)

    def rIndifChanged(self):
        """ Activate/deactivate the spinboxes """
        state = self.sender().isChecked()
        self.rSphereSpin.setDisabled(state)
        self.rCylSpin.setDisabled(state)
        self.rAxisSpin.setDisabled(state)
        self.rAddSpin.setDisabled(state)
        self.rMasterRadio.setDisabled(state)
        if state:
            self.lMasterRadio.setChecked(state)
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
        self.model.clear()
        self.sender().setStyleSheet("")
        self.rLabelCylPos.setVisible(self.rCylSpin.value() > 0)
        self.lLabelCylPos.setVisible(self.lCylSpin.value() > 0)

    def getMasterEyeCoef(self):
        """ returns the coefficient applied to both eyes score """
        return ((MASTER_EYE_COEF - 1) * int(self.lMasterRadio.isChecked()) + 1,
               (MASTER_EYE_COEF - 1) * int(self.rMasterRadio.isChecked()) + 1)

    def setRSphere(self, value):
        """ set the Right Sphere label to value with proper formatting """
        self.rSphereLabel.setText(formatSph(value))

    def setLSphere(self, value):
        """ set the Left Sphere label to value with proper formatting """
        self.lSphereLabel.setText(formatSph(value))

    def setRCyl(self, value):
        """ set the Right Cylinder label to value with proper formatting """
        self.rCylLabel.setText(formatCyl(value))

    def setLCyl(self, value):
        """ set the Left Cylinder label to value with proper formatting """
        self.lCylLabel.setText(formatCyl(value))

    def setRAxis(self, value):
        """ set the Right Axis label to value with proper formatting """
        self.rAxisLabel.setText(formatAxis(value))

    def setLAxis(self, value):
        """ set the Left Axis label to value with proper formatting """
        self.lAxisLabel.setText(formatAxis(value))

    def setRAdd(self, value):
        """ set the Right Addition label to value with proper formatting """
        self.rAddLabel.setText(formatSph(value))

    def setLAdd(self, value):
        """ set the Left Addition label to value with proper formatting """
        self.lAddLabel.setText(formatSph(value))

    def getSolar(self):
        """ returns the code corresponding to the selected radio button
            0 means normal lenses
            1 means solar lenses
        """
        return int(self.solarRadioYes.isChecked())

    def setSolarLabel(self, value):
        """ set the text corresponding to the solar value
        """
        if value == 0:
            self.solarLabel.setText(u'Non teintés')
        elif value == 1:
            self.solarLabel.setText(u'Teintés')
        else:
            self.solarLabel.setText(u'')

    def setSolar(self, value):
        """ selects the radio button corresponding to the input code
            0 selects normal lenses
            1 selects solar lenses
        """
        if value == 1:
            self.solarRadioYes.setChecked(True)
        else:
            self.solarRadioNo.setChecked(True)

    def setAddType(self, value):
        """ set the text corresponding to the AddType value
        """
        if value == 2:
            self.addLabel.setText(u'Bifocal')
        elif value == 1:
            self.addLabel.setText(u'Progressif')
        else:
            self.addLabel.setText(u'')
    
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

    def setFrameLabel(self, value):
        """ set the text corresponding to the Frame value
        """
        if value == 1:
            self.frameLabel.setText(u'Enfant')
        elif value == 0:
            self.frameLabel.setText(u'Adulte')
        elif value == 2:
            self.frameLabel.setText(u'Demi-lune')
        else:
            self.frameLabel.setText(u'Aucune lunette avec ce numéro')

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

    def setComment(self, value):
        """ write the input value to the comment field """
        self.commentEdit.setPlainText(str(value))

    def convert(self):
        """ convert the data entered if cylinder is positive """
        if self.data_structure[2][2]() > 0:
            self.data_structure[1][3](self.data_structure[1][2]() +
                    self.data_structure[2][2]())
            self.data_structure[2][3](-self.data_structure[2][2]())
            self.data_structure[3][3]((self.data_structure[3][2]()+90) % 180)

        if self.data_structure[6][2]() > 0:
            self.data_structure[5][3](self.data_structure[5][2]() +
                    self.data_structure[6][2]())
            self.data_structure[6][3](-self.data_structure[6][2]())
            self.data_structure[7][3]((self.data_structure[7][2]()+90) % 180)

    def loadData(self, num):
        """ Load data from the self.data variable
            and display it in the stock box """
        self.rLinkCheckbox.setChecked(False)
        if num in self.data:
            for i, element in enumerate(self.data_structure[1:]):
                # if i < len(self.data[num]):
                    element[5](self.data[num][i])
            self.eyeglassesNum.setValue(num)

            if self.data[num][12] == 1:
                self.addButton.setDisabled(True)
                self.removeButton.setDisabled(False)
                self.givenButton.setDisabled(False)
                self.lostButton.setDisabled(False)
            else:
                self.addButton.setDisabled(False)
                self.removeButton.setDisabled(True)
                self.givenButton.setDisabled(True)
                self.lostButton.setDisabled(True)
        else:
            for i, element in enumerate(self.data_structure[1:]):
                element[5](element[4])
            self.addButton.setDisabled(True)
            self.removeButton.setDisabled(True)
            self.givenButton.setDisabled(True)
            self.lostButton.setDisabled(True)
        self.eyeglassesNum.setStyleSheet("QSpinBox { background-color: "+QtGui.QColor(UNIT_COLORS[int(str(self.eyeglassesNum.value())[-1])]).name()+"; }")

    def selectLine(self):
        """ change the eyeglasses number to the selected line in the table """
        row = self.tableView.selectionModel().currentIndex().row()
        self.loadData(int(self.model.item(row, 1).text()))

    def reset(self):
        """ Reset the values in the form to the default values """
        self.rMasterRadio.setChecked(True)

        self.rSphereSpin.setValue(DEFAULT_SPHERE)
        self.rCylSpin.setValue(DEFAULT_CYL)
        self.rAxisSpin.setValue(DEFAULT_AXIS)
        self.rAddSpin.setValue(DEFAULT_ADD)
        self.lSphereSpin.setValue(DEFAULT_SPHERE)
        self.lCylSpin.setValue(DEFAULT_CYL)
        self.lAxisSpin.setValue(DEFAULT_AXIS)
        self.lAddSpin.setValue(DEFAULT_ADD)

        self.childRadioNo.setChecked(True)
        self.solarRadioNo.setChecked(True)

        self.rFineCheckbox.setChecked(False)
        self.lFineCheckbox.setChecked(False)

        self.rLinkCheckbox.setChecked(True)
        self.lLinkCheckbox.setChecked(True)

        self.rIndifCheckBox.setChecked(False)
        self.lIndifCheckBox.setChecked(False)
        self.model.clear()

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = MainWindow()
#     mainWin.inventoryWindowButton.hide()
#     mainWin.show()
#     sys.exit(app.exec_())
