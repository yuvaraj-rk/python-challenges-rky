#https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

#!/bin/python3

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_string=""
for column in range(m):
    for row in range(n):
        decoded_string += matrix[row][column]

regex = r"(?<=\w)\W+(?=\w)"
final_decoded_str = re.sub(regex, " ", decoded_string,)

print(final_decoded_str)
