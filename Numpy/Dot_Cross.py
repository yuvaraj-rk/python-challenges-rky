#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true

import numpy

N = int(input())

A, B = [], []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

np_A = numpy.array(A)
np_B = numpy.array(B)

print(numpy.dot(np_A, np_B))
