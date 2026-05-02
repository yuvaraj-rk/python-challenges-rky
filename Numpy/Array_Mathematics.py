#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy

N, M = map(int, input().split())
a, b = [], []

for _ in range(N):
    a.append(list(map(int, input().split())))

for _ in range(N):
    b.append(list(map(int, input().split())))

A = numpy.array(a)
B = numpy.array(b)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
