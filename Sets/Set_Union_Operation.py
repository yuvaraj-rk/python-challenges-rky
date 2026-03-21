#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

n = input()
english=set(map(int, input().split()))
b=input()
french=set(map(int, input().split()))

print(len(english.union(french)))
