#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print.py: Offers functionality to print out database tables and feature classes"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy
import RegisterData as rd

def featureClasses():
	featureClasses = rd.featureClasses()
	print "\nFeature Classes:"
	for fc in featureClasses:
		print fc + ': ' + featureClasses[fc]


def tables():
	tables = rd.tables()
	print "\nTables:"
	for tab in tables:
		print tab + ': ' + tables[tab]
