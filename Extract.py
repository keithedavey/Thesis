#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract.py: Extracts ID from tables"""

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
import Text as t
from operator import itemgetter, attrgetter, methodcaller

# idFromTable: Extracts the unique identifier of each row from a table
# for given inField (CD30515413), extract output fields by splitting and assigning outPrefixField to CD and outIdField to 30515413
def idFromTable(infc, outfc, inField, outIdField, outPrefixField):
	tab.copy(infc, outfc)
	tables = rd.tables()
	arcpy.management.AddField(tables[outfc], outIdField, 'TEXT')
	arcpy.management.AddField(tables[outfc], outPrefixField, 'TEXT')

	with arcpy.da.UpdateCursor(tables[outfc], (inField, outIdField, outPrefixField)) as cursor:
		for row in cursor:
			inSplit =  row[0].split('[')[1].split(']')[-2]
			fid = None
			prefix = None
			if 'CD' in inSplit:
				fid = inSplit.split('CD')[1]
				fid = fid[0:2] + fid[4:]
				fid = fid[0:4]
				prefix = 'CD'
			elif 'CCS' in inSplit:
				fid = inSplit.split('CCS')[1]
				fid = fid[0:2] + fid[4:]
				prefix = 'CCS'
			elif 'CAR' in inSplit:
				fid = inSplit.split('CAR')[1]
				prefix = 'CAR'
			elif 'PR' in inSplit:
				fid = inSplit.split('PR')[1]
				prefix = 'PR'
			else:
				fid = inSplit
				prefix = 'CO'
			
			# print fid
			row[1] = fid
			row[2] = prefix
			cursor.updateRow(row)

# Extracts a list of the unique class fields from a table
# given a (assumed) triple of data (item, unit, value) or simple double of data (item, value), extract the unique class fields from the table and write to xml
def fieldsFromTable(tab, tableName, fieldPrimary, fieldSecondary):
	tables = rd.tables()
	firstRowFlag = True
	attributes = {}
	prefix = 'at'
	i = 0
	if fieldSecondary == '':
		with arcpy.da.SearchCursor(tables[tab], ['id', fieldPrimary]) as cursor:
			for row in sorted(cursor, key=itemgetter(0)):
				if firstRowFlag:
					ref = row[0]
					fid = 'tc' + str(i).zfill(2) 
					attributes[fid] = row[1]
					i+=1
					firstRowFlag = False
				elif ref == row[0]:
					fid = 'tc' + str(i).zfill(2) 
					attributes[fid] = row[1]
					i+=1
				else:
					break
			
			t.writeToFile(tab[:9] + '.xml', tableName, attributes)
	else: 
		with arcpy.da.SearchCursor(tables[tab], ['id', fieldPrimary, fieldSecondary]) as cursor:
			for row in sorted(cursor, key=itemgetter(0)):
				if firstRowFlag:
					ref = row[0]
					fid = 'tc' + str(i).zfill(2) 
					attributes[fid] = row[1] + ' (' + row[2] + ')'
					i+=1
					firstRowFlag = False
				elif ref == row[0]:
					fid = 'tc' + str(i).zfill(2) 
					attributes[fid] = row[1] + ' (' + row[2] + ')'
					i+=1
				else:
					break
			
			t.writeToFile(tab[:9] + '.xml', tableName, attributes)
	return attributes