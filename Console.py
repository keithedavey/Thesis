#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Console.py: Interactive console to query tables and feature classes in database"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy
import Print as p
import RegisterData as rd
from DatabaseWorkspace import *

def run():
	while True:
		print '\n#########################'
		print '#ArcGIS Database Console#'
		print '#########################\n'
		print '\nOptions:\n'
		print 'f - Print Feature Classes'
		print 't - Print Tables\n'
		command = raw_input("Please enter a command\n")
		if command == 'f':
			p.featureClasses()
		elif command == 't':
			p.tables()
		elif command == 'q':
			print 'Quitting'
			return
		else: 
			print 'Not a valid option, try again'

if __name__ == "__main__":
	run()