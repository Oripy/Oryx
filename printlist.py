# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:30:21 2013

@author: pmaurier
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport, uic

# from printUI import Ui_Dialog
Ui_Dialog = uic.loadUiType("print.ui")[0]

import os, time

NormalFormat = QtGui.QTextCharFormat()

ItalicFormat = QtGui.QTextCharFormat()
ItalicFormat.setFontItalic(True)

TitleFormat = QtGui.QTextCharFormat()
TitleFormat.setFontPointSize(15)
TitleFormat.setFontWeight(QtGui.QFont.Bold)
TitleFormat.setVerticalAlignment(QtGui.QTextCharFormat.AlignMiddle)
# TitleFormat.setUnderlineStyle(QtGui.QTextCharFormat.SingleUnderline)

tableFormat = QtGui.QTextTableFormat()
tableFormat.setAlignment(QtCore.Qt.AlignHCenter)
tableFormat.setAlignment(QtCore.Qt.AlignLeft)
#tableFormat.setBackground(QtGui.QColor("#ffffff"))
tableFormat.setCellPadding(0)
tableFormat.setCellSpacing(0)
tableFormat.setBorder(1)
tableFormat.setHeaderRowCount(1)
#tableFormat.PageBreakFlag(tableFormat.PageBreak_AlwaysAfter)

headerFormat = QtGui.QTextCharFormat()
headerFormat.setFontPointSize(10)
headerFormat.setFontWeight(QtGui.QFont.Bold)

cellFormat = QtGui.QTextCharFormat()
cellFormat.setFontPointSize(10)

centerAlignment = QtGui.QTextBlockFormat()
centerAlignment.setAlignment(QtCore.Qt.AlignCenter)

OG = 5
OD = 1
stockColumn = 13

class myDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(myDialog, self).__init__()
        super(Ui_Dialog, self).__init__()

        self.setupUi(self)

    def getValues(self):
        if self.numRadio.isChecked():
            sort = 0
        elif self.rRadio.isChecked():
            sort = OD
        elif self.lRadio.isChecked():
            sort = OG
        return sort, self.stockCheckBox.isChecked()

    def on_acceptButton_clicked(self):
        self.close()

    def on_rejectButton_clicked(self):
        self.close()

def createpdf(model):

    dlg = myDialog()
    if dlg.exec_():
        sort, stock = dlg.getValues()

        new_filename = os.path.join(os.getcwd(), 'oryx_print_'+time.strftime('%Y-%m-%d_%Hh%M',time.localtime())+'.pdf')
        filename = QtWidgets.QFileDialog.getSaveFileName(None,
                       u'Choix du nom du fichier PDF',
                       new_filename, u'PDF (*.pdf)')[0]

        if filename != '':
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setOrientation(QtPrintSupport.QPrinter.Landscape)

            printer.setOutputFileName(filename)
            printtable(model, printer, sort, stock)

def printtable(model, printer, sortedcolum, stock):
    editor = QtWidgets.QTextBrowser()

    #Print title and print date/time
    editor.setCurrentCharFormat(TitleFormat)
    editor.setAlignment(QtCore.Qt.AlignCenter)
    editor.append(u'Trié par '+model.horizontalHeaderItem(sortedcolum).text())

    timestamp = u'Imprimé le : ' + time.strftime('%Y-%m-%d_%Hh%M',time.localtime())
    editor.setCurrentCharFormat(ItalicFormat)
    editor.append(timestamp)

    editor.setCurrentCharFormat(NormalFormat)

    cursor = editor.textCursor()
    cursor.beginEditBlock()

    # Calculate the number of rows to print
    if stock:
        rowCount = 0
        for row in range(model.rowCount()):
            if model.item(row, stockColumn).text() == "1":
                rowCount += 1
    else:
        rowCount = model.rowCount()

    #Create the table with the right number of rows and columns
    table = cursor.insertTable(rowCount+1, model.columnCount(), tableFormat)

    frame = cursor.currentFrame()
    frameFormat = frame.frameFormat()
    frameFormat.setBorder(0)
    frame.setFrameFormat(frameFormat)

    #Headers
    for i in range(model.columnCount()):
        # selecting the right cell
        titre = table.cellAt(0,i)

        # place cursor in the right place
        cellCursor = titre.firstCursorPosition()
        cellCursor.setBlockFormat(centerAlignment)

        # writing into the cell
        cellCursor.insertText(model.horizontalHeaderItem(i).text(), headerFormat)

    cell = QtGui.QTextTableCell()
    cellCursor = QtGui.QTextCursor()

    model.sort(sortedcolum, QtCore.Qt.AscendingOrder)

    rowPrint = 0
    for row in range(0, model.rowCount()):
        if (model.item(row, stockColumn).text() == "1") or (not stock):
            rowPrint += 1
            for col in range(table.columns()):
                cell = table.cellAt(rowPrint,col)
                cellCursor = cell.firstCursorPosition()
                cellCursor.setBlockFormat(centerAlignment)
                cellCursor.insertText(model.item(row,col).text(), cellFormat)

    model.sort(0, QtCore.Qt.AscendingOrder)

    # End editing table
    cursor.endEditBlock()

    # Printing
    editor.print_(printer)
