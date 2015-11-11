#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main.py: Main script for geoprocessing tasks"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import os
import datetime
from Mailer import mail

def write(text):
	outPath = '../Log/'
	outFile = 'log.txt'
	logText = str(datetime.datetime.now()) + ' - ' + text + '\n'
	if not os.path.isdir(outPath):
		os.makedirs(outPath)
	with open(outPath + outFile, 'a') as f:
		f.write(logText)
		print logText
		#mail('kedavey90@gmail.com', 'RESISTOR - Geoprocessing task update', logText, None)
