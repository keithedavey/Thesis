#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main.py: Main script for geoprocessing tasks"""

__appname__ = "Main.py"
__author__  = "Keith E. Davey (keithedavey@gmail.com)"
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
from Data import * 

from Mailer import mail
from Zip import createZipFile

try:
	tables = rd.tables()
	featureClasses = rd.featureClasses()
	# extractId(tables['t00040203_eng'], 'insert16' , 'geo', 'id', 'prefix')

	###########################
	# Extract ids from tables #
	###########################

	rawTables = {}

	# Start timer
	# start = time.clock()
	# l.write('Started extract ID task')
	# # l.write('Extraction ID started at: ' + str(start))

	# # Get list of raw tables
	# for tab in sorted(tables):
	# 	if '_eng' in tab[-4:]:
	# 		rawTables[tab] = tables[tab]


	# Extract ID from raw tables
	# for tab in sorted(rawTables):
	# 	try:
	# 		newTableName = tab + '_prefixid'
	# 		e.idFromTable(rawTables[tab], newTableName , 'geo', 'id', 'prefix')
	# 		l.write(tab + ' table IDs extracted')
	# 	except:
	# 		pass
			# l.write(tab + ' failed. Most likely already created... Moving on')

	# Stop timer
	# end = time.clock()
	# elapsed = (end - start)
	# l.write('Finsihed extract ID task')
	# l.write('Time for task: ' + str(elapsed) + ' seconds')

	tables = rd.tables()
	featureClasses = rd.featureClasses()

	newTables = {}

	for tab in sorted(tables):
		if '_prefixid' in tab[-9:]:
			newTables[tab] = tables[tab]

	# print newTables

	# Mail extract report
	# mail('kedavey90@gmail.com', 'ID extraction complete', 'ID extraction complete.\n\nProcess took ' + str(elapsed) + ' seconds.\n\nTables Created:\n' + newTables, None)



	geog = 'gcsd000a11a_e'
	# try:
	# 	a.intersect([featureClasses[geog], featureClasses['southernontarioboundary']], 'gcs_so')
	# except:
	# 	l.write("gcs_so alrady exists... Moving on")
	featureClasses = rd.featureClasses()
	start = time.clock()
	l.write('Started join task')
	# Iterate through new tables and join to feature classes
	for table in sorted(newTables):
		try:
			# Get list of unique columns of table from class attribute
			shortName = table[0:13]
			#print shortName
			columns = e.fieldsFromTable(table, tableName[shortName], columnPrimary[shortName], columnSecondary[shortName])
			for c in sorted(columns):
				print c, columns[c]
			# Join table to new fc with name geog_table
			newFcName = 'gcs_so' + '_' + table[:9]
			print 'New layer being created: ' + newFcName
			#print columnPrimary[shortName], columnSecondary[shortName]
			j.fcToTable(featureClasses['gcs_so'], tables[table], newFcName, columns, geogId[geog],  columnPrimary[shortName], columnSecondary[shortName])
			l.write(newFcName + ' joined successfully')
		except:
			pass
			l.write('Error during join: ' + traceback.format_exc())
	end = time.clock()
	elapsed = (end - start)
	l.write('Finsihed join task')
	l.write('Time for task: ' + str(elapsed) + ' seconds')




	#########################################
	# Clip by intersection of boundary File #
	#########################################

	# geographies = {}

	# # Start timer
	# start = time.clock()

	# for fc in featureClasses:
	# 	if 'e11a_e' in fc or 'a11a_e' in fc:
	# 		geographies[fc] = featureClasses[fc]

	# newFcs = ''

	# for g in geographies:
	# 	newFcName = g[1:3] + 'sa'
	# 	a.intersect([geographies[g], featureClasses['southernontarioboundary']], newFcName)
	# 	newFcs = newFcs + '\n' + newFcName

	# # Mail extract report
	# mail('kedavey90@gmail.com', 'Study area clipping complete', 'Study area clipping complete.\n\nProcess took ' + elapsed + ' minutes.\n\n Created:\n' + newFcs, None)

	####################
	# Table join by id #
	####################

	# Geography_Feature_Date

	# cd_t00040200_20150224

except Exception, err:	
	l.write('Error occured in script: ' + traceback.format_exc())

#######################
# Program entry point #
#######################
if __name__ == '__main__':
    main()