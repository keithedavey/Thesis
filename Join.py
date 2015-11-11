#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Join.py: Extracts ID from tables"""

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
import RegisterData as rd

def fcToTable(inFc, inTab, outFc, columns, idField, fieldPrimary, fieldSecondary):
	fc.copy(inFc, outFc)
	fcs = rd.featureClasses()
	tables = rd.tables()
	for c in sorted(columns):
		arcpy.management.AddField(fcs[outFc], c, 'FLOAT')
	col = columns.keys()	
	col.append(idField)

	with arcpy.da.UpdateCursor(fcs[outFc], col) as fcCursor:
		# print fcCursor.fields
		for fcRow in fcCursor:
			if fieldSecondary == '':
				with arcpy.da.SearchCursor(inTab, ['id', fieldPrimary, 'value']) as tabCursor:
					for tabRow in sorted(tabCursor):
						# Match Feature Class ID to table ID
						#print str(fcRow[-1][0:2]) 
						if str(fcRow[-1]) == str(tabRow[0]):
							for i in range(len(col)-1):
								if columns[col[i]] == tabRow[1]:
									if tabRow[2] != 'x':
										fcRow[i] = tabRow[2]
										#print tabRow[2]
									else:
										fcRow[i] = -1
										#print tabRow[2]
									fcCursor.updateRow(fcRow)
			else:
				with arcpy.da.SearchCursor(inTab, ['id', fieldPrimary, fieldSecondary, 'value']) as tabCursor:
					for tabRow in tabCursor:
						# Match Feature Class ID to table ID
						if str(fcRow[-1]) == str(tabRow[0]):
							for i in range(len(col)-1):
								if columns[col[i]] == tabRow[1] + ' (' + tabRow[2] + ')':
									if tabRow[3] != 'x':
										fcRow[i] = tabRow[3]
									else:
										fcRow[i] = -1
									fcCursor.updateRow(fcRow)
			#fcCursor.updateRow(fcRow)