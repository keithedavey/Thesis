#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Table.py: Provides functionality related to tables"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy
import RegisterData as rd

# Execute Copy
def copy(inTab, outTab):
	arcpy.management.CopyRows(inTab, outTab)