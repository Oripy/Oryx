# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:19:55 2013

@author: pierre
"""

from config import AUTOSAVE_DIR, AUTOSAVE_INTERVAL, AUTOSAVE_MAX_NUM, FILENAME
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
    with open(filename, "wb") as file_input:
        data_writer = csv.writer(file_input)
        for key, values in data.iteritems():
            data_writer.writerow([key]+values)
            
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