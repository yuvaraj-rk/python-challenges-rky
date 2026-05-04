#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true

import numpy

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

np_array = numpy.array(array)

np_min_array = numpy.min(np_array, axis=1)
print(numpy.max(np_min_array))
