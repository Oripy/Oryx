# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt5 import QtGui, QtWidgets

from formatting import formatAxis

class angleSpinBox(QtWidgets.QSpinBox):
    """ Spinbox that display values with the following convention:
        - always show 3 digits
        - append a "°"

        examples:
            005°
            015°
            155° """
    def textFromValue(self, value):
        return formatAxis(value)

    def valueFromText(self, text):
        try:
            out = int(text[0:3])
            if out % 5 >= 3:
                out = out / 5 * 5 + 5
            else:
                out = out / 5 * 5
        except:
            out = 180
        return out

    def validate(self, text, num):
        if self.valueFromText(text) % 5 == 0:
            return (QtGui.QValidator.Acceptable, text, num)
        else:
            return (QtGui.QValidator.Intermediate, text, num)
