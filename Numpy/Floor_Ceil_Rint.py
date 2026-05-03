#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy='1.13')

array = numpy.array(list(map(float, input().split())))

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
