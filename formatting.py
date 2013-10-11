# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:12:10 2013

@author: pierre
"""

from PyQt4 import QtCore, QtGui

from anglespinbox import formatAxis
from negativezerospinbox import formatCyl
from dotspinbox import formatSph

# Color constants
RED_PALETTE = QtGui.QPalette()
RED_PALETTE.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)

RIGHT_COLOR = QtGui.QColor(QtCore.Qt.green).lighter(180)
LEFT_COLOR = QtGui.QColor(QtCore.Qt.red).lighter(180)

RED_COLOR = QtGui.QColor(QtCore.Qt.red).lighter(125)

def percentcolor(value):
    """ returns a color between green and red based on the value """
    return QtGui.QColor(int(255*(100-value)/100), int(255*value/100), 0, 128)

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
    except ValueError:
        out = value
    return out