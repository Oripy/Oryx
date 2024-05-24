# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:12:10 2013

@author: pierre
"""

from PyQt5 import QtCore, QtGui
from datetime import datetime

from config import *

# Color constants
RED_PALETTE = QtGui.QPalette()
RED_PALETTE.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)

RIGHT_COLOR = QtGui.QColor(QtCore.Qt.green).lighter(180)
LEFT_COLOR = QtGui.QColor(QtCore.Qt.red).lighter(180)

RED_COLOR = QtGui.QColor(QtCore.Qt.red).lighter(125)
YELLOW_COLOR = QtGui.QColor(QtCore.Qt.yellow).lighter(125)
BLUE_COLOR = QtGui.QColor(QtCore.Qt.blue).lighter(125)
GREEN_COLOR = QtGui.QColor(QtCore.Qt.green).lighter(125)

STATUS_COLOR = [RED_COLOR, GREEN_COLOR, BLUE_COLOR, YELLOW_COLOR]

def getBoxNum(value):
    box = value//NBR_PER_BOX
    box_letter = chr(65+box//6)
    box_number = box % 6 + 1
    return f'''{box_letter}{box_number}'''

def percentcolor(value):
    """ returns a color between green and red based on the value """
    return QtGui.QColor(int(255*(100-value)/100), int(255*value/100), 0, 128)

def formatSph(value):
    """ Ensure that the values are shown with 2 decimals
        and that + and - sign is always visible
        0.00
        +4.50
        -3.75     """
    value = float(value)
    if value == 0:
        return '0.00'
    elif value > 0:
        return '+%0.2f' % value
    else:
        return '%0.2f' % value

def formatCyl(value):
    """ Ensure that the values are shown with 2 decimals
        and that -0.00 is displayed with a negative sign
        (-0.00)
        (-4.50
        (-3.75)     """
    value = float(value)
    if value == 0:
        return '(-0.00)'
    elif value < 0:
        return '(%0.2f)' % value
    else:
        return '(+%0.2f)' % value

def formatAxis(value):
    """ Ensure that 3 digits are displayed
        and append a "°" at the end
        005°
        045°
        180°       """
    value = float(value)
    return u'%03d°' % value

def formatType(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Pr'
    elif value == 2:
        return u'Bf'
    else:
        return u''

def formatSun(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'TT'
    else:
        return u'NT'

def formatFrame(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 1:
        return u'Enf'
    elif value == 2:
        return u'DL'
    else:
        return u'Adult'
    
def formatStock(value):
    """ Convert saved numbers into respective human readable text """
    value = float(value)
    if value == 2:
        return u'Donnée'
    elif value == 1:
        return u'Stock'
    elif value == 3:
        return u'Egarée'
    elif value == 0:
        return u'Supprimée'

def formatDate(value):
    if value == 0:
        return ""
    if isinstance(value, str):
        return datetime.strftime(datetime.strptime(value, '%Y-%m-%d'), '%Y-%m-%d')
    else:
        return datetime.strftime(value, '%Y-%m-%d')

def getData(value):
    """ returns a float or string depending on the input type """
    try:
        out = float(value)
    except ValueError:
        out = value
    return out
