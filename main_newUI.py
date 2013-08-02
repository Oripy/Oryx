# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:52:58 2013

@author: pmaurier
"""

from PyQt4 import QtCore, QtGui

from inventoryUI import Ui_MainWindow 

import csv
import time

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

###########################################

######## Text formating functions #########
    
from anglespinbox import formatAxis
from negativezerospinbox import formatCyl

def formatType(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Progressif'
    elif value == 2:
        return u'Bifocal'
    elif value == 3:
        return u'Trifocal'
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
    else:
        return u'Adulte'    

def getData(value):
    """ returns an int, float or string depending on the input type """
    try:
        out = int(value)
    except:
        try:
            out = float(value)
        except:
            out = value
    return out

###########################################

############## Main Window ################

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super(Ui_MainWindow, self).__init__()
        
        self.setupUi(self)
        self.initUI()
        
        self.currentNum = self.eyeglassesNum.value()
        self.modif = False
        
        # Data Structure (Name, formating function, get function, 
        #                 set function, default value)
        self.dataStructure = [
            ['Num', lambda n: str(int(n)), self.eyeglassesNum.value, 
             self.eyeglassesNum.setValue, 1],
            ['OD Sphere', lambda n: '%0.2f' % float(n), 
             self.rSphereSpin.value, self.rSphereSpin.setValue, DEFAULT_SPHERE],
            ['OD Cylindre', formatCyl, self.rCylSpin.value, 
             self.rCylSpin.setValue, DEFAULT_CYL],
            ['OD Axe', formatAxis, self.rAxisSpin.value, 
             self.rAxisSpin.setValue, DEFAULT_AXIS],
            ['OD Add', lambda n: '%0.2f' % float(n), self.rAddSpin.value, 
             self.rAddSpin.setValue, DEFAULT_ADD],
            ['OG Sphere', lambda n: '%0.2f' % float(n), self.lSphereSpin.value, 
             self.lSphereSpin.setValue, DEFAULT_SPHERE],
            ['OG Cylindre', formatCyl, self.lCylSpin.value, 
             self.lCylSpin.setValue, DEFAULT_CYL],
            ['OG Axe', formatAxis, self.lAxisSpin.value, 
             self.lAxisSpin.setValue, DEFAULT_AXIS],
            ['OG Add', lambda n: '%0.2f' % float(n), self.lAddSpin.value, 
             self.lAddSpin.setValue, DEFAULT_ADD],
            ['Type', formatType, self.getAddType, 
             self.setAddType, 0],
            ['Monture', formatFrame, self.getFrame, 
             self.setFrame, 0],
            ['Teinte', formatSun, self.getSolar, 
             self.setSolar, 0],
            ['Commentaire', lambda n: unicode(n, encoding='latin_1'), self.getComment, 
             self.setComment, ''],
            ['Stock', lambda n: str(int(n)), lambda: 1, 
             lambda n: n, 1]]
             
        self.data = dict()
        self.model = QtGui.QStandardItemModel(self)
        
        self.loadCsv(FILENAME)
        self.loadData()
        self.new()
        

    def initUI(self):
        """ create actions and default values of the interface """
        # List actions and create the menubar
        self.exitAction.triggered.connect(QtGui.qApp.quit)
        self.saveAction.triggered.connect(self.save)
        self.newAction.triggered.connect(self.new)
               
        # Numbering/Actions panel
        self.eyeglassesNum.valueChanged.connect(self.warnModified)
        
        self.currentNum = self.eyeglassesNum.value()
        self.eyeglassesNum.noWarn = False
        
        self.saveButton.clicked.connect(self.saveAction.trigger)
        self.newButton.clicked.connect(self.newAction.trigger)
        
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
              
        # Addition        
        self.addRadioP.toggled.connect(self.modified)
        self.addRadioBF.toggled.connect(self.modified)
        self.addRadioTF.toggled.connect(self.modified)
               
        # Comments
        self.commentEdit.textChanged.connect(self.modified)

        # Solar        
        self.solarRadioNo.toggled.connect(self.modified)
        self.solarRadioYes.toggled.connect(self.modified)

        # Frame
        self.childRadioNo.toggled.connect(self.modified)
        self.childRadioYes.toggled.connect(self.modified)
        
        # Table
        self.tableView.doubleClicked.connect(self.selectLine)
            
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
        self.setStatus('Modified')
        self.modif = True
    
    def getFirstNewNumber(self):
        n = 1
        while self.data.has_key(n):
            n += 1
        return n
    
    def new(self):
        """ set the number to the smallest available eyeglasses number """
        n = self.getFirstNewNumber()
        if n != self.currentNum:
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
            3 means Trifocal
        """
        if (self.rAddSpin.value() != 0) or (self.lAddSpin.value() != 0):
            if self.addRadioP.isChecked():
                return 1
            elif self.addRadioBF.isChecked():
                return 2
            else:
                return 3
        else:
            return 0
    
    def setAddType(self, value):
        """ selects the radio button corresponding to the input code
            0 or 1 selects Progressive
            2 selects Bifocal
            3 selects Trifocal
        """
        if value == 2:
            self.addRadioBF.setChecked(True)
        elif value == 3:
            self.addRadioTF.setChecked(True)
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
            
    def getFrame(self):
        """ returns the code corresponding to the selected radio button
            0 means adult frame
            1 means child frame
        """
        return int(self.childRadioYes.isChecked())
    
    def setFrame(self, value):
        """ selects the radio button corresponding to the input code
            0 selects adult frame
            1 selects child frame
        """
        if value == 1:
            self.childRadioYes.setChecked(True)
        else:
            self.childRadioNo.setChecked(True)
            
    def getComment(self):
        """ returns the comment formated to suitable codec """
        return self.commentEdit.toPlainText().toLatin1()
    
    def setComment(self, value):
        """ write the input value to the comment field """
        self.commentEdit.setPlainText(unicode(value, encoding='latin_1'))
    
    def save(self):
        """ Save the modifications and write it to the CSV file """
        item = [QtGui.QStandardItem(str(self.currentNum))] \
               + [QtGui.QStandardItem( \
                   self.dataStructure[i][1](self.dataStructure[i][2]()) \
                   ) for i in range(len(self.dataStructure))[1:]]
        if not self.data.has_key(self.currentNum):
            # Add a line to the table if the current item do not exists
            self.model.appendRow(item)
        else:
            # Alter the existing line
            rows = self.model.findItems(str(self.currentNum))
            if len(rows) == 1:
                row = rows[0].row()
                for column, elem in enumerate(item):
                    self.model.setItem(row, column, elem)
            else:
                print "Error when trying to update the TableView"
        if self.modif:
            self.data[self.currentNum] = [self.dataStructure[i][2]()
                          for i in range(len(self.dataStructure))[1:]]
            self.writeCvs(FILENAME)    
            self.setStatus('Saved')
            self.modif = False
        self.scrollTo(self.currentNum)
    
    def loadData(self):
        """ Load data from the self.data variable
            and display it in the form """
        self.rLinkCheckbox.setChecked(False)
        if self.data.has_key(self.currentNum):
            for i, element in enumerate(self.dataStructure[1:]):
                element[3](self.data[self.currentNum][i])
            self.modif = False
            self.setStatus('Saved')
        else:
            self.reset()

        if self.rAddSpin.value() == self.lAddSpin.value():
            self.rLinkCheckbox.setChecked(True)
    
        self.scrollTo(self.currentNum)
    
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
        self.currentNum = int(self.model.item(row, 0).text())
        self.eyeglassesNum.setValue(self.currentNum)

    def reset(self):
        """ Reset the values in the form to the default values """
        for element in self.dataStructure[1:]:
            element[3](element[4])        
        self.modif = False
        
        self.setStatus('New')
    
    def setStatus(self, value):
        """ Display the current status (Saved/Modified/New)
            with different colors """
        if value == 'Saved':
            self.status.setText(u'Sauvegardé')
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

    def warnModified(self):
        """ Warn the user that unsaved data will be lost if unsaved """      
        if not(self.eyeglassesNum.noWarn):
            if self.modif:
                text = (u'Les lunettes '+str(self.currentNum)+' '
                        u'n\'ont pas été enregistrées.\n'
                        u'Voulez-vous sauvegarder les changements ?')
                question = QtGui.QMessageBox.warning(self, u'Sauvegarde',
                    text,
                    QtGui.QMessageBox.Save,
                    QtGui.QMessageBox.Discard,
                    QtGui.QMessageBox.Cancel)
                if question == QtGui.QMessageBox.Save:
                    self.save()
                    self.reset()
                    self.currentNum = min(self.getFirstNewNumber(), self.eyeglassesNum.value())
                    self.eyeglassesNum.setValue(self.currentNum)
                    self.loadData()
                    return 'Saved'
                elif question == QtGui.QMessageBox.Discard:
                    self.currentNum = min(self.getFirstNewNumber(), self.eyeglassesNum.value())
                    self.eyeglassesNum.setValue(self.currentNum)
                    self.loadData()
                    return 'Discarded'
                else:
                    if self.sender() != None:
                        self.eyeglassesNum.noWarn = True
                    self.eyeglassesNum.setValue(self.currentNum)
                    return 'Canceled'
            else:
                self.currentNum = min(self.getFirstNewNumber(), self.eyeglassesNum.value())
                self.eyeglassesNum.setValue(self.currentNum)
                self.loadData()
        else:
            self.eyeglassesNum.noWarn = False
            return 'Saved'

    def loadCsv(self, fileName):
        """ Load data from the CSV file and displays it in the table """
        deb = time.time()
        print 'Creating model...'
        self.model.clear()
        self.model.setHorizontalHeaderLabels([self.dataStructure[i][0]
                          for i in xrange(len(self.dataStructure))])
        fin = time.time()
        print '%0.2f sec' % float(fin-deb)
        deb = fin
        print 'Loading data...'
        with open(fileName, "rb") as fileInput:
            for row in csv.reader(fileInput):
                items = [QtGui.QStandardItem(self.dataStructure[i][1](row[i])) 
                          for i in xrange(len(self.dataStructure))]
                self.model.appendRow(items)
                
                self.data[int(row[0])] = [getData(row[a])
                          for a in range(len(self.dataStructure))[1:]]
        fin = time.time()
        print '%0.2f sec' % float(fin-deb)
        deb = fin
        print 'Populating table...'
        self.tableView.setModel(self.model)        
        fin = time.time()
        print '%0.2f sec' % float(fin-deb)
        deb = fin
        print 'Resizing columns...'
        self.tableView.resizeColumnsToContents()
        fin = time.time()
        print '%0.2f sec' % float(fin-deb)
        
    def writeCvs(self, fileName):
        """ Write data in the CSV file """
        with open(fileName, "wb") as fileInput:
            dataWriter = csv.writer(fileInput)
            for key, values in self.data.iteritems():
                dataWriter.writerow([key]+values)

###########################################

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
