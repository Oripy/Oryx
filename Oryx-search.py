# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:52:58 2013

@author: pmaurier
"""

from PyQt4 import QtCore, QtGui

from searchUI import Ui_MainWindow 

import csv

############## Configuration ##############
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

def configSectionMap(section):
    """ Retreive values from a section of the config file
        return: a dictionnary containing all key: value from the section """
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print 'skip: %s' % option
        except:
            print 'exception on %s!' % option
            dict1[option] = None
    return dict1
    
FILENAME = configSectionMap('Main')['filename']

try:
    with open(FILENAME):
        pass
except IOError:
    # Create the file
    f = open(FILENAME, 'w+')
    f.write('')
    f.close()

correction = configSectionMap('Correction')

MAX_SPHERE = float(correction['max_sphere'])
MIN_SPHERE = float(correction['min_sphere'])
STEP_SPHERE = float(correction['step_sphere'])
DEFAULT_SPHERE = float(correction['default_sphere'])

MAX_CYL = float(correction['max_cyl'])
MIN_CYL = float(correction['min_cyl'])
STEP_CYL = float(correction['step_cyl'])
DEFAULT_CYL = float(correction['default_cyl'])

MAX_AXIS = float(correction['max_axis'])
MIN_AXIS = float(correction['min_axis'])
STEP_AXIS = float(correction['step_axis'])
DEFAULT_AXIS = float(correction['default_axis'])

MAX_ADD = float(correction['max_add'])
MIN_ADD = float(correction['min_add'])
STEP_ADD = float(correction['step_add'])
DEFAULT_ADD = float(correction['default_add'])

search = configSectionMap('Search')

MASTER_EYE_COEF = float(search['master_eye_coef'])

SPHERE_DELTA_MAX = float(search['sphere_delta_max'])+.25
SPHERE_DELTA_MIN = float(search['sphere_delta_min'])-.25

CYL_DELTA_MAX = float(search['cyl_delta_max'])+.25
CYL_DELTA_MIN = float(search['cyl_delta_min'])-.25

PARAM_AXIS_TOL0 = float(search['param_axis_tol0'])
PARAM_AXIS_TOL1 = float(search['param_axis_tol1'])
PARAM_AXIS_TOL2 = float(search['param_axis_tol2'])

ADD_DELTA_MAX = float(search['add_delta_max'])

SPHERE_COEF = float(search['sphere_coef'])
CYL_COEF = float(search['cyl_coef'])
AXIS_COEF = float(search['axis_coef'])
ADD_COEF = float(search['add_coef'])

###########################################

######## Text formating functions #########
    
from anglespinbox import formatAxis
from negativezerospinbox import formatCyl
from dotspinbox import formatSph

def formatType(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Progressif'
    elif value == 2:
        return u'Bifocal'
    else:
        return u''

def formatSun(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Teintés'
    else:
        return u'Non teintés'

def formatFrame(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Enfant'
    elif value == 2:
        return u'Demi-lunes'
    else:
        return u'Adulte'    

def getData(value):
    """ returns a float or string depending on the input type """
    try:
        out = float(value)
    except:
        out = value
    return out

redPalette = QtGui.QPalette()
redPalette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)

rightcolor = QtGui.QColor(QtCore.Qt.green).lighter(180)
leftcolor = QtGui.QColor(QtCore.Qt.red).lighter(180)

def percentcolor(value):
    return QtGui.QColor(int(255*(100-value)/100), int(255*value/100), 0, 128)

###########################################

######## Score related functions #########

def scoringFunction(delta, minimum, maximum):
    if delta >= 0:
        return max(-(delta/maximum)**2 + 1, 0)
    else:
        return max(-(delta/minimum)**2 + 1, 0)

def eye_score(data, target):
    s = score_sphere(data, target)
    c = score_cyl(data, target)
    a = score_axis(data, target)
    p = score_add(data, target)
    score = (s**SPHERE_COEF)*(c**CYL_COEF)*(a**AXIS_COEF)*(p**ADD_COEF)
    return score
    
def sphericalEquivalentRefraction(data, target):
    delta_cyl = target[1] - data[1]
    return target[0] - delta_cyl/2 + (delta_cyl/2 % .25)
    
def score_sphere(data, target):
    if (data[0] < 0 and target[0] > 0) or (data[0] > 0 and target[0] < 0):
        return 0
    delta_sph = sphericalEquivalentRefraction(data, target) - data[0]
    if data[0] >= 0:
        score = scoringFunction(delta_sph, SPHERE_DELTA_MIN, SPHERE_DELTA_MAX)
    else:
        score = scoringFunction(delta_sph, -SPHERE_DELTA_MAX, -SPHERE_DELTA_MIN)
    return score
    
def score_cyl(data, target):
    delta_cyl = target[1] - data[1]
    return scoringFunction(delta_cyl, CYL_DELTA_MIN, CYL_DELTA_MAX)
    
def score_axis(data, target):
    # if no cylinder correction, axis is not taken into account
    if (data[1] == 0) or (target[1] == 0):
        return 1
    tolerance = PARAM_AXIS_TOL2*data[1]**2+PARAM_AXIS_TOL1*data[1]+PARAM_AXIS_TOL0
    tolerance = tolerance - (tolerance % 5) + (5 if (tolerance % 5) >= 2.5 else 0)
    
    delta_axis = (target[2] - data[2])
    delta_axis = abs((delta_axis + 90) % 180 - 90)
    if delta_axis > tolerance:
        return 0
    else:
        return -(delta_axis/tolerance)**2 + 1
    
def score_add(data, target):
    if target[3] == 0 and data[3] != 0:
        return 0
    delta_add = target[3] - data[3]
    return scoringFunction(delta_add, -ADD_DELTA_MAX, target[3]+0.25)
    
sortRole = QtCore.Qt.UserRole + 1

###########################################

############## Main Window ################

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        
        self.setupUi(self)
        self.initUI()
        
        self.setWindowState(QtCore.Qt.WindowMaximized)  
        
        # Data Structure (Name, formating function, get function, 
        #                 set function, default value)
        self.dataStructure = [
            ['Num', lambda n: str(int(n)), lambda: 1,
             lambda n: n, 1, self.eyeglassesNum.setValue],
            ['OD Sphere', formatSph, self.rSphereSpin.value,
             self.rSphereSpin.setValue, DEFAULT_SPHERE, self.setRSphere],
            ['OD Cylindre', formatCyl, self.rCylSpin.value, 
             self.rCylSpin.setValue, DEFAULT_CYL, self.setRCyl],
            ['OD Axe', formatAxis, self.rAxisSpin.value, 
             self.rAxisSpin.setValue, DEFAULT_AXIS, self.setRAxis],
            ['OD Add', formatSph, self.rAddSpin.value, 
             self.rAddSpin.setValue, DEFAULT_ADD, self.setRAdd],
            ['OG Sphere', formatSph, self.lSphereSpin.value,
             self.lSphereSpin.setValue, DEFAULT_SPHERE, self.setLSphere],
            ['OG Cylindre', formatCyl, self.lCylSpin.value, 
             self.lCylSpin.setValue, DEFAULT_CYL, self.setLCyl],
            ['OG Axe', formatAxis, self.lAxisSpin.value, 
             self.lAxisSpin.setValue, DEFAULT_AXIS, self.setLAxis],
            ['OG Add', formatSph, self.lAddSpin.value, 
             self.lAddSpin.setValue, DEFAULT_ADD, self.setLAdd],
            ['Multifocal', formatType, lambda: 0, 
             lambda n: n, 0, self.setAddType],
            ['Monture', formatFrame, self.getFrame, 
             self.setFrame, -1, self.setFrameLabel],
            ['Teinte', formatSun, self.getSolar, 
             self.setSolar, -1, self.setSolarLabel],
            ['Commentaire', lambda n: unicode(n, encoding='latin_1'),
             lambda: '', lambda n: n, '', self.setComment],
            ['Stock', lambda n: str(int(n)), lambda: 1, 
             lambda n: n, 1, lambda n: n]
            ]
             
        self.data = dict()
        self.model = QtGui.QStandardItemModel(self)
        self.tableView.setModel(self.model)     
        
        self.loadCsv(FILENAME)
        self.loadData(self.eyeglassesNum.value())
        self.tableView.sortByColumn(1, QtCore.Qt.AscendingOrder)

    def initUI(self):
        """ create actions and default values of the interface """
        self.exitAction.triggered.connect(QtGui.qApp.quit)
        self.searchAction.triggered.connect(self.search)
        self.distantSearchAction.triggered.connect(self.distSearch)
        self.nearSearchAction.triggered.connect(self.nearSearch)
        self.resetAction.triggered.connect(self.reset)
        
        self.searchButton.clicked.connect(self.searchAction.trigger)
        self.distantSearchButton.clicked.connect(self.distantSearchAction.trigger)
        self.nearSearchButton.clicked.connect(self.nearSearchAction.trigger)
        self.resetButton.clicked.connect(self.resetAction.trigger)
        self.addButton.clicked.connect(self.addToStock)
        self.removeButton.clicked.connect(self.removeFromStock)
        
        # Right Eye
        self.rMasterRadio.toggled.connect(self.modified)
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
        self.rLabelCylPos.setPalette(redPalette)
        
        self.rAxisSpin.setMaximum(MAX_AXIS)
        self.rAxisSpin.setMinimum(MIN_AXIS)
        self.rAxisSpin.setSingleStep(STEP_AXIS)
        self.rAxisSpin.setValue(DEFAULT_AXIS)
        self.rAxisSpin.valueChanged.connect(self.modified)
        
        self.rAddSpin.setMaximum(MAX_ADD)
        self.rAddSpin.setMinimum(MIN_ADD)
        self.rAddSpin.setSingleStep(STEP_ADD)
        self.rAddSpin.setValue(DEFAULT_ADD)
        self.rAddSpin.valueChanged.connect(self.enableAddition)
        
        self.rLinkCheckbox.stateChanged.connect(self.linkChanged)
        
        # Left Eye
        self.lMasterRadio.toggled.connect(self.modified)
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
        self.lLabelCylPos.setPalette(redPalette)
        
        self.lAxisSpin.setMaximum(MAX_AXIS)
        self.lAxisSpin.setMinimum(MIN_AXIS)
        self.lAxisSpin.setSingleStep(STEP_AXIS)
        self.lAxisSpin.setValue(DEFAULT_AXIS)
        self.lAxisSpin.valueChanged.connect(self.modified)
        
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

    def addToStock(self):
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 0:
            self.data[num][12] = 1
            
        self.addButton.setDisabled(True)
        self.removeButton.setDisabled(False)
        
        self.writeCsv(FILENAME)

    def removeFromStock(self):
        num = self.eyeglassesNum.value()
        if self.data[num][12] == 1:
            self.data[num][12] = 0
            
        self.addButton.setDisabled(False)
        self.removeButton.setDisabled(True)
        
        self.writeCsv(FILENAME)

    def search(self):        
        self.convert()        
        # Fetch query from form
        query = [self.dataStructure[i][2]()
                    for i in range(len(self.dataStructure))[1:]]
        
        self.abstractSearch(query)
        
    def nearSearch(self):
        self.convert()
        # Fetch query from form
        query = [self.dataStructure[i][2]()
                    for i in range(len(self.dataStructure))[1:]]
        query[1] += query[4]
        query[5] += query[8]
        query[4] = 0
        query[8] = 0
        
        self.abstractSearch(query)
    
    def distSearch(self):
        self.convert()
        # Fetch query from form
        query = [self.dataStructure[i][2]()
                    for i in range(len(self.dataStructure))[1:]]
        query[4] = 0
        query[8] = 0
        
        self.abstractSearch(query)
    
    def abstractSearch(self, query):
        # Get database from file
        self.loadCsv(FILENAME)
        
        new_data = dict()
        
        for num, value in self.data.iteritems():
            if value[12] == 1:
                new_data[num] = [self.score(value, query)]+value
        
        self.displayData([[y[0]]+[x]+y[1:] for x, y in new_data.iteritems()])
    
    def displayData(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels([u'Score']+[self.dataStructure[i][0]
          for i in xrange(len(self.dataStructure))])
        
        for row in data:
            items = [QtGui.QStandardItem("{0:.2f}%".format(row[0]))]+[
                     QtGui.QStandardItem(self.dataStructure[i][1](row[i+1])) 
                         for i in xrange(len(self.dataStructure))]
            
            # For each item, add the data value to allow correct sorting
            for i, item in enumerate(items):
                item.setData(getData(row[i]), sortRole)
            
            items[0].setBackground(percentcolor(row[0]))
            
            items[2].setBackground(rightcolor)
            items[3].setBackground(rightcolor)
            items[4].setBackground(rightcolor)
            items[5].setBackground(rightcolor)
            
            items[6].setBackground(leftcolor)
            items[7].setBackground(leftcolor)
            items[8].setBackground(leftcolor)
            items[9].setBackground(leftcolor)
            
            self.model.appendRow(items)
            
            self.model.setSortRole(sortRole)
            self.tableView.sortByColumn(0, QtCore.Qt.DescendingOrder)           
            self.tableView.resizeColumnsToContents()
    
    def score(self, data, target):
        # Frame
        if data[10] != target[10]:
            return 0
        
        # Sun
        if data[11] != target[11]:
            return 0
        
        # Correction
        mLeft, mRight = self.getMasterEyeCoef()
        lScore = eye_score(data[4:8], target[4:8])
        rScore = eye_score(data[0:4], target[0:4])
        score = 100 * lScore**mLeft * rScore**mRight
        return score

    def enableAddition(self):
        """ Change the state of both spinboxes in case the link is checked """
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
        
    def modified(self):
        """ Action when a value is modified """
        self.model.clear()
        self.rLabelCylPos.setVisible(self.rCylSpin.value() > 0)
        self.lLabelCylPos.setVisible(self.lCylSpin.value() > 0)
    
    def getMasterEyeCoef(self):
        """ returns the coefficient applied to both eyes score """
        mLeft = (MASTER_EYE_COEF-1) * int(self.lMasterRadio.isChecked()) + 1
        mRight = (MASTER_EYE_COEF-1) * int(self.rMasterRadio.isChecked()) + 1
        return mLeft, mRight
        
    def setRSphere(self, value):
        self.rSphereLabel.setText(formatSph(value))
    
    def setLSphere(self, value):
        self.lSphereLabel.setText(formatSph(value))
        
    def setRCyl(self, value):
        self.rCylLabel.setText(formatCyl(value))
    
    def setLCyl(self, value):
        self.lCylLabel.setText(formatCyl(value))
       
    def setRAxis(self, value):
        self.rAxisLabel.setText(formatAxis(value))
    
    def setLAxis(self, value):
        self.lAxisLabel.setText(formatAxis(value))
    
    def setRAdd(self, value):
        self.rAddLabel.setText(formatSph(value))
    
    def setLAdd(self, value):
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
            self.solarLabel.setText(u'Non teinté')
        elif value == 1:
            self.solarLabel.setText(u'Teinté')
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
            self.frameLabel.setText(u'Aucune lunettes avec ce numéro')
    
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
        pass
        self.commentEdit.setPlainText(unicode(value, encoding='latin_1'))
    
    def convert(self):
        """ convert the data entered if cylinder is positive """
        if self.dataStructure[2][2]() > 0:
            self.dataStructure[1][3](self.dataStructure[1][2]()+self.dataStructure[2][2]())
            self.dataStructure[2][3](-self.dataStructure[2][2]())
            self.dataStructure[3][3]((self.dataStructure[3][2]()+90) % 180)
        
        if self.dataStructure[6][2]() > 0:
            self.dataStructure[5][3](self.dataStructure[5][2]()+self.dataStructure[6][2]())
            self.dataStructure[6][3](-self.dataStructure[6][2]())
            self.dataStructure[7][3]((self.dataStructure[7][2]()+90) % 180)
                 
    def loadData(self, num):
        """ Load data from the self.data variable
            and display it in the stock box """
        self.rLinkCheckbox.setChecked(False)
        if self.data.has_key(num):
            for i, element in enumerate(self.dataStructure[1:]):
                element[5](self.data[num][i])
            self.eyeglassesNum.setValue(num)
            
            if self.data[num][12] == 1:
                self.addButton.setDisabled(True)
                self.removeButton.setDisabled(False)
            else:
                self.addButton.setDisabled(False)
                self.removeButton.setDisabled(True)
        else:
            for i, element in enumerate(self.dataStructure[1:]):
                element[5](element[4])
            self.addButton.setDisabled(True)
            self.removeButton.setDisabled(True)
    
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
        
        self.rLinkCheckbox.setChecked(True)
        self.lLinkCheckbox.setChecked(True)
        self.model.clear()

    def loadCsv(self, fileName):
        """ Load data from the CSV file and displays it in the table """
        self.data = dict()
        with open(fileName, "rb") as fileInput:
            for row in csv.reader(fileInput):               
                self.data[int(row[0])] = [getData(row[a])
                          for a in range(len(self.dataStructure))[1:]]
        
    def writeCsv(self, fileName):
        """ Write data in the CSV file """
        with open(fileName, "wb") as fileInput:
            dataWriter = csv.writer(fileInput)
            for key, values in self.data.iteritems():
                dataWriter.writerow([key]+values)
        
###########################################

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
#    splash = QtGui.QSplashScreen(QtGui.QPixmap("splash.jpg"))
#    splash.show()
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
