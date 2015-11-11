#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""FeatureClass.py: Provides functionality related to feature classes"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy, time
import traceback
import Log as l

# Query structured like this: '"prname" = \'Ontario\''

# fc.select(gcsd, 'test', '"prname" = \'Ontario\'', 'NEW_SELECTION'):

def select(infc, outfc, query, selectType):
	try:
		sLayer = arcpy.management.MakeFeatureLayer(infc, 'selectLayer')
		arcpy.management.SelectLayerByAttribute(sLayer, selectType, query)
		arcpy.management.CopyFeatures(sLayer, outfc)
	except:
		print 'Selection Failed'

def copy(infc, outfc):
	try:
		#sLayer = arcpy.management.MakeFeatureLayer(infc, 'selectLayer')
		arcpy.management.CopyFeatures(infc, outfc)
	except:
		l.write('Error occured in script: ' + traceback.format_exc())
		print 'Copy Failed'
	finally:
		print 'Copy outfc: ' + outfc 
