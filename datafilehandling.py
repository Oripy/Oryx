# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:19:55 2013

@author: pierre
"""

from PyQt5 import QtWidgets
from config import AUTOSAVE_DIR, AUTOSAVE_INTERVAL, AUTOSAVE_MAX_NUM, FILENAME
from formatting import getData

import os
import time
import csv

def getListAutosaves():
    """ returns the list of autosave files in autosave folder """
    list_autosaves = os.listdir(AUTOSAVE_DIR)
    for item in list_autosaves:
        if item[:18] != 'oryxdata_autosave_':
            list_autosaves.remove(item)
    list_autosaves.sort()
    return list_autosaves

def getLastAutoSaved():
    """ returns the time and date of the last autosaved file
        if no autosave file, returns epoch (1970-01-01_01h00) """
    if len(getListAutosaves()) > 0:
        return time.strptime(getListAutosaves()[-1][18:-4], '%Y-%m-%d_%Hh%M')
    else:
        return time.localtime(0)

def writeCsv(data, filename = FILENAME):
    """ Write data in the CSV file """
    print(filename)
    with open(filename, "wt", encoding="ISO-8859-1") as file_input:
        data_writer = csv.writer(file_input, lineterminator="\n")
        for key, values in data.items():
            data_writer.writerow([key]+values)

def loadCsv(filename = FILENAME):
    """ Returns data from the CSV file """
    data = dict()
    with open(filename, "rt", encoding="ISO-8859-1") as file_input:
        for row in csv.reader(file_input):
            data[int(row[0])] = [getData(row[a]) for a in range(14)[1:]]
    return data

def autoSave(data):
    """ Autosaves if more than AUTOSAVE_INTERVAL seconds without save """
    if (time.time() - time.mktime(getLastAutoSaved())) > AUTOSAVE_INTERVAL:
        new_filename = os.path.join(AUTOSAVE_DIR, 'oryxdata_autosave_'
            ''+time.strftime('%Y-%m-%d_%Hh%M',time.localtime())+'.csv')
        writeCsv(data, new_filename)

        list_autosaves = getListAutosaves()
        if len(list_autosaves) > AUTOSAVE_MAX_NUM:
            for item in list_autosaves[:(
                    len(list_autosaves) - AUTOSAVE_MAX_NUM)]:
                os.remove(os.path.join(AUTOSAVE_DIR, item))

def backup():
    """ Open a File Chooser dialog and saves the datafile to a new file """
    new_filename = os.path.join(os.getcwd(),
            'oryxdata_backup_' + \
            time.strftime('%Y-%m-%d_%Hh%M', time.localtime()) + '.csv')
    filename = QtWidgets.QFileDialog.getSaveFileName(None,
            u'Choix du nom de fichier de Backup',
            new_filename, u'csv (*.csv)')[0]
    if filename != '':
        data = loadCsv()
        writeCsv(data, filename)

def restore():
    """ After a warning, open a File Chooser dialog and load the data in the
       selected file a new data """
    text = (u'Attention, l\'ensemble des données actuelles seront '
            u'perdues et\n remplacées par les données du fichier de '
            u'backup sélectionné.\n\n Souhaitez-vous continuer ?')
    question = QtWidgets.QMessageBox.warning(None,
        u'Ecraser les données ?',
        text,
        QtWidgets.QMessageBox.Yes,
        QtWidgets.QMessageBox.No)

    if question == QtWidgets.QMessageBox.Yes:
        filename = QtWidgets.QFileDialog.getOpenFileName(None,
                   u'Choix du fichier de Backup à restaurer',
                   os.getcwd(), u'csv (*.csv)')[0]
        if filename != '':
            data = loadCsv(filename)
            writeCsv(data)
            return data
        else:
            return []
    else:
        return []
