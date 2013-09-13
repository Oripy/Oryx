# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt4 import QtGui

def formatCyl(value):
    """ Ensure that the values are shown with 2 decimals
        and that -0.00 is displayed with a negative sign 
        (-0.00) 
        (-4.50
        (-3.75)     """
    value = float(value)
    if value == 0:
        return '(-0.00)'
    else:
        return '(%0.2f)' % value

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
