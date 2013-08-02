# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt4 import QtGui

def formatAxis(value):
    """ Ensure that 3 digits are displayed 
        and append a "°" at the end
        005°
        045°
        180°       """
    value = float(value)
    return u'%03d°' % value

class angleSpinBox(QtGui.QSpinBox):
    """ Spinbox that display values with the following convention:
        - always show 3 digits
        - append a "°"
        
        examples:
            005°
            015°
            155° """
    def textFromValue(self, value):
        return formatAxis(value)

