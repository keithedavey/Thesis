#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Text.py: Write an element to an XML document"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import os
import xml.etree.cElementTree as ET

def writeToFile(outFile, tabName, data):

	outPath = '../Reference/'
	if not os.path.isdir(outPath):
		os.makedirs(outPath)
	#with open(outPath + outFile, 'w') as f:
	table = ET.Element("Table")
	columns = ET.SubElement(table, 'columns')
	name = ET.SubElement(table, 'name')
	name.text = tabName
	for d in sorted(data):
		column = ET.SubElement(columns, 'column')
		columnName = ET.SubElement(column, 'columnName')
		columnId = ET.SubElement(column, 'columnId')
		columnName.text = data[d]
		columnId.text = d

	ET.ElementTree(table).write(outPath + outFile)