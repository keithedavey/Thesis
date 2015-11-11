##########################
# Author: Keith E. Davey #
# Purpose: Arcpy script  #
##########################

################
# Helpful info # 
################
# <toolname_<toolbox_alias>
# arcpy.mapping
# arcpy.da
# arcpy.sa
# arcpy.ga
# arcpy.na
# arcpy.time

###########
# Imports # 
###########
import arcpy, time
from Mailer import mail
from Zip import createZipFile

####################
# Global Variables # 
####################

workspaceDirectory = 'C:/Users/kedavey/Documents/GEOG607/Data/'

# Agricultural Ecumene Boundary File

agCdShp = 'Raw/AgriculturalEcumeneBoundaryFile/geca000e11a_eng/gcd_000e11a_e.shp'
agPrShp = 'Raw/AgriculturalEcumeneBoundaryFile/geca000e11a_eng/gpr_000e11a_e.shp'
agHyShp = 'Raw/AgriculturalEcumeneBoundaryFile/geca000e11a_eng/ghy_000e11a_e.shp'
agCaShp = 'Raw/AgriculturalEcumeneBoundaryFile/geca000e11a_eng/geca000e11a_e.shp'

# Census Agricultural Regions Boundary File

agReShp = 'Raw/CensusAgriculturalRegionsBoundaryFile/gcar000a11a_e/gcar000a11a_e.shp'

# Census Sub Division Digital Boundary File

agCsShp = 'Raw/CensusSubDivisionDigitalBoundaryFile/gcsd000a11a_e/gcsd000a11a_e.shp'

def printShpFields(f):
	print '|',
	for fld in f:
		print fld.name + ' |',
	print '\n'

# createZipFile('text.zip', workspaceDirectory)
# mail('kedavey90@gmail.com', 'hello!', 'Message', 'text.csv')
#####################
# Setup Environment # 
#####################

arcpy.env.workspace = workspaceDirectory

fields = arcpy.ListFields(agCsShp)
printShpFields(fields)

qry = '"PRNAME" = \'Ontario\''


# # Select by attribute
# sLayer = arcpy.management.MakeFeatureLayer(agCsShp, 'agRe')
# arcpy.management.SelectLayerByAttribute(sLayer, "NEW_SELECTION", qry)
# cnt = arcpy.management.GetCount(sLayer)
# print 'Count is: ' + str(cnt)

# Select by geography
try:
	sLayer = arcpy.management.MakeFeatureLayer(agCdShp, 'agCdLayer')
	arcpy.management.SelectLayerByLocation(sLayer, 'WITHIN', 'Derived/Geography/SouthernOntario.shp')
	arcpy.management.CopyFeatures(sLayer, 'WCD.shp')
	# cnt = arcpy.management.GetCount(sLayer)
	# print cnt
except:
	print 'Nope'


# start = time.clock()

# # Output results
# with arcpy.da.SearchCursor(agCsShp, ('SHAPE@TRUECENTROID', 'CSDNAME', 'CDNAME', 'PRNAME'), qry) as cursor:
# 	for row in sorted(cursor):
# 		print(str(row[0]) + ', ' + row[1] + ', ' + row[2])
# elapsed = (time.clock() - start)
# print 'Time for query: ' + str(elapsed) + ' seconds'

# try:
# 	outputFC = arcpy.GetParameterAsText(0)
# except:
# 	print "Fail!"
# print outputFC