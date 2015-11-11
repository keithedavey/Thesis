#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Zipper.py: Provides file zip functionality"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import os
import zipfile

def createZipFile(zipFileName, zipDirectory):
	# ZIP_STORED vs. ZIP_DEFLATED
	zipFile = zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED)
	files = os.listdir(zipDirectory)

	for file in files:
		if file.endswith('shp') or file.endswith('dbf') or file.endswith('shx') or file.endswith('csv'):
			zipFile.write(zipDirectory + file)

	for file in zipFile.namelist():
		print "Zipped " + file

	zipFile.close()