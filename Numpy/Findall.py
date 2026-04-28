#https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

import numpy

def arrays(arr):
    num_arr = numpy.array(arr[::-1], float)
    return num_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
