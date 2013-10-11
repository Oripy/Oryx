# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:19:55 2013

@author: pierre
"""

from config import AUTOSAVE_DIR
import os
import time

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