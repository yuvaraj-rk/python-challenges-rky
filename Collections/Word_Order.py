#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

n = int(input())

distinct_strings = {}

for i in range(n):
    string = hash(input())   
    distinct_strings[string] = distinct_strings.get(string, 0) + 1

print(len(distinct_strings))
print(*distinct_strings.values())
