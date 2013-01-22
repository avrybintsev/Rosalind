#!/usr/bin/python
import sys

f = open(sys.argv[1],'r')
text = f.readlines()
f.close()

def percent(dnastring):
	if (len(dnastring) > 0):
		return (dnastring.count('G')+dnastring.count('C'))*100.0/(len(dnastring))
	else:
		return 0

maxName = ''
maxValue = 0

curName = ''
curValue = 0

dna = ''

for line in text:
	if (line[0] == '>'):
		dna = dna.replace('\n','')
		curValue = percent(dna)
		if (curValue > maxValue):
			maxValue = curValue
			maxName = curName
		curName = line
		curValue = 0
		dna = ''
	else:
		dna += line

curValue = percent(dna)
if (curValue > maxValue):
	maxValue = curValue
	maxName = curName

print maxName[1:-1]
print str(maxValue)+"%"
