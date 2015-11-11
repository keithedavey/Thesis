#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main.py: Calculates pearson coefficent using all variables starting with 'tc', then calculates squared sum amongst all other variables"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import csv

from itertools import izip

import scipy
from scipy.stats import pearsonr

filename = '00040242-eng.csv'

def calculateScore(variable0, variable1):
	score = 0
	for variable in variableCorrelations[variable0]:
		if not variable == variable1:
			score = score + (variableCorrelations[variable0][variable][0] - variableCorrelations[variable1][variable][0])**2
	normalizedScore = score/(len(variableCorrelations)-1)
	return normalizedScore

# with open(filename, 'rb') as file:
# 	reader = csv.reader(file)
# 	print reader

a = izip(*csv.reader(open(filename, "rb")))
csv.writer(open(filename + "trans.csv", "wb")).writerows(a)

columnDictionary = {}

with open(filename + "trans.csv", 'rb') as file:
	reader = csv.reader(file)
	for row in reader:
		columnName = row[0]
		if columnName.startswith('tc'):
			columnDictionary[columnName] = []
			count = 1
			while(True):
				try:
					columnDictionary[columnName].append(float(row[count]))
					count+=1
				except:
					#print columnDictionary[columnName]
					break

variableCorrelations = {}
i = 0
j = 0
while i < len(columnDictionary):
	j+=1
	if j == len(columnDictionary):
		i+=1
		j=i+1
	if i == len(columnDictionary) - 1:
		break
	r, p = scipy.stats.pearsonr(columnDictionary.values()[i],columnDictionary.values()[j])

	# print columnDictionary.keys()[i] + columnDictionary.keys()[j]
	# print 'R value: ' + str(r) + 'P value: ' + str(p) + '\n' 

	if columnDictionary.keys()[i] in variableCorrelations:
		pass
	else:
		variableCorrelations[columnDictionary.keys()[i]] = {}
	variableCorrelations[columnDictionary.keys()[i]][columnDictionary.keys()[j]] = [r, p]

	if columnDictionary.keys()[j] in variableCorrelations:
		pass
	else:
		variableCorrelations[columnDictionary.keys()[j]] = {}
	variableCorrelations[columnDictionary.keys()[j]][columnDictionary.keys()[i]] = [r, p]

for variable in variableCorrelations:
	print variable
	for each in variableCorrelations[variable]:
		print each, variableCorrelations[variable][each] 
	print '\n'




variableScores = {}
i = 0
j = 0
while i < len(columnDictionary):
	j+=1
	if j == len(columnDictionary):
		i+=1
		j=i+1
	if i == len(columnDictionary) - 1:
		break

	if columnDictionary.keys()[i] + '-' + columnDictionary.keys()[j] in variableScores:
		pass
	else:
		variableScores[columnDictionary.keys()[i] + '-' + columnDictionary.keys()[j]] = [calculateScore(columnDictionary.keys()[i], columnDictionary.keys()[j]), variableCorrelations[columnDictionary.keys()[j]][columnDictionary.keys()[i]]]
for variable in variableScores:
	if variableScores[variable][0] < 0.05 and variableScores[variable][1][0] > 0.70 and 'tc00' not in variable:
		print variable, variableScores[variable]
print '\n'

for variable in variableScores:
	if variableScores[variable][0] < 0.05 and variableScores[variable][1][0] > 0.5 and variableScores[variable][1][0] < .7:
		print variable, variableScores[variable]
print '\n'

for variable in variableScores:
	if variableScores[variable][0] < 0.05 and variableScores[variable][1][0] > 0.0 and variableScores[variable][1][0] < .5:
		print variable, variableScores[variable]

