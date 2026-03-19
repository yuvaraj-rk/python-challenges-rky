#https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

from itertools import groupby

string = input()
result = ""

for k, g in groupby(string):
    result += f"({len(list(g))}, {k}) "

print(result)
