# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt4 import QtGui

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

class dotSpinBox(QtGui.QDoubleSpinBox):
    """ Spinbox that display values with the following convention:
        - dot separator 
        - always show 2 decimals
        - show + and - signs
        
        examples:
            0.00
            +3.50
            -4.25 """
            
    def textFromValue(self, value):
        return formatSph(value)