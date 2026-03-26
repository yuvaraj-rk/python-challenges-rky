#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

_ = input()

array = list(input().split())
A = set(input().split())
B = set(input().split())

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
