# -*- coding: utf-8 -*-
"""
Created on Fri Aug 02 17:19:43 2013

@author: pmaurier
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from formatting import formatSph

class dotSpinBox(QtWidgets.QDoubleSpinBox):
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

    def focusInEvent(self, event):
        super(dotSpinBox, self).focusInEvent(event)
        QTimer.singleShot(0, self.selectAll)
