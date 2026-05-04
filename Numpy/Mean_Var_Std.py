#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

np_array = numpy.array(array)

print(numpy.mean(np_array, axis=1))
print(numpy.var(np_array, axis=0))
print(round(numpy.std(np_array), 11))
