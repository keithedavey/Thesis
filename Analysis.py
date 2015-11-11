#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Analysis.py: Analysis functions"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy, time
import RegisterData as rd

tables = rd.tables()
featureClasses = rd.featureClasses()

def intersect(inFc, outFc):
	arcpy.analysis.Intersect(inFc, outFc)