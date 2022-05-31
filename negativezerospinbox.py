# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtGui import QRegExpValidator

from formatting import formatCyl

class negativeZeroSpinBox(QtWidgets.QDoubleSpinBox):
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
    
    def valueFromText(self, text):
        try:
            return float(text.replace("(","").replace(")",""))
        except:
            return super().valueFromText(text)

    def focusInEvent(self, event):
        super(negativeZeroSpinBox, self).focusInEvent(event)
        QTimer.singleShot(0, self.selectAll)

    def validate(self, input, pos):
        steps = "0{1,2}"
        increment = self.singleStep()*100
        while True:
            steps += f"|{increment:.0f}"
            increment += self.singleStep()*100
            if increment % 100 == 0:
                break
        rx = QRegExp(f"^\(?(\+|-)?[0-9]*[.,]?({steps})?\)?$")
        validator = QRegExpValidator(rx, self)
        state = validator.validate(input, pos)
        return state

    def fixup(self, text):
        text = text.replace(",", ".")
        try:
            text = round(float(text)*1/self.singleStep())/(1/self.singleStep())
            self.setValue(text)
        except:
            text = text
        return str(text)
