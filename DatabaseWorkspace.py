#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DatabaseWorkspace.py: Main environment configuration file for a database environment."""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import arcpy

workspaceDirectory = 'Database Connections/Connection to localhost.sde/'

arcpy.env.workspace = workspaceDirectory