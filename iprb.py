#!/usr/bin/python
import sys

if len(sys.argv) != 4:
	exit()

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

def c2(n):
	return n*(n-1)/2

total = k*m + k*n + m*n + c2(k) + c2(m) + c2(n)
answer = (k*m + k*n + 0.5*m*n + c2(k) + 0.75*c2(m))/total

print answer
