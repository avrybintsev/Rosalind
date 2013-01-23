#!/usr/bin/python
import sys
Ns = sys.argv[1:7]
N = [ int(n) for n in Ns ]
P = [ 1, 1, 1, 0.75, 0.5, 0 ]
print sum(2*n*p for n,p in zip(N, P))
