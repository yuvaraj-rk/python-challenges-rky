#https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy

arr = list(map(int,input().split()))
print(numpy.reshape(arr, (3,3)))
