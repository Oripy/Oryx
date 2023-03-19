# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:05:31 2013

@author: pierre
"""

import configparser
import os

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

def configSectionMap(section):
    """ Retreive values from a section of the config file
        return: a dictionnary containing all key: value from the section """
    dict1 = {}
    try:
        options = CONFIG.options(section)
    except configparser.NoSectionError:
        return False
    for option in options:
        try:
            dict1[option] = CONFIG.get(section, option)
            if dict1[option] == -1:
                print('skip: %s' % option)
        except:
            print('exception on %s!' % option)
            dict1[option] = None
    return dict1

MAIN = configSectionMap('Main')

FILENAME = MAIN['filename']
AUTOSAVE_INTERVAL = float(MAIN['autosave_interval'])
AUTOSAVE_MAX_NUM = int(MAIN['autosave_max_num'])
AUTOSAVE_DIR = os.path.join(os.getcwd(), 'autosave')
NBR_PER_BOX = int(MAIN['nbr_per_box'])

if 'pass' in MAIN:
    PASSWORD = MAIN['pass']

CORRECTION = configSectionMap('Correction')

MAX_SPHERE = float(CORRECTION['max_sphere'])
MIN_SPHERE = float(CORRECTION['min_sphere'])
STEP_SPHERE = float(CORRECTION['step_sphere'])
DEFAULT_SPHERE = float(CORRECTION['default_sphere'])

MAX_CYL = float(CORRECTION['max_cyl'])
MIN_CYL = float(CORRECTION['min_cyl'])
STEP_CYL = float(CORRECTION['step_cyl'])
DEFAULT_CYL = float(CORRECTION['default_cyl'])

MAX_AXIS = int(CORRECTION['max_axis'])
MIN_AXIS = int(CORRECTION['min_axis'])
STEP_AXIS = int(CORRECTION['step_axis'])
DEFAULT_AXIS = int(CORRECTION['default_axis'])

MAX_ADD = float(CORRECTION['max_add'])
MIN_ADD = float(CORRECTION['min_add'])
STEP_ADD = float(CORRECTION['step_add'])
DEFAULT_ADD = float(CORRECTION['default_add'])

SEARCH = configSectionMap('Search')

if SEARCH:

    MASTER_EYE_COEF = float(SEARCH['master_eye_coef'])

    SPHERE_DELTA_MAX = float(SEARCH['sphere_delta_max'])+.25
    SPHERE_DELTA_MIN = float(SEARCH['sphere_delta_min'])-.25

    CYL_DELTA_MAX = float(SEARCH['cyl_delta_max'])+.25
    CYL_DELTA_MIN = float(SEARCH['cyl_delta_min'])-.25

    PARAM_AXIS_TOL0 = float(SEARCH['param_axis_tol0'])
    PARAM_AXIS_TOL1 = float(SEARCH['param_axis_tol1'])
    PARAM_AXIS_TOL2 = float(SEARCH['param_axis_tol2'])

    ADD_DELTA_MAX = float(SEARCH['add_delta_max'])+.25

    SPHERE_COEF = float(SEARCH['sphere_coef'])
    CYL_COEF = float(SEARCH['cyl_coef'])
    AXIS_COEF = float(SEARCH['axis_coef'])
    ADD_COEF = float(SEARCH['add_coef'])

    SCORE_SHAPE_PARAM = float(SEARCH['score_shape_param'])

STOCK = configSectionMap("Stock")

if STOCK:
    # Config of colors for glasses tags
    UNIT_COLORS = [int(STOCK['unit'+str(a)], 16) for a in range(10)]

# Create the data file if it doesn't exists
open(FILENAME, 'a').close()

# Create autosaves dir if it doesn't exists
if not os.path.exists(AUTOSAVE_DIR):
    os.makedirs(AUTOSAVE_DIR)
