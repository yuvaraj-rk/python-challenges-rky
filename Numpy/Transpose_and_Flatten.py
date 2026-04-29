#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy

N = int(input().split()[0])

array = []
for _ in range(N):
    a = list(map(int, input().split()))
    array.append(a)

print(numpy.array(array).transpose())
print(numpy.array(array).flatten())
