#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Publish.py: Main script for geoprocessing tasks"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy, time
from DatabaseWorkspace import *
import FeatureClass as fc
import Table as tab
import Print as p
import RegisterData as rd
import Extract as e
import Analysis as a
import Join as j
import Log as l
import traceback

from Mailer import mail
from Zip import createZipFile

try:
	tables = rd.tables()
	featureClasses = rd.featureClasses()