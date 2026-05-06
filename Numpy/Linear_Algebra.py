#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy

A = []

for _ in range(int(input())):
    A.append(list(map(float, input().split())))

print(round(numpy.linalg.det(A), 2))
