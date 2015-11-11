#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ExtractIdFromTable.py: Extracts ID from tables"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy
import FeatureClass as fc
import Table as tab
import time

def extractId(infc, outfc, extractFields):
	tab.copy(infc, outfc)
	with arcpy.da.SearchCursor(outfc, ['geo']) as cursor:
		for row in sorted(cursor):
			fid =  row[0].split('[')[1].split(']')[0]
			splitId = fid.split('CD')
			if len(splitId) > 1:
				print splitId[1]