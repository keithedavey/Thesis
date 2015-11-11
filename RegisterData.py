#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""RegisterData.py: Registers tables and feature classes within database into dictionaries with shortnames as keys and path as value"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy

def featureClasses():
	fcList = {}
	fcs = arcpy.ListFeatureClasses()
	for fc in fcs:
		fcList[fc.split('.')[2]] = fc
	return fcList


def tables():
	tabList = {}
	tabs = arcpy.ListTables()	
	for tab in tabs:
		tabList[tab.split('.')[2]] = tab
	return tabList