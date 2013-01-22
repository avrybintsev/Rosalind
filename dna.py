#!/usr/bin/python
import sys
dnastring = sys.argv[1]
for character in 'ACGT':
    print dnastring.count(character)