# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QTimer

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
            out = int(text.replace("°", ""))
        except:
            out = 180
        return out

    def validate(self, text, num):
        if self.valueFromText(text) % self.singleStep() == 0:
            return (QtGui.QValidator.Acceptable, text, num)
        else:
            return (QtGui.QValidator.Intermediate, text, num)
    
    def fixup(self, text):
        try:
            text = int(round(self.valueFromText(text) / self.singleStep()) * self.singleStep())
            self.setValue(text)
        except:
            text = text
        return str(text)

    def focusInEvent(self, event):
        super(angleSpinBox, self).focusInEvent(event)
        QTimer.singleShot(0, self.selectAll)
