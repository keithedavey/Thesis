#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Proximity.py: Extracts ID from tables"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy
import os
import time

# Define program globals #

# Directories
workingDirectory = 'E:\\Personal\\Data\\Thesis\\Data\\Derived\\'
outputDirectory = os.path.join(workingDirectory, 'ProximityCSD\\')
tempDirectory = os.path.join(workingDirectory, 'temp\\')
polygons = os.path.join(workingDirectory, 'SouthernOntarioCSDBoundary.shp')

outputFile = os.path.join(outputDirectory, 'polymerge.shp')

fields = ["CSDUID"]

# Call with getAdjancentPolygons(polygons, fields, 

def getAdjacentPolygonArea(polygons, joinField, tempFolder, outputFolder):

        # Make a layer out of the the original FC
        arcpy.MakeFeatureLayer_management(polygons, 'polygons')

        with arcpy.da.SearchCursor(fc, fields) as cursor:
            for row in cursor:

                # Define local variables    
                joinValue = str(row[0])
                
                # Select the current row in the UpdateCursor
                expression = str(joinField[0]) + ' = \'' + joinValue + '\'' 
                arcpy.SelectLayerByAttribute_management('polygons', 'NEW_SELECTION', expression)
                arcpy.AddMessage("Selection by attributes complete")
                print ("Selection by attributes complete")

                # Copy the selection to a new temporary feature
                tempAttrSelect = os.path.join(tempDirectory, 'tempAttrSelect' + row[0] +'.shp')
                arcpy.CopyFeatures_management('polygons', tempAttrSelect)
                arcpy.AddMessage("Copy complete")
                print ("Copy complete")
                
                # Make the temp feature a layer
                arcpy.MakeFeatureLayer_management(tempAttrSelect, 'tempAttrSelect')
                arcpy.AddMessage("Feature layer created")
                print ("Feature layer created")

                # Select all features 
                arcpy.SelectLayerByLocation_management('polygons', 'BOUNDARY_TOUCHES', 'temp', '', 'ADD_TO_SELECTION')
                arcpy.AddMessage("Select by Location complete")
                print ("Select by Location complete")

                # Copy the selection to a new temporary feature
                tempLocSelect = os.path.join(tempDirectory, 'tempLocSelect' + row[0] +'.shp')
                arcpy.CopyFeatures_management('polygons', tempLocSelect)
                arcpy.AddMessage("Copy complete")
                print ("Copy complete")

                # Make the temp feature a layer
                arcpy.MakeFeatureLayer_management(tempLocSelect, 'tempLocSelect')
                arcpy.AddMessage("Feature layer created")
                print ("Feature layer created")

                outputAdjPoly = os.path.join(outputDirectory, row[0] + '.shp')
                arcpy.Dissolve_management('tempLocSelect', outputAdjPoly)

                # Clean up workspace, removing layers
                arcpy.RemoveLayer('polygon')

                # Delete intermediate data
                arcpy.Delete_management('tempAttrSelect')
                arcpy.Delete_management(tempAttrSelect)

                arcpy.Delete_management('tempLocSelect')
                arcpy.Delete_management(tempLocSelect)

def addField():
    for file in os.listdir(outputDirectory):
        splitFile = file.split('.')
        if len(splitFile) == 2 and splitFile[1] == 'shp':
                currentLayer = os.path.join(outputDirectory + splitFile[0] + '.shp')
    
                arcpy.MakeFeatureLayer_management(currentLayer, 'currentLayer')
                arcpy.AddField_management(currentLayer, 'CSDUID', 'TEXT')

                arcpy.Delete_management('currentLayer')
                
def updateField():
    for file in os.listdir(outputDirectory):
        splitFile = file.split('.')
        if len(splitFile) == 2 and splitFile[1] == 'shp':
                currentLayer = os.path.join(outputDirectory + splitFile[0] + '.shp')
    
                arcpy.MakeFeatureLayer_management(currentLayer, 'currentLayer')
                
                with arcpy.da.UpdateCursor('currentLayer', fields) as updateCursor:
                        for updateRow in updateCursor:
                                updateRow[0] = splitFile[0]
                                updateCursor.updateRow(updateRow)
                        print updateRow[0]
                arcpy.Delete_management('currentLayer')



def mergePolygons(output):
        arcpy.CreateFeatureclass_management(outputDirectory, 'polymerge.shp', 'POLYGON', os.path.join(outputDirectory + '3538007' + '.shp'))
        for file in os.listdir(outputDirectory):
                splitFile = file.split('.')
                if len(splitFile) == 2 and splitFile[1] == 'shp':
                        print splitFile[0]
                        currentLayer = os.path.join(outputDirectory + splitFile[0] + '.shp')
                        arcpy.MakeFeatureLayer_management(currentLayer, 'currentLayer')
                        arcpy.Append_management([currentLayer], output)
                        arcpy.Delete_management('currentLayer')



        # # Process: Select Layer By Attribute
        # arcpy.SelectLayerByAttribute_management(SouthernOntarioCSDBoundary, "CLEAR_SELECTION", "")
