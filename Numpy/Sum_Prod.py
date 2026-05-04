#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy

N, M = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

np_array = numpy.array(array)
np_add_array = numpy.sum(np_array, axis=0)

print(numpy.prod(np_add_array))
