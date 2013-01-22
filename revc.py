#!/usr/bin/python
import sys
dnastring = sys.argv[1]
dnareversed = dnastring[::-1]
print dnareversed.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
