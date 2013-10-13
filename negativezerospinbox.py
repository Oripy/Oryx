# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt4 import QtGui

from formatting import formatCyl

class negativeZeroSpinBox(QtGui.QDoubleSpinBox):
    """ Spinbox that display values with the following convention:
        - dot separator 
        - always show 2 decimals
        - zero is always negative
        - between brackets
        
        examples:
            (-0.00)
            (3.50)
            (-4.25) """   
    def textFromValue(self, value):
        return formatCyl(value)
