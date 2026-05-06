#https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true

import numpy

P = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(P, x))
